from machine import Pin, PWM
from time import sleep

# Define RGB LED pins
RED_PIN = 0
GREEN_PIN = 1
BLUE_PIN = 2

# Set up PWM for each color
red = PWM(Pin(RED_PIN))
green = PWM(Pin(GREEN_PIN))
blue = PWM(Pin(BLUE_PIN))

# Set PWM frequency
FREQ = 1000
red.freq(FREQ)
green.freq(FREQ)
blue.freq(FREQ)

# Function to set RGB color
def set_color(r, g, b):
    # Convert 0-255 range to 0-65535 range for PWM duty
    red.duty_u16(int((r / 255) * 65535))
    green.duty_u16(int((g / 255) * 65535))
    blue.duty_u16(int((b / 255) * 65535))

# Example: Cycle through some colors
try:
    while True:
        set_color(255, 0, 0)  # Red
        sleep(1)
        set_color(0, 255, 0)  # Green
        sleep(1)
        set_color(0, 0, 255)  # Blue
        sleep(1)
        set_color(255, 255, 0)  # Yellow
        sleep(1)
        set_color(0, 255, 255)  # Cyan
        sleep(1)
        set_color(255, 0, 255)  # Magenta
        sleep(1)
        set_color(255, 255, 255)  # White
        sleep(1)
except KeyboardInterrupt:
    # Clean up
    red.deinit()
    green.deinit()
    blue.deinit()
