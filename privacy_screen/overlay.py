"""Always-on-top black overlays for external monitors."""

from __future__ import annotations

import tkinter as tk

from .models import Monitor


class OverlayController:
    """Create and remove black full-screen windows."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.windows: list[tk.Toplevel] = []

    def show(self, monitors: list[Monitor]) -> None:
        self.hide()
        for monitor in monitors:
            window = tk.Toplevel(self.root)
            window.configure(background="black", cursor="none")
            window.overrideredirect(True)
            window.attributes("-topmost", True)
            geometry = (
                f"{monitor.width}x{monitor.height}"
                f"{monitor.left:+d}{monitor.top:+d}"
            )
            window.geometry(geometry)
            window.update_idletasks()
            window.lift()
            window.attributes("-topmost", True)
            window.focus_set()
            self.windows.append(window)

    def hide(self) -> None:
        for window in self.windows:
            try:
                window.destroy()
            except tk.TclError:
                pass
        self.windows.clear()
