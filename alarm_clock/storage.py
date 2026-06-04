import json
from pathlib import Path
from alarm_clock.models import Alarm

ALARMS_FILE = Path("alarms.json")


def load_alarms() -> list[Alarm]:
    if not ALARMS_FILE.exists():
        return []
    with open(ALARMS_FILE, "r") as f:
        data = json.load(f)
    return [Alarm.from_dict(item) for item in data]


def save_alarms(alarms: list[Alarm]) -> None:
    with open(ALARMS_FILE, "w") as f:
        json.dump([alarm.to_dict() for alarm in alarms], f, indent=2)