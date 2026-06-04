import typer
from rich.console import Console
from rich.table import Table
from alarm_clock.models import Alarm
from alarm_clock.storage import load_alarms, save_alarms
from alarm_clock.scheduler import run_scheduler

app = typer.Typer(help="🕐 Alarm Clock CLI")
console = Console()


@app.command()
def add(
    label: str = typer.Argument(..., help="Label for the alarm e.g. 'Wake up'"),
    time: str = typer.Argument(..., help="Time in HH:MM format e.g. '07:00'")
):
    """Add a new alarm."""
    # Validate time format
    try:
        hour, minute = time.split(":")
        assert 0 <= int(hour) <= 23 and 0 <= int(minute) <= 59
    except:
        console.print("[red]❌ Invalid time format. Use HH:MM e.g. '07:00'[/red]")
        raise typer.Exit()

    alarms = load_alarms()
    alarm = Alarm(label=label, time=time)
    alarms.append(alarm)
    save_alarms(alarms)

    console.print(f"\n[green]✅ Alarm added![/green]")
    console.print(f"   ID:    [bold]{alarm.id}[/bold]")
    console.print(f"   Label: [bold]{alarm.label}[/bold]")
    console.print(f"   Time:  [bold]{alarm.time}[/bold]\n")


@app.command()
def list_alarms():
    """List all alarms."""
    alarms = load_alarms()

    if not alarms:
        console.print("\n[yellow]⚠ No alarms set.[/yellow]\n")
        raise typer.Exit()

    table = Table(title="🕐 Your Alarms", border_style="blue")
    table.add_column("ID",      style="cyan",  no_wrap=True)
    table.add_column("Label",   style="white")
    table.add_column("Time",    style="green")
    table.add_column("Enabled", style="magenta")

    for alarm in alarms:
        table.add_row(
            alarm.id,
            alarm.label,
            alarm.time,
            "✅" if alarm.enabled else "❌"
        )

    console.print(table)


@app.command()
def delete(
    alarm_id: str = typer.Argument(..., help="ID of the alarm to delete")
):
    """Delete an alarm by ID."""
    alarms = load_alarms()
    matched = [a for a in alarms if a.id == alarm_id]

    if not matched:
        console.print(f"\n[red]❌ No alarm found with ID: {alarm_id}[/red]\n")
        raise typer.Exit()

    alarms = [a for a in alarms if a.id != alarm_id]
    save_alarms(alarms)
    console.print(f"\n[green]✅ Alarm '{matched[0].label}' deleted.[/green]\n")


@app.command()
def run():
    """Start the alarm scheduler."""
    run_scheduler()


if __name__ == "__main__":
    app()