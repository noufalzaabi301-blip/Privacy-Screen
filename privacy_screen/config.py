"""Local configuration storage for Privacy Screen."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """User-editable application settings."""

    hotkey: str = "F8"
    monitor: str = "AUTO"


class ConfigStore:
    """Load and save settings in the user's local application-data folder."""

    def __init__(self) -> None:
        appdata = os.getenv("LOCALAPPDATA")
        base = Path(appdata) if appdata else Path.home() / "AppData" / "Local"
        self.path = base / "PrivacyScreen" / "config.json"

    def load(self) -> AppConfig:
        if not self.path.exists():
            return AppConfig()

        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return AppConfig(
                hotkey=str(data.get("hotkey", "F8")),
                monitor=str(data.get("monitor", "AUTO")),
            )
        except (OSError, ValueError, TypeError):
            return AppConfig()

    def save(self, config: AppConfig) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(asdict(config), indent=2),
            encoding="utf-8",
        )
        temporary.replace(self.path)
