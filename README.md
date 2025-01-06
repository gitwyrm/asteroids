# asteroids - boot.dev guided project

Anything after commit [5653afd2](../../commit/5653afd275dc149f49c2768bd065c235fc35382c) are my own improvements, not from the guided project.

## Build Instructions

You can build the **Asteroids** game into a standalone executable for macOS, Windows, or Linux using **PyInstaller**.

### 🔧 How to Build

```bash
# clone this repository
git clone https://github.com/gitwyrm/asteroids.git
cd asteroids

# create a venv
python3 -m venv venv

# if you're on macOS/Linux
source venv/bin/activate

# or on Windows
venv\Scripts\activate

# install dependencies with pip
pip install -r requirements.txt

# run PyInstaller with the provided spec
pyinstaller main.spec

# or run the game directly without PyInstaller
python3 main.py
```

### 📦 Output
- macOS: The .app bundle will be in the dist/ folder as asteroids.app.
- Windows/Linux: The executable will be in the dist/ folder as asteroids.exe or asteroids.

## Added after the guided project:

- **GAME OVER screen** with restart and quit buttons
- **PyInstaller support** to package the game as a standalone `.app` or `.exe`
- More realistic ship controls
- **Wrap** player, asteroids and shots at edges
- **No ifinite spawning** asteroids anymore, instead you win if you shoot down all of them
- **Optional images**, change `USE_IMAGES` to `False` in [constants.py](./constants.py) to go back to the simple draw style