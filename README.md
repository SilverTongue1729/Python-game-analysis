# Python-game-analysis

# DASS Assignement 2

Analysis of a python game, with a uml diagram, list of bugs and code smells

## Code Smells

### 1) Rename Files to follow pep 8

change all file names to lowercase and separate words using underscore in the file name 

### 2) Repeated code files (included in Bonus)

Restructure directory as

```md
.
├── README.md
├── game.py
├── replay.py
├── src
│   ├── army.py
│   ├── central_processing_unit.py
│   ├── engine.py
│   ├── infrastructure.py
│   ├── input.py
│   ├── starting_ending.py
│   └── village.py
└── replays
    └── ...

```

## Bugs

### 1) Full size terminal

Readme doesn't mention that the terminal must be in full size for the program to run
