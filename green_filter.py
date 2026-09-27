import numpy as np, glob, os, json
from PIL import Image, ImageFilter, ImageOps
SRC=os.environ.get('SRC','MyArtWork')
PAINT={'Castle.jpg','beach.jpg','lion with his grl.jpg'}
BG=(253,248,238)  # page cream
def hx(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)],float)
FILTERS={
 'forest':  dict(name='Forest Ink',      stops=['#173f2c','#ffffff'], gamma=0.9, lo=0.10, hi=0.92),
 'sage':    dict(name='Sage Pencil',     stops=['#4f7358','#ffffff'], gamma=0.75,lo=0.00, hi=0.95),
 'emerald': dict(name='Emerald Pen',     stops=['#0b6b42','#ffffff'], gamma=1.4, lo=0.35, hi=0.85),
 'moss':    dict(name='Moss & Olive',    stops=['#3f4f1e','#ffffff'], gamma=0.9, lo=0.08, hi=0.92),
 'verdigris':dict(name='Verdigris Teal', stops=['#135f58','#ffffff'], gamma=0.9, lo=0.08, hi=0.92),
 'bluetri':dict(name='Blue Tri-tone',stops=['#0c3a68','#3a94d8','#ffffff'], gamma=0.9, lo=0.08, hi=0.92),
 'botanical':dict(name='Botanical Tri-tone',stops=['#10301f','#3f8f5e','#ffffff'], gamma=0.9, lo=0.08, hi=0.92),
}
def prep(path, size=720):
    im=Image.open(path); im=ImageOps.exif_transpose(im).convert('L'); im.thumbnail((size,size),Image.LANCZOS)
    g=np.asarray(im,float)/255
    if os.path.basename(path) not in PAINT:
        # flatten paper: divide by heavily blurred copy -> paper becomes white, lighting evened
        bg=np.asarray(im.filter(ImageFilter.GaussianBlur(max(im.size)/7)),float)/255
        g=np.clip(g/np.maximum(bg,1e-3),0,1)**1.5
    else:
        g=np.asarray(ImageOps.autocontrast(im,cutoff=1),float)/255
    return g
def apply(g,f):
    t=np.clip((g-f['lo'])/(f['hi']-f['lo']),0,1)**f['gamma']
    st=[hx(s) for s in f['stops']]
    if len(st)==2: rgb=st[0]*(1-t[...,None])+st[1]*t[...,None]
    else:
        a=np.clip(t*2,0,1)[...,None]; b=np.clip(t*2-1,0,1)[...,None]
        rgb=np.where(t[...,None]<0.5, st[0]*(1-a)+st[1]*a, st[1]*(1-b)+st[2]*b)
    return Image.fromarray(rgb.astype(np.uint8))

import sys
size=int(sys.argv[1]); outdir=sys.argv[2]
names=sorted(os.path.basename(p) for p in glob.glob(SRC+'/*.jpg'))
for k in list(FILTERS)+['original']: os.makedirs(f'{outdir}/{k}',exist_ok=True)
for n in names:
    g=prep(os.path.join(SRC,n),size); base=os.path.splitext(n)[0].replace(' ','_')
    o=ImageOps.exif_transpose(Image.open(os.path.join(SRC,n))).convert('RGB'); o.thumbnail((size,size)); o.save(f'{outdir}/original/{base}.jpg',quality=82)
    for k,f in FILTERS.items(): apply(g,f).save(f'{outdir}/{k}/{base}.jpg',quality=82)
