from machine import Pin, PWM
from time import sleep
import os  # To read CPU temperature

# Define the GPIO pin connected to the fan
fan_pin = PWM(Pin(18))  # Replace with the correct GPIO pin
fan_pin.freq(1000)  # Set PWM frequency to 1 kHz

# Function to set fan speed (0 to 100%)
def set_fan_speed(speed):
    duty_cycle = int(speed * 1023 / 100)  # Convert percentage to duty cycle (0-1023)
    fan_pin.duty(duty_cycle)

# Function to read CPU temperature (replace with your platform-specific method)
def get_cpu_temperature():
    try:
        # On Linux (like Raspberry Pi), CPU temperature can be read from /sys/class/thermal
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            cpu_temp = int(temp_file.read()) / 1000.0  # Temperature in Celsius
        return cpu_temp
    except Exception as e:
        print(f"Error reading CPU temperature: {e}")
        return None

# Main loop
try:
    while True:
        cpu_temp = get_cpu_temperature()
        if cpu_temp is not None:
            print(f"CPU Temperature: {cpu_temp:.2f}°C")
            
            # Adjust fan speed based on CPU temperature
            if cpu_temp < 40:  # Below 40°C, turn off the fan
                set_fan_speed(0)
            elif cpu_temp < 60:  # 40°C to 60°C, fan at 50% speed
                set_fan_speed(50)
            elif cpu_temp < 80:  # 60°C to 80°C, fan at 75% speed
                set_fan_speed(75)
            else:  # 80°C or higher, fan at 100% speed
                set_fan_speed(100)
        
        sleep(2)  # Check the temperature every 2 seconds

except KeyboardInterrupt:
    print("Program stopped")
    set_fan_speed(0)  # Turn off the fan
    fan_pin.deinit()
