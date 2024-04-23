import psutil
import time
from win11toast import toast
import sys

#Программа для уведомлении о зарядки аккумулятора
#auto-py-to-exe - команда для создания exe
def check_battery():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    if battery.power_plugged and battery.percent > 75:
        result = toast("Заряд батареи: " + percent + "%", "\nОтключить уведомления:",
                       selection=['-', '30 минут', '1 час', 'До следующей перезагрузки ПК'],
                       button='Хорошо')
        try:
            if result["user_input"]["selection"] == "30 минут":
                time.sleep(25 * 60)
            elif result["user_input"]["selection"] == "1 час":
                time.sleep(55 * 60)
            elif result["user_input"]["selection"] == "До следующей перезагрузки ПК":
                sys.exit()
        except Exception as ex: print(ex)


if __name__ == "__main__":
    while True:
        check_battery()
        time.sleep(5 * 60)  # Задержка в 5 минут
