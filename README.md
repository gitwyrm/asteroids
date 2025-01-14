# Spacerocks - boot.dev guided project

Anything after commit [5653afd2](../../commit/5653afd275dc149f49c2768bd065c235fc35382c) are my own improvements, not from the guided project.

## Screenshots

With sprites

<img src="https://github.com/user-attachments/assets/b77de640-f64a-4ca6-bc7b-a41cd01ee8b0" width=600/>

Retro

<img src="https://github.com/user-attachments/assets/4606f769-a247-42a4-8d83-54d6a9b75753" width=600/>

## Build Instructions

You can build the **Spacerocks** game into a standalone executable for macOS, Windows, or Linux using **PyInstaller**.

### 🔧 How to Build

```bash
# clone this repository
git clone https://github.com/gitwyrm/spacerocks.git
cd spacerocks

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
- macOS: The .app bundle will be in the dist/ folder as spacerocks.app.
- Windows/Linux: The executable will be in the dist/ folder as spacerocks.exe or spacerocks.

## Added after the guided project:

- **GAME OVER screen** with restart and quit buttons
- **PyInstaller support** to package the game as a standalone `.app` or `.exe`
- More realistic ship controls
- **Wrap** player, asteroids and shots at edges
- **No ifinite spawning** asteroids anymore, instead you win if you shoot down all of them
- **Optional images**, change `USE_IMAGES` to `False` in [constants.py](./constants.py) to go back to the simple draw style
- In addition to WASD controls (minus the S since it is not used), arrow keys and right shift can now be used
- Press p to take a screenshot
