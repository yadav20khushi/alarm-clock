# Alarm Clock CLI — Design Document

## Overview
A command-line alarm clock built in Python. Users can set, view, and delete alarms
from the terminal. A separate `run` command starts a live scheduler that watches the
clock and fires alarms when the time matches.

---

## Requirements Decisions

### What counts as a complete alarm?
An alarm has:
- A unique ID (auto-generated)
- A label (e.g. "Wake up", "Take medicine")
- A time in HH:MM format (24-hour)
- An enabled flag (True/False)

### Does it persist across sessions?
Yes. Alarms are saved to a local `alarms.json` file in the project root.
If you close the terminal and reopen it, your alarms are still there.

### How does the scheduler work?
`python main.py run` starts an infinite loop that checks every 30 seconds
whether any alarm matches the current HH:MM time. When matched, it fires
a notification and marks the alarm as fired for that minute to avoid double-firing.

### What happens when an alarm fires?
1. A message is printed to the terminal with the alarm label and time
2. A system beep is played using `winsound` (Windows built-in, no install needed)

### Does it support recurring alarms?
No. Out of scope for this exercise. Each alarm fires once per `run` session.
This is a deliberate tradeoff to keep the scope tight and the code clean.

### Does it support snooze?
No. Out of scope. Would require interactive input during the scheduler loop,
adding significant complexity for little gain in a 30-minute build.

---

## Tradeoffs

| Decision | Chosen | Rejected | Reason |
|---|---|---|---|
| CLI library | `typer` | `argparse` | Typer is cleaner, auto-generates help output |
| Output formatting | `rich` | plain `print()` | Rich makes tables and colors trivial |
| Persistence | JSON file | SQLite / no persistence | No DB per spec; JSON is readable and zero setup |
| File paths | `pathlib` | hardcoded strings | pathlib works cross-platform |
| Notification | `winsound` | `plyer`, `playsound` | winsound is Windows built-in, zero install |
| Recurrence | None | daily / weekday repeat | Out of scope, adds complexity |
| Snooze | None | 5/10 min snooze | Out of scope, needs interactive loop input |

---

## System Flow
User runs a command
↓
main.py receives it (CLI layer via typer)
↓
Two paths:
[add / list / delete]          [run]
↓                        ↓
models.py                 scheduler.py
(create Alarm object)     (infinite loop, checks time every 30s)
↓                        ↓
storage.py                storage.py
(save/read JSON)          (load alarms from JSON)
↓
notifier.py
(terminal message + system beep)
---
## File Structure

alarm-clock/
├── main.py                  # CLI entry point, defines all commands
├── alarms.json              # Auto-created at runtime, stores alarm data
├── requirements.txt         # typer, rich
├── README.md                # Setup and usage instructions
├── DESIGN.md                # This file
└── alarm_clock/
    ├── __init__.py          # Makes alarm_clock a Python package
    ├── models.py            # Alarm dataclass definition
    ├── storage.py           # Load and save alarms to JSON
    ├── scheduler.py         # Live loop that checks and fires alarms
    └── notifier.py          # Handles terminal output and beep on alarm fire

---
## What is explicitly out of scope
- No recurring alarms
- No snooze
- No database
- No web UI
- No cross-platform audio (Windows only via winsound)
- No authentication or multi-user support

---

## AI Usage
This project was built with AI assistance (Claude) for:
- Refining requirements and making tradeoff decisions
- Designing the system architecture and file structure
- Generating implementation plan before writing code

All code was reviewed and understood before being committed.