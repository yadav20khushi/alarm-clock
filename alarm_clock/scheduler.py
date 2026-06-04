import time
from datetime import datetime
from alarm_clock.storage import load_alarms
from alarm_clock.notifier import notify

def run_scheduler() -> None:
    print("⏰ Alarm scheduler started. Press Ctrl+C to stop.\n")

    fired_this_minute = set()
    last_minute = None

    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")

            # Reset fired set every new minute
            if current_time != last_minute:
                fired_this_minute = set()
                last_minute = current_time

            # Load fresh from disk every cycle (in case alarms were added)
            alarms = load_alarms()

            for alarm in alarms:
                if (
                    alarm.enabled
                    and alarm.time == current_time
                    and alarm.id not in fired_this_minute
                ):
                    notify(alarm)
                    fired_this_minute.add(alarm.id)

            time.sleep(30)

    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped.")