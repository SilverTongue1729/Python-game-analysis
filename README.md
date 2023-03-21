# Python-game-analysis

## DASS Assignment 2

Analysis of a python game, with a uml diagram, list of bugs and code smells

## Code Smells

<!-- ### 1) Rename Files to follow PEP 8 (not sure whether to include)

change all file names to lowercase and separate words using underscore in the file name  -->

### 2) Repeated code files (Bonus)

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

<!-- ### 3) Indecent Exposure (not applicable in python??)

make all variables private unless necessary -->

### 4) Unused Imports

Remove Unused imports

### 5) Unnecessary Code

- `Village.py` method `Update()` is never used
- `checkBuilding()` and `checkTroop()` always return `true` and are not required, they are used only because `AddBuildingOrWeaponToVillage()` is actually used as an `AddBuilding()` and `AddTroop()` is used for troop

### 6) Unnecessary Class StartingEnding (Bonus)

- Lazy Class, can replace the appropriate functions directly in Game.py

<!-- ### 7) Unnecessary Class Troops (combine with Army) (Bonus) -->

### 8) Unnecessary Classes in input.py (Bonus)

- Lazy Classes, can replace the with functions make small change in Game.py

## Bugs

### 1) Full size terminal (Bonus)

Readme doesn't mention that the terminal must be in full size for the program to run
