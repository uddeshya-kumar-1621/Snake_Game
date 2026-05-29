**📌 Project Overview**
This is a fully-featured Snake Game built using Python's turtle module — no external dependencies required. The project was developed as a complete software solution with a clear separation between frontend (visuals) and backend (game logic), demonstrating clean code structure, OOP principles, and thoughtful UX design.
The game features a proper start screen, live in-game HUD, game over state, and a high score that persists between sessions — so the player never loses their best run.

**🗂️ Repository Structure**
**Snake-Game/**

│
├── Golden Response/
│   ├── snake_game.py          # Complete game implementation
│   ├── backend Game Logic.md  # Backend logic documentation
│   └── frontend.md            # Frontend/UI documentation
│
├── PROMPT.md                  # Project brief and requirements
├── JUSTIFICATION.md           # Design decisions and justifications
└── README.md                  # This file

✨ Features
FeatureDetails🎮 Smooth MovementGrid-based 20px steps, no stuttering or visual glitches🖥️ Styled WindowDark background (#1a1a2e), visible play border, 600×600px🐍 Distinct SnakeWhite/light-green head, orange body segments🍎 Dynamic FoodRandom shape (square, circle, triangle) + random color each spawn📊 Live Score HUDCandara 24pt bold — only redraws when score changes💾 Persistent High ScoreSaved to highscore.txt, survives between sessions🚀 Progressive SpeedStarts at 0.1s delay, -0.001s per food, floored at 0.05s🔄 Full Game StatesStart screen → Gameplay → Game Over → Restart⌨️ Dual ControlsWASD + Arrow keys both supported🧱 Visible BorderDrawn with Turtle so player knows exact play boundaries✍️ SignatureCoder: Uddeshya shown on screen throughout

🏗️ Architecture
This project is designed with a clear separation of concerns:
Backend (Game Logic)
Handles all the rules, state, and data of the game:

Snake movement, direction control, and 180° reversal prevention
Collision detection — wall hits (±290 boundary) and self-collision (< 20px)
Food spawning — random position, never overlapping the snake body
Score tracking and high score persistence (highscore.txt)
Game state machine — START → PLAYING → GAME_OVER → RESTART
Speed progression — delay decreases with each food eaten

Frontend (UI / Visuals)
Handles everything the player sees:

Dark-themed game window with wn.tracer(0) + manual wn.update() to eliminate flicker
Snake rendering — head vs body color distinction
Score display using pen.write() — redraws only on change (performance-conscious)
Food visual — randomized shape and color on every spawn
Start screen with title, instructions, and loaded high score
Game over screen with final score and replay options
Bottom signature line — always visible


🎮 Controls
ActionKeyAlternativeMove UpW↑ Up ArrowMove DownS↓ Down ArrowMove LeftA← Left ArrowMove RightD→ Right ArrowStart / RestartSPACE—QuitQClose window

Note: 180° reversal is blocked — pressing the opposite direction has no effect, preventing instant self-collision.


🕹️ Game States
┌─────────────────┐     SPACE      ┌─────────────────┐
│   START SCREEN  │ ─────────────► │    GAMEPLAY     │
│                 │                │                 │
│  - Title        │                │  - Snake moves  │
│  - Instructions │                │  - Food spawns  │
│  - High Score   │                │  - Score live   │
└─────────────────┘                └────────┬────────┘
         ▲                                  │
         │                           Wall / Self hit
         │                                  │
         │              SPACE        ┌──────▼────────┐
         └───────────────────────────│  GAME OVER    │
                                     │               │
                                     │  Final score  │
                                     │  SPACE/Q      │
                                     └───────────────┘

📈 Difficulty Progression
Score RangeFrame DelayFeel0 – 500.100s → 0.095sRelaxed60 – 1500.094s → 0.085sGetting faster160 – 3000.084s → 0.070sChallenging300+Floored at 0.050sExpert level

🔧 Collision Logic
Wall Collision — triggered when head exceeds ±290 on x or y axis:

Freeze for 1 second (player sees what happened)
Head returns to (0, 0)
All body segments sent off-screen to (1000, 1000) and cleared
Score resets to 0, delay resets to 0.1
Score display redraws

Self Collision — triggered when any segment is < 20px from head:

Same full reset process as wall collision

Food Collision — triggered when head is < 20px from food:

Food teleports to new random position (guaranteed not on snake body)
New segment added at tail
Score +10, delay -0.001
Food gets new random shape and color


💾 High Score Persistence
python# On startup — read from file
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except (FileNotFoundError, ValueError):
    high_score = 0

# On new high score — write to file
with open("highscore.txt", "w") as f:
    f.write(str(high_score))

File missing (first run) → starts at 0 gracefully ✅
File corrupted → catches ValueError, defaults to 0 ✅
Game closed mid-session → score already written on beat ✅


🐛 Error Handling
ScenarioHandlingWindow closed mid-gameturtle.Terminator caught → clean exit, no tracebackhighscore.txt missingFileNotFoundError → defaults to 0Corrupted score fileValueError → defaults to 0Speed underflowDelay floored at 0.050 — always playableFood spawns on snakeLoop regenerates coordinates until clear position found

🚀 How to Run
bash# Clone the repository
git clone https://github.com/uddeshya-kumar-1621/Snake_Game.git

# Navigate into the project
cd Snake_Game/Golden\ Response

# Run the game — no pip install needed!
python snake_game.py

Requirements: Python 3.8 or newer. All modules (turtle, time, random) are part of the standard library.


⚡ Performance Decisions
DecisionReasonwn.tracer(0) + manual wn.update()Eliminates screen flicker completelyScore text redraws only on changeAvoids wasting cycles redrawing identical text every frameSegments moved off-screen (not deleted)Object creation in game loops is expensive — reuse is fastertime.sleep(delay) for pacingKeeps CPU usage low; sufficient precision for Turtle games

📄 Documentation Files
FileContentsbackend Game Logic.mdFull breakdown of game rules, state machine, collision logic, scoring, and file I/Ofrontend.mdVisual design decisions, rendering approach, animation, font choices, and screen layoutPROMPT.mdOriginal project brief and requirementsJUSTIFICATION.mdReasoning behind key design and implementation choices

🔮 Possible Extensions

🌀 Wall wrapping mode — exit one side, appear on the other
🧱 Obstacle mode — static blocks appear as score climbs
⚡ Power-ups — temporary speed reduction, double points, invincibility
🏆 Leaderboard — top 10 scores saved with player initials
🎨 Themes — neon, retro pixel art, minimalist
🔊 Sound effects — winsound (Windows) or playsound (cross-platform)


👨‍💻 Author
Uddeshya Kumar
GitHub: @uddeshya-kumar-1621
