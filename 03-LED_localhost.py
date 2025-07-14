# این پروژه برای کنترل LED به صورت ریموت و با نتورک لوکال هست
# در قسمت اتصال به وای فای مشخصات وای فای خودتون رو وارد کنید


import network
import socket
from machine import Pin, Timer

# تعریف LEDها
led_red = Pin(16, Pin.OUT)
led_green = Pin(17, Pin.OUT)
led_blue = Pin(18, Pin.OUT)

# تایمرها برای هر LED
timer_red = Timer(0)
timer_green = Timer(1)
timer_blue = Timer(2)

# اتصال به وای‌فای
ssid = 'YourSSID'
password = 'YourPassword'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print('Connected. IP:', sta_if.ifconfig()[0])

# تابع ساخت صفحه HTML
def web_page():
    def led_status(led):
        return "ON" if led.value() else "OFF"

    html = f"""
    <!DOCTYPE html>
    <html><head>
    <title>LED Control Panel</title>
    <style>
      html {{ font-family: Arial; text-align: center; }}
      .led-btn {{ padding: 15px; font-size: 18px; margin: 10px; }}
      .on {{ background-color: green; color: white; }}
      .off {{ background-color: red; color: white; }}
    </style></head>
    <body>
    <h2>ESP32 Wi-Fi LED Control (5s Timer)</h2>

    <p>RED LED: <strong>{led_status(led_red)}</strong></p>
    <a href="/red_on"><button class="led-btn on">Red ON (5s)</button></a>
    <a href="/red_off"><button class="led-btn off">Red OFF</button></a>

    <p>GREEN LED: <strong>{led_status(led_green)}</strong></p>
    <a href="/green_on"><button class="led-btn on">Green ON (5s)</button></a>
    <a href="/green_off"><button class="led-btn off">Green OFF</button></a>

    <p>BLUE LED: <strong>{led_status(led_blue)}</strong></p>
    <a href="/blue_on"><button class="led-btn on">Blue ON (5s)</button></a>
    <a href="/blue_off"><button class="led-btn off">Blue OFF</button></a>

    </body></html>
    """
    return html

# وب‌سرور
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Request from', addr)
    request = conn.recv(1024).decode()

    # RED LED
    if '/red_on' in request:
        led_red.on()
        timer_red.init(mode=Timer.ONE_SHOT, period=5000, callback=lambda t: led_red.off())
    if '/red_off' in request:
        led_red.off()
        timer_red.deinit()

    # GREEN LED
    if '/green_on' in request:
        led_green.on()
        timer_green.init(mode=Timer.ONE_SHOT, period=5000, callback=lambda t: led_green.off())
    if '/green_off' in request:
        led_green.off()
        timer_green.deinit()

    # BLUE LED
    if '/blue_on' in request:
        led_blue.on()
        timer_blue.init(mode=Timer.ONE_SHOT, period=5000, callback=lambda t: led_blue.off())
    if '/blue_off' in request:
        led_blue.off()
        timer_blue.deinit()

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
