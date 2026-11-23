"""Windows display-mode switching helpers."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess


def _display_switch(argument: str) -> None:
    windows = Path(os.environ.get("WINDIR", r"C:\Windows"))
    executable = windows / "System32" / "DisplaySwitch.exe"
    subprocess.Popen(
        [str(executable), argument],
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )


def switch_to_extend() -> None:
    """Request Windows Extended display mode."""
    _display_switch("/extend")


def switch_to_duplicate() -> None:
    """Request Windows Duplicate display mode."""
    _display_switch("/clone")
