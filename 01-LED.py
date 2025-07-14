from machine import Pin
import time

# پایه D4 معمولاً GPIO 4 هست
led = Pin(4, Pin.OUT)  # تنظیم پایه به عنوان خروجی

led.value(1)  # روشن کردن LED (HIGH)
