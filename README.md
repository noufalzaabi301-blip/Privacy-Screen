# Privacy Screen

Privacy Screen is a lightweight Windows desktop application that protects content shown on a projector or external monitor.

When privacy mode is enabled, the application moves eligible windows from the external screen to the laptop, remembers their original positions, and covers the external screen with a black always-on-top overlay. When privacy mode is disabled in Extended mode, only the windows moved by Privacy Screen return to their original positions.

If Windows starts in Duplicate mode, Privacy Screen temporarily changes to Extended mode. When privacy mode is disabled, Duplicate mode is restored.

## Requirements

- Windows 10 or Windows 11
- Python 3.11 or newer for source execution

## Run from source

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m privacy_screen
```

## Build locally

```bat
python -m pip install pyinstaller
pyinstaller --noconfirm --clean --onefile --windowed --name PrivacyScreen --collect-submodules privacy_screen main.py
```

The executable is created at `dist\PrivacyScreen.exe`.

## Build with GitHub Actions

Push the project to GitHub, open the **Actions** tab, run **Build Windows EXE**, and download the `PrivacyScreen-Windows` artifact from the completed run.

## Notes

- Some elevated or protected windows may refuse to move because Windows blocks lower-privilege applications from controlling them.
- A newly built unsigned EXE may be blocked by Smart App Control. Run the source for testing or distribute a version signed with a trusted code-signing certificate.
