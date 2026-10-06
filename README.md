
#     Ping Pong

A two-player Pong game built with Python and Turtle as part of Angela Yu’s **100 Days of Code** course.

Control the paddles, bounce the ball, and keep the rally going as the game gets faster!

## 🎮 Features

- Local multiplayer on one keyboard
- Keyboard-controlled paddles
- Ball rebounds from paddles and the top and bottom walls
- Ball speeds up after each bounce
- Separate score displays for both players
- Ball returns to the centre and resets its speed after a miss

## 🕹️ Controls

| Player | Move up | Move down |
|---|---|---|
| Left paddle | W | S |
| Right paddle | ↑ | ↓ |

Use the English keyboard layout with Caps Lock off for W and S.

## 🚀 How to Run

You need **Python 3** with **Tkinter/Tk support**. No additional pip packages are required.

1. Download or clone the repository.
2. Make sure all four Python files are in the same folder.
3. Open a terminal in the project folder and run:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

Close the game window or stop the program in your IDE to exit.

## 📂 Project Structure

| File | Purpose |
|---|---|
| `main.py` | Sets up the screen, keyboard controls, game loop, and collision checks |
| `paddle.py` | Defines the paddle appearance and movement |
| `ball.py` | Handles ball movement, bouncing, speed changes, and resets |
| `scoreboard.py` | Tracks and displays the scores |

Use these filenames without download suffixes such as `(1)` so that imports work correctly.

## 🛠️ Technologies

- Python 3
- Turtle
- Time
- Object-oriented programming and inheritance

## 🔧 Current Limitations

- Scoring currently increases the score on the side where the ball exits. In standard Pong, the opposite player should receive the point.
- Paddles can move outside the window.
- Collision detection is approximate.
- Ball speed has no upper limit.
- There is no winning-score limit or restart menu yet.
