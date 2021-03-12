from pathlib import Path
import os

directory = Path(os.environ["XDG_RUNTIME_DIR"]) / "clipperoni"
dmenu_args = [
    "dmenu",
    "-l",
    "10",
    "-c",
    "-F",
    "-fn",
    "Mononoki Nerd Font:bold:pixelsize=14",
]
