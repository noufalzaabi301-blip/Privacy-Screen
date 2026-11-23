"""Notification-area icon for Privacy Screen."""

from __future__ import annotations

from threading import Thread
from typing import Callable

from PIL import Image, ImageDraw
import pystray


def _create_icon() -> Image.Image:
    image = Image.new("RGBA", (64, 64), (18, 18, 18, 255))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((8, 12, 56, 48), radius=5, outline="white", width=4)
    draw.rectangle((27, 49, 37, 55), fill="white")
    draw.rectangle((20, 55, 44, 59), fill="white")
    draw.line((15, 19, 49, 41), fill=(70, 160, 255, 255), width=5)
    return image


class TrayController:
    """Run the system-tray menu on its own thread."""

    def __init__(
        self,
        on_toggle: Callable[[], None],
        on_settings: Callable[[], None],
        on_exit: Callable[[], None],
    ) -> None:
        menu = pystray.Menu(
            pystray.MenuItem("Toggle privacy mode", lambda _icon, _item: on_toggle(), default=True),
            pystray.MenuItem("Settings", lambda _icon, _item: on_settings()),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Exit", lambda _icon, _item: on_exit()),
        )
        self.icon = pystray.Icon("PrivacyScreen", _create_icon(), "Privacy Screen", menu)
        self.thread: Thread | None = None

    def start(self) -> None:
        self.thread = Thread(target=self.icon.run, name="PrivacyScreenTray", daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.icon.stop()
        if self.thread is not None:
            self.thread.join(timeout=2)
