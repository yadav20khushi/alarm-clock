# ⏰ Alarm Clock CLI

A command-line alarm clock built in Python for a Senior Software Engineer interview exercise.

---

## Tech Stack
- **Python 3.x**
- **typer** — CLI framework
- **rich** — terminal formatting
- **winsound** — system beep (Windows built-in)
- **dataclasses, json, pathlib, uuid, datetime** — Python standard library

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/yadav20khushi/alarm-clock.git
cd alarm-clock
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Usage

### Add an alarm
```bash
python main.py add "Wake up" "07:00"
```

### List all alarms
```bash
python main.py list-alarms
```

### Delete an alarm
```bash
python main.py delete <alarm-id>
```

### Start the scheduler
```bash
python main.py run
```
> Press `Ctrl+C` to stop the scheduler.

---

## How it works
1. Alarms are stored in `alarms.json` in the project root — no database needed
2. `python main.py run` starts a loop that checks every 30 seconds if any alarm matches the current time
3. When an alarm fires, a styled message prints to the terminal and a system beep plays 3 times

---

## Project Structure
alarm-clock/
├── main.py                  # CLI entry point
├── alarms.json              # Auto-created, stores alarm data
├── requirements.txt
├── README.md
├── DESIGN.md                # Requirements, tradeoffs, system design
└── alarm_clock/
    ├── init.py
    ├── models.py            # Alarm dataclass
    ├── storage.py           # JSON read/write
    ├── scheduler.py         # Live scheduler loop
    └── notifier.py          # Terminal output + beep

---
---

## Design Decisions
See [DESIGN.md](DESIGN.md) for full details on requirements, tradeoffs, and architecture decisions.