from machine import ADC, Pin, PWM
import time

# Setup
TEMP_SENSOR_PIN = 26  # GP26 (ADC0)
FAN_PWM_PIN = 15      # GP15 (PWM output)
FAN_FREQ = 25000      # 25kHz is typical for fans

adc = ADC(TEMP_SENSOR_PIN)
fan_pwm = PWM(Pin(FAN_PWM_PIN))
fan_pwm.freq(FAN_FREQ)

def read_temp_c():
    # Read ADC (0-65535), convert to voltage (0-3.3V)
    reading = adc.read_u16()
    voltage = reading * 3.3 / 65535
    # TMP36: 0.5V at 0°C, 10mV/°C
    temp_c = (voltage - 0.5) * 100
    return temp_c

def set_fan_speed(temp_c):
    # Set fan speed based on temperature
    # Below 30°C: off, 30-60°C: linear, above 60°C: full speed
    if temp_c < 30:
        duty = 0
    elif temp_c > 60:
        duty = 65535
    else:
        duty = int((temp_c - 30) / 30 * 65535)
    fan_pwm.duty_u16(duty)

while True:
    temp = read_temp_c()
    set_fan_speed(temp)
    print("Temp: {:.1f}°C".format(temp))
    time.sleep(1)
