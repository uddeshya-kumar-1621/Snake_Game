**📌 Project Overview**

This is a fully-featured Snake Game built using Python's turtle module no external dependencies required. The project was developed as a complete software solution with a clear separation between frontend (visuals) and backend (game logic), demonstrating clean code structure, OOP principles, and thoughtful UX design.
The game features a proper start screen, live in-game HUD, game over state, and a high score that persists between sessions so the player never loses their best run.

---

**🗂️ Repository Structure**

```
Snake-Game/
│
├── Golden Response/
│   ├── snake_game.py          # Complete game implementation
│   ├── backend Game Logic.md  # Backend logic documentation
│   └── frontend.md            # Frontend/UI documentation
│
├── PROMPT.md                  # Project brief and requirements
├── JUSTIFICATION.md           # Design decisions and justifications
└── README.md                  # This file
```

---

**✨ Features**

| Feature                     | Details                                                          |
|-----------------------------|------------------------------------------------------------------|
| 🎮 Smooth Movement          | Grid-based 20px steps, no stuttering or visual glitches          |
| 🖥️ Styled Window            | Dark background (#1a1a2e), visible play border, 600×600px        |
| 🐍 Distinct Snake           | White/light-green head, orange body segments                     |
| 🍎 Dynamic Food             | Random shape (square, circle, triangle) + random color each spawn|
| 📊 Live Score HUD           | Candara 24pt bold — only redraws when score changes              |
| 💾 Persistent High Score    | Saved to highscore.txt, survives between sessions                |
| 🚀 Progressive Speed        | Starts at 0.1s delay, -0.001s per food, floored at 0.05s         |
| 🔄 Full Game States         | Start screen → Gameplay → Game Over → Restart                    |
| ⌨️ Dual Controls            | WASD + Arrow keys both supported                                 |
| 🧱 Visible Border           | Drawn with Turtle so player knows exact play boundaries          |
| ✍️ Signature                | Coder: Uddeshya shown on screen throughout                       |

---

**🏗️ Architecture**

This project is designed with a clear separation of concerns:

**Backend (Game Logic)**
Handles all the rules, state, and data of the game:

- Snake movement, direction control, and 180° reversal prevention
- Collision detection — wall hits (±290 boundary) and self-collision (< 20px)
- Food spawning — random position, never overlapping the snake body
- Score tracking and high score persistence (highscore.txt)
- Game state machine — START → PLAYING → GAME_OVER → RESTART
- Speed progression — delay decreases with each food eaten

**Frontend (UI / Visuals)**
Handles everything the player sees:

- Dark-themed game window with wn.tracer(0) + manual wn.update() to eliminate flicker
- Snake rendering — head vs body color distinction
- Score display using pen.write() — redraws only on change (performance-conscious)
- Food visual — randomized shape and color on every spawn
- Start screen with title, instructions, and loaded high score
- Game over screen with final score and replay options
- Bottom signature line — always visible

---

**🎮 Controls**

| Action          | Key    | Alternative    |
|-----------------|--------|----------------|
| Move Up         | W      | ↑ Up Arrow     |
| Move Down       | S      | ↓ Down Arrow   |
| Move Left       | A      | ← Left Arrow   |
| Move Right      | D      | → Right Arrow  |
| Start / Restart | SPACE  | —              |
| Quit            | Q      | Close window   |

> **Note:** 180° reversal is blocked — pressing the opposite direction has no effect, preventing instant self-collision.

---

**🕹️ Game States**

```
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
```

---

**📈 Difficulty Progression**

| Score Range | Frame Delay        | Feel             |
|-------------|--------------------|------------------|
| 0 – 50      | 0.100s → 0.095s    | Relaxed          |
| 60 – 150    | 0.094s → 0.085s    | Getting faster   |
| 160 – 300   | 0.084s → 0.070s    | Challenging      |
| 300+        | Floored at 0.050s  | Expert level     |

---

**🔧 Collision Logic**

**Wall Collision** — triggered when head exceeds ±290 on x or y axis:
- Freeze for 1 second (player sees what happened)
- Head returns to (0, 0)
- All body segments sent off-screen to (1000, 1000) and cleared
- Score resets to 0, delay resets to 0.1
- Score display redraws

**Self Collision** — triggered when any segment is < 20px from head:
- Same full reset process as wall collision

**Food Collision** — triggered when head is < 20px from food:
- Food teleports to new random position (guaranteed not on snake body)
- New segment added at tail
- Score +10, delay -0.001
- Food gets new random shape and color

---

**💾 High Score Persistence**

```python
# On startup — read from file
try:
    with open("highscore.txt", "r") as f:
        high_score = int(f.read())
except (FileNotFoundError, ValueError):
    high_score = 0

# On new high score — write to file
with open("highscore.txt", "w") as f:
    f.write(str(high_score))
```

- File missing (first run) → starts at 0 gracefully ✅
- File corrupted → catches ValueError, defaults to 0 ✅
- Game closed mid-session → score already written on beat ✅

---

**🐛 Error Handling**

| Scenario                  | Handling                                                          |
|---------------------------|-------------------------------------------------------------------|
| Window closed mid-game    | turtle.Terminator caught → clean exit, no traceback              |
| highscore.txt missing     | FileNotFoundError → defaults to 0                                |
| Corrupted score file      | ValueError → defaults to 0                                       |
| Speed underflow           | Delay floored at 0.050 — always playable                         |
| Food spawns on snake      | Loop regenerates coordinates until clear position found          |

---

**🚀 How to Run**

```bash
# Clone the repository
git clone https://github.com/uddeshya-kumar-1621/Snake_Game.git

# Navigate into the project
cd Snake_Game/Golden\ Response

# Run the game — no pip install needed!
python snake_game.py
```

**Requirements:** Python 3.8 or newer. All modules (turtle, time, random) are part of the standard library.

---

**⚡ Performance Decisions**

| Decision                              | Reason                                                               |
|---------------------------------------|----------------------------------------------------------------------|
| wn.tracer(0) + manual wn.update()     | Eliminates screen flicker completely                                 |
| Score text redraws only on change     | Avoids wasting cycles redrawing identical text every frame           |
| Segments moved off-screen (not deleted) | Object creation in game loops is expensive — reuse is faster       |
| time.sleep(delay) for pacing          | Keeps CPU usage low; sufficient precision for Turtle games           |

---

**📄 Documentation Files**

| File                    | Contents                                                                                          |
|-------------------------|---------------------------------------------------------------------------------------------------|
| backend Game Logic.md   | Full breakdown of game rules, state machine, collision logic, scoring, and file I/O              |
| frontend.md             | Visual design decisions, rendering approach, animation, font choices, and screen layout           |
| PROMPT.md               | Original project brief and requirements                                                           |
| JUSTIFICATION.md        | Reasoning behind key design and implementation choices                                            |

---

**🔮 Possible Extensions**

- 🌀 **Wall wrapping mode** — exit one side, appear on the other
- 🧱 **Obstacle mode** — static blocks appear as score climbs
- ⚡ **Power-ups** — temporary speed reduction, double points, invincibility
- 🏆 **Leaderboard** — top 10 scores saved with player initials
- 🎨 **Themes** — neon, retro pixel art, minimalist
- 🔊 **Sound effects** — winsound (Windows) or playsound (cross-platform)

---

**👨‍💻 Author**

Uddeshya Kumar
GitHub: [@uddeshya-kumar-1621](https://github.com/uddeshya-kumar-1621)
