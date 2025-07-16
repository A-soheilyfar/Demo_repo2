#🔌 اتصالات سخت‌افزاری (Wiring)
#🎯 هدف:
#روشن و خاموش کردن یک LED معمولی با استفاده از پایه GPIO شماره 4.

#🛠 شماتیک اتصال:

#پایه بلند LED (آند +)	مقاومت حدود 220Ω → GPIO4
#پایه کوتاه LED (کاتد -)	GND (زمین برد)


from machine import Pin
import time

led = Pin(4, Pin.OUT)

while True:
    led.value(1)  # روشن
    time.sleep(1)
    led.value(0)  # خاموش
    time.sleep(1)
