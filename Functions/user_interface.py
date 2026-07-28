import Functions.oled_display as oled_display
import Functions.gpio_input as gpio_input
import subprocess
import time

while True:
    oled_display.clear()
    oled_display.display_temperature()
    current_network = subprocess.check_output(
        ["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]
    ).decode()

    for line in current_network.splitlines():
        if line.startswith("yes:"):
            current_network = line[4:]
            break
    else:
        current_network = "No WiFi"
    oled_display.display_text(current_network, 0)



    oled_display.show()
    time.sleep(1)