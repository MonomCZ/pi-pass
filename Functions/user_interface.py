import Functions.oled_display as oled_display
import Functions.gpio_input as gpio_input
import subprocess

while True:
    oled_display.clear()
    oled_display.display_temperature()
    current_network = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi", "|", "grep", "'^yes'"]).decode().strip()
    oled_display.display_text(current_network, 0)



    oled_display.show()