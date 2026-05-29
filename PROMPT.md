**Snake Game** - Development Prompt

**What is the Role Here?**
You act like a senior Python developer who is  pretty comfortable with the Turtle graphics module.Your task is to create a very basic Snake Game yourself. It should be smooth and slick and even something fun to play, not some basic one that barely works. Consider clean code, structure and something you'd be proud of displaying on your GitHub.
Everything must go smoothly. Should have good start screen, in game, scores, and a game over state (no jank). By the way, high score should persist even after game is closed. When the user closes the window by mistake he/she does not want to lose his/her best score.

**What Are We Building?**
Here is what the finished game needs to do:
Snake moves around the screen smoothly using Turtle graphics. No stuttering, no weird jumps.
The game window should actually look good. Not just a plain screen with a dot moving around. Give it some color, a border, proper fonts.
Scores show up on screen in real time. When you beat your old high score, that updates too.
If the snake hits a wall or runs into itself, the game resets properly. No crashes, no leftover segments floating around.
It gets harder as you play. Every time you eat food, the snake moves a tiny bit faster.
Players can use either WASD or arrow keys. Some people prefer one, some prefer the other.
There should be a start screen before the game begins and a game over screen when you lose, with an option to play again.

**How Should It Look?**
The Game Window
Set the window title to "Snake Game" and make it 600 by 600 pixels. For the background, go with something dark maybe a deep navy (#1a1a2e) or just black. Dark backgrounds make the snake and food colors pop way more than a light one would.

Draw a visible border around the play area using Turtle so the player knows exactly where the boundaries are. Screen update handling is covered in the Visual Polish section below.

**The Snake Itself**
Use a square for the head in the color white or light green – a distinctive color. The segments and limbs should be in a different color (orange is good) than the head (white or light green) so that they are visibly distinguishable. Each segment takes up an area of 20x20 pixels, and the snake moves in a gridlike fashion, making exactly 20 pixels each time. This makes collisions simple and reliable.

**Food**
Whenever the food comes out, change the shape and the colour of the food. Choose between shapes such as square, triangle, and circle or colors such as red, green, yellow, purple or cyan. The place should be random within the play area, but not directly on top of the body of the snake. They can naturally fall on the snake if it should happen, then use the same method as before to calculate their location.

**Score Display**
Write the score in the center of the screen just above the white board. Use the Candara font at 24 size, bold face and format it with a score of 40 and a high score of 120, in white. If the score doesn't actually change, don't redraw the text, you will use cycles for redrawing the same thing each frame!

At the bottom center, insert a small signature line `Coder: Uddeshya in Candara, size 12.`. This remains on-screen throughout.

**Game States**
Before the game starts: Show the title, maybe some brief instructions like "Press SPACE to Start", and the current high score loaded from the save file.

**During gameplay:** Just the snake, food, and score display. Keep it clean.

**When the player loses:** Show "GAME OVER" along with their final score. Give them the option to press SPACE to restart or Q to quit. Wait about a second before showing this so the collision doesn't feel abrupt.

**How Does the Game Actually Work?**
**Movement**
The snake keeps moving in whatever direction it's currently facing. It doesn't stop unless the game resets. Each frame, it moves forward by 20 pixels on the grid.

One important rule: the snake can't do a 180. If you're going up, pressing down shouldn't do anything. This stops the player from accidentally running the head straight into the first body segment. Same logic applies for left/right.

**Controls**
What it does	Key	Also works with
Go up	W	Up arrow
Go down	S	Down arrow
Go left	A	Left arrow
Go right	D	Right arrow
Bind these using wn.onkeypress() and don't forget to call wn.listen() first or none of the keys will register.

**Eating Food**
When the head gets within 20 pixels of the food:

Food teleports to a new random spot
Snake grows by one segment at the tail
Score goes up by 10
The delay between frames drops by 0.001 seconds, making things slightly faster
Food gets a fresh random look (new shape, new color)
Make sure food can't appear outside the play area or directly on the snake. If the random coordinates happen to overlap with a body segment, just roll the dice again.

**How the Body Follows the Head**
This part trips people up sometimes. You need to move segments starting from the tail end going forward. Each segment takes the position of the one in front of it. Then the first segment moves to where the head just was. Do it in this order or you'll get weird visual glitches where segments stack on top of each other.

**Collision Handling**
Hitting a Wall
The play area goes from -290 to +290 on both axes (within the 600px window). If the head's x or y position goes past those limits, that's a wall hit.

**When it happens:**

Freeze for 1 second so the player sees what happened
Move the head back to the center at (0, 0)
Stop all movement
Get rid of every body segment (send them off screen to 1000, 1000 then clear the list)
Zero out the score and reset the speed back to the starting delay of 0.1
Redraw the score display
Running Into Yourself
After the snake moves each frame, loop through all body segments. If any one of them is less than 20 pixels from the head, that's a self-collision. The reset process is identical to hitting a wall.

Watch out for a subtle bug here: segment 0 sits at the head's previous position, so in some implementations it can trigger a false collision right after being placed. Test this carefully.

**Quick Reference**
What happened	When does it trigger	What do we do
Hit a wall	Head goes past ±290 on x or y	Full reset
Hit yourself	Any body segment within 20px of head	Full reset
Ate food	Head within 20px of food	Grow, speed up, add points
Scoring
Every piece of food is worth 10 points. The score display updates right away - no lag, no waiting for the next frame.

The high score tracks the best run in the current session. Whenever the current score passes it, the high score updates.

For keeping the high score between sessions, save it to a file called highscore.txt. Just write the number as plain text. When the game boots up, try to read that file. If it doesn't exist or contains garbage data, just start the high score at 0. Handle all file errors gracefully - details in the Error Handling section.

Making It Harder Over Time
The game starts with a frame delay of 0.1 seconds. Each food eaten shaves off 0.001 seconds. Here's roughly how that plays out:

Your score	Frame delay	How it feels
0 to 50	0.100 down to 0.095	Pretty chill
60 to 150	Around 0.094 to 0.085	Getting quicker
160 to 300	About 0.084 to 0.070	Now it's a challenge
Past 300	Floors at 0.050	Good luck
Put a floor on the delay at 0.050. Below that, things move too fast to be playable for most people and the game loop starts behaving unpredictably.

If you want to go further, you could add selectable modes at the start:

**Easy:** Walls wrap around (go off the right side, appear on the left)
**Normal:** Standard wall collision, this is the default
**Hard:** Everything starts faster and there are obstacles scattered on the field
Visual Polish
No Flickering
Using wn.tracer(0) is non-negotiable. You call wn.update() yourself at the top of each loop iteration. This gives you complete control over when the screen refreshes and eliminates the flickering that happens with Turtle's default auto-update.

**Little Visual Touches**
When the snake eats food, a quick color flash on the head or some kind of brief animation on the new food spawn makes it feel more responsive. On collision, you could flash the border red or briefly change the background color before resetting. These are small things but they make the game feel way more alive.

When you hit a score milestone like 50, 100, or 200 — maybe change the border color or do a brief celebration effect. Nothing over the top, just enough that the player notices.

**Sound (If You Want)**
This is optional since Turtle doesn't have built-in audio. But if you're on Windows, you can use winsound to play quick beeps. Or use the playsound library for cross-platform support.

**When	What sound**
Ate food	Quick beep or chime
Hit a wall	Buzzer or crash sound
Crashed into yourself	Same crash sound
Game starts	Little startup jingle
Hit a milestone score	Achievement-style ding
Don't stress about this too much. It's a nice bonus but the game works perfectly fine without it.

**Code Organization**
Don't cram everything into one file. Break it up like this:


**Snake-Game/**
├── main.py            - starts the game, runs the loop
├── snake.py           - Snake class with head, body, movement, growing, resetting
├── food.py            - Food class that handles spawning and randomizing appearance
├── scoreboard.py      - Scoreboard class for score display, high score, reading/writing the file
├── game.py            - Game class that ties everything together, handles collisions and game states
├── config.py           -all your constants go here: colors, window size, speeds, font settings
├── highscore.txt       - just stores the high score number
└── README.md          - how to set up and run the thing
Classes
**Snake:** Holds the head turtle, list of body segments, current direction. Has methods for moving, turning, growing a new segment, and resetting back to starting state.

**Food:** Wraps a turtle object. Can spawn at random valid positions and randomize its own shape and color each time.

**Scoreboard:** Manages the score turtle/pen, current score, high score. Can read and write the high score file. Updates the display only when needed.

**Game:** The brain of the operation. Creates instances of Snake, Food, and Scoreboard. Runs the main loop, checks collisions every frame, and manages state transitions between start, playing, and game over.

**Code Quality**
Stick to PEP 8 formatting. Add type hints to your functions - it makes the code way easier to follow later. Write docstrings for your classes and any method that isn't immediately obvious. Put all your magic numbers (the 290 boundary, 20px grid size, starting delay, etc.) into config.py as named constants. Apply defensive error handling throughout - see Handling Things That Go Wrong

**Input and Data Handling**
For keyboard input, just ignore any key that isn't mapped to a direction. The opposite-direction blocking can not go left while moving right is the most important validation here.

Rapid key presses can sometimes queue up and cause the snake to effectively reverse direction across two frames. If you notice this happening, you might need to limit direction changes to one per game tick.

For food spawning, keep regenerating coordinates until you find a spot that doesn't overlap with any snake segment. Simple loop with a safety counter so it can't run forever if the snake fills most of the screen (unlikely, but defensive coding is good habit).

For the high score file, keep it dead simple. One number in the file. Read it as an integer, write it as an integer. If the file is missing, corrupted, or has non-numeric content — catch the exception and default to 0.

**What the Finished Game Should Feel Like**
**When someone runs this, they should get:**

A game that starts up without errors and shows a clean start screen
Gameplay that feels responsive with no visible lag or screen tearing
Score and high score updating instantly as they play
A clean reset when they lose (no ghost segments, no score artifacts on screen)
Their high score waiting for them next time they open the game
A smooth exit when they close the window (no exception tracebacks in the terminal)
Handling Things That Go Wrong
The biggest runtime error you will hit is turtle.Terminator - this happens when someone closes the game window while the loop is still running. Wrap your main loop in a try/except to catch this and exit cleanly.

File I/O for the high score can throw FileNotFoundError (first run, file doesn't exist yet) or ValueError (file got corrupted somehow). Handle both cases.

If the delay somehow drops to zero or goes negative (shouldn't happen if you set a floor, but just in case), clamp it to the minimum value.

Making It Run Well
The big performance wins with Turtle are:
Don't create and destroy turtle objects during gameplay. When a segment gets removed, move it way off screen and recycle it later if needed. Object creation in the game loop is expensive.
Only clear and rewrite the score text when the score actually changes. Doing it every single frame is wasteful.
time.sleep(delay) handles pacing. It's not the most precise timing method, but for a Turtle game it works fine and keeps CPU usage low.
The game should run comfortably on pretty much any machine that can run Python. We're not exactly pushing hardware limits here, but bad practices can still make Turtle games feel sluggish.

**Tech Stack**
Everything here is part of Python's standard library, so there's nothing to install:

**Python 3.8 or newer**
**turtle** - all the graphics and window management
**time** - for sleep() to control game speed
**random** - for food position and appearance randomization

**If you want to go beyond the basics:**
**json** - for storing the high score in a structured format instead of plain text
**os** - for reliable file path handling across different operating systems
winsound (Windows only) for sound effects
**Ideas for Later**
Once the core game works well, here are some things you could add down the road:

Wall wrapping mode where the snake goes through walls and comes out the other side
Obstacles that appear on the field as your score gets higher
Special food items that give temporary powers (slow motion, double points, invincibility for a few seconds)
Two player mode on the same keyboard with different key bindings
A leaderboard screen showing top 10 scores with player initials
Different visual themes the player can pick from a menu (neon, retro pixel art, clean minimalist)
Actual levels with pre-designed layouts and increasing difficulty
