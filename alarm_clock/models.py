import uuid
from dataclasses import dataclass, field


@dataclass
class Alarm:
    label: str
    time: str  # format: "HH:MM"
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    enabled: bool = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "label": self.label,
            "time": self.time,
            "enabled": self.enabled
        }

    @staticmethod
    def from_dict(data: dict) -> "Alarm":
        return Alarm(
            id=data["id"],
            label=data["label"],
            time=data["time"],
            enabled=data["enabled"]
        )