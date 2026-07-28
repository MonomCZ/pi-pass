import Functions.oled_display as oled_display
import Functions.gpio_input as gpio_input
import time
while True:
    oled_display.clear()
    if gpio_input.button1():
        oled_display.display_text("Button 1 pressed", 0)
    oled_display.display_temperature()
    oled_display.show()
    time.sleep(1)