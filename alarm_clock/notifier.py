import winsound
from rich.console import Console
from rich.panel import Panel
from alarm_clock.models import Alarm

console = Console()


def notify(alarm: Alarm) -> None:
    console.print(Panel(
        f"⏰ [bold yellow]ALARM FIRING![/bold yellow]\n\n"
        f"[bold white]Label:[/bold white] {alarm.label}\n"
        f"[bold white]Time:[/bold white]  {alarm.time}",
        title="[red]🔔 Alarm Clock[/red]",
        border_style="red"
    ))
    for _ in range(3):
        winsound.Beep(1000, 500)  # frequency: 1000Hz, duration: 500ms