# 💡 ESP32 Wi-Fi LED Control

This is a simple MicroPython project for controlling an LED connected to an ESP32 board using a web browser via Wi-Fi.

## 📱 Features

- Connects to your Wi-Fi network
- Hosts a web server on the ESP32
- Lets you turn an LED ON or OFF via a simple HTML interface
- Shows real-time LED status
- Uses GPIO2 by default for the LED pin

## 🔧 Hardware Requirements

- ESP32 board
- 1x LED
- 1x Resistor (1kΩ is a good choice)
- Breadboard and jumper wires
- MicroUSB cable

## ⚙️ Wiring

ESP32 GPIO2 ---> Resistor ---> Anode of LED
Cathode of LED ---> GND

## 🧠 How it works

1. ESP32 connects to your Wi-Fi network.
2. It creates a basic HTTP web server.
3. When accessed in a browser, the server displays buttons to turn the LED ON or OFF.
4. Clicking the buttons sends requests (`/on` or `/off`) that toggle the LED accordingly.

## 🛠️ Setup

1. Install [MicroPython firmware](https://micropython.org/download/esp32/) on your ESP32.
2. Use tools like [Thonny](https://thonny.org/) or `ampy` to upload the Python script to the ESP32.
3. Change the `ssid` and `password` in the script to match your own Wi-Fi.
4. Run the script, and visit the IP address shown in the console from your browser.

## 🌐 Example Web Interface

```html
<h2>Control LED with ESP32</h2>
<p>LED STATUS: <strong>ON</strong></p>
[Turn OFF] [Turn ON]
```
