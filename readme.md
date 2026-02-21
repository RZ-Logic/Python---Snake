# Python Arcade: Snake 🐍

A polished, fully functional clone of the classic arcade game Snake, built in Python using the Pygame library. 

## Features
* **Custom Graphics:** Styled snake segments with distinct head/body graphics and an apple-style food sprite.
* **Game State Management:** Features a smooth "Game Over" screen with a translucent overlay.
* **Continuous Play:** Built-in loop allowing the player to hit `R` to instantly restart or `Q` to quit upon death without crashing the terminal.
* **Score Tracking:** Real-time score updates displayed directly on the game window.

## Prerequisites
* Python 3.x
* Pygame library

## Installation & Setup

Because this game uses third-party libraries, you will need to install the dependencies before running it.

**1. Clone the repository and navigate to the folder:**
```bash
git clone https://github.com/rizwanahmed109-beep/Python---Snake.git
cd Python---Snake
```

**2. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

## How to Run

### Windows
```cmd
python snake_.py
```

### macOS and Linux
```bash
python3 snake_.py
```

## Controls
* **Arrow Keys:** Move the snake (Up, Down, Left, Right)
* **R:** Restart the game (on Game Over screen)
* **Q:** Quit the game (on Game Over screen)

## Troubleshooting

### Pygame Installation Error (Python 3.14+)
If you are using a very recent version of Python (like 3.14+) and encounter a massive red error when running `pip install -r requirements.txt` (specifically failing to build the "wheel" or missing `distutils`), this is because standard `pygame` may not have pre-built release files for your specific Python version yet.

**Solutions:**
1. **Use Anaconda (Recommended):** Run the installation and game through an Anaconda environment terminal. Anaconda environments typically default to highly stable Python versions (like 3.11 or 3.12) where `pygame` installs seamlessly.
2. **Use Pygame Community Edition:** Change the dependency in the `requirements.txt` from `pygame` to `pygame-ce` (Pygame Community Edition), which is a modernized fork optimized for newer Python versions, and run the install command again.
3. **Downgrade Python:** Run the script using Python 3.12 or 3.11.