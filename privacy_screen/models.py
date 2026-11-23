"""Data models used by Privacy Screen."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Monitor:
    """A physical or virtual monitor reported by Windows."""

    device_name: str
    left: int
    top: int
    right: int
    bottom: int
    primary: bool = False

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top

    @property
    def label(self) -> str:
        primary = " (Primary)" if self.primary else ""
        return f"{self.device_name}{primary} — {self.width}×{self.height}"


@dataclass(frozen=True)
class SavedWindowPlacement:
    """The original placement of a window moved by Privacy Screen."""

    hwnd: int
    left: int
    top: int
    right: int
    bottom: int
    was_minimized: bool = False
    was_maximized: bool = False

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top
