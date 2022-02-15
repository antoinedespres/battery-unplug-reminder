import time
import psutil
from win10toast import ToastNotifier

toaster = ToastNotifier()

while True:
    battery = psutil.sensors_battery()
    if battery.percent >= 80 and battery.power_plugged:
        toaster.show_toast("Unplug reminder", "Battery level is ≥ 80 %. It is recommended to unplug your computer.")
    time.sleep(3*60)
