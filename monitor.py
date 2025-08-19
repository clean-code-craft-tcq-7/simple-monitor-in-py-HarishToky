
import sys
from time import sleep

def blink_alert(times=6, interval=1):
    """Blinks an alert symbol alternately."""
    for _ in range(times):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(interval)

def vitals_ok(temperature, pulse_rate, spo2):
    if not (95 <= temperature <= 102):
        print('Temperature critical!')
        blink_alert()
        return False

    if not (60 <= pulse_rate <= 100):
        print('Pulse Rate is out of range!')
        blink_alert()
        return False

    if spo2 < 90:
        print('Oxygen Saturation out of range!')
        blink_alert()
        return False

    return True

