// Projects shown on the Projects page. Edit freely; order = order on the page.
const GH = "https://github.com/abdullahforecasts/";
const PROJECTS = [
  {
    name: "Multi-Agent Knowledge Graph Engine",
    desc: "Turns plain-English questions into safe SQL using FAISS retrieval, a NetworkX schema graph, and a small pipeline of LLM agents.",
    url: GH + "multiagent-vector-graph-engine"
  },
  {
    name: "Distributed Transformer",
    desc: "A transformer decoder split across several devices, built to study how model size trades off against communication overhead.",
    url: GH + "Distributed-Transformer-"
  },
  {
    name: "LLM Inference Pruning Benchmarks",
    desc: "Benchmarks measuring how pruning changes the speed and output quality of large language model inference.",
    url: GH + "llm-inference-pruning-benchmarks"
  },
  {
    name: "Inference Engine",
    desc: "A model inference engine written from scratch, to understand how serving works underneath the frameworks.",
    url: GH + "Inference-Engine"
  },
  {
    name: "IntegrityGuard AI",
    desc: "A web-based academic integrity analyzer that flags likely plagiarism and machine-generated work.",
    url: GH + "IntegrityGuard-AI"
  },
  {
    name: "OFS: File-Verse",
    desc: "A single binary-file container that behaves as a file system, letting multiple users read and write it at the same time.",
    url: GH + "OFS"
  },
  {
    name: "Micro Editor",
    desc: "A lightweight terminal-style text editor in C++ with search and replace, undo and redo, and chapter and section structure.",
    url: GH + "Micro_Editor"
  },
  {
    name: "Spendee",
    desc: "A personal finance app built in Flutter and Dart for tracking spending and budgets. More than a cash app.",
    url: GH + "Spendee"
  },
  {
    name: "Karatsuba Visualizer",
    desc: "An interactive visualizer for the Karatsuba fast-multiplication algorithm, built as a teaching aid.",
    url: GH + "Karatsuba-Vis"
  },
  {
    name: "MyLeetCode",
    desc: "My worked solutions to the LeetCode problems I have solved, kept in one place in C++.",
    url: GH + "MyLeetCode"
  },
  {
    name: "Chess",
    desc: "A two-player chess game in C++ and Raylib with full rules: castling, en passant, promotion, and check detection.",
    url: GH + "Chess"
  },
  {
    name: "Gravity Duck",
    desc: "A gravity-flipping platformer in C++ and Raylib with a shop system, currency exchange, and unlockable skins.",
    url: GH + "Gravity-Duck"
  },
  {
    name: "Metal Maniac",
    desc: "An object-oriented side-scrolling shooter with a shop system, unlockable themes, and persistent progress.",
    url: GH + "Metal-Maniac"
  },
  {
    name: "Plants vs Zombies",
    desc: "A polished C++ and Raylib replica of the classic Plants vs Zombies, built around object-oriented design.",
    url: GH + "Plants-Vs-Zombies"
  }
];
