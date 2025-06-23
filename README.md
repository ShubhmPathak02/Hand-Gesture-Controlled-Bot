# Hand-Gesture-Controlled-Bot

markdown
Copy
Edit
# 🤖 Gesture Controlled Bot using OpenCV & MediaPipe

![Banner](images/banner.jpg)

A robot controlled entirely using **hand gestures**, powered by **OpenCV** and **MediaPipe**. Show 1 to 5 fingers to move the bot forward, backward, left, right, or stop — no physical remote required!

🏆 **Winner of Roboquest 2.0 - Gesture Tech Challenge**  

---

## ✋ Gesture Controls

| Gesture | Fingers | Action         |
|---------|---------|----------------|
| ☝️       | 1       | Move Forward   |
| ✌️       | 2       | Move Backward  |
| 🤟      | 3       | Turn Left      |
| ✋       | 4       | Turn Right     |
| 🖐️       | 5       | Stop           |

Gestures are detected using a webcam and processed with **MediaPipe Hand Tracking**, then converted into movement commands which are wirelessly interpreted by the ESP8266 microcontroller to control the robot.

---

## ⚙️ Components Used

- 🔌 **ESP8266 NodeMCU**
- ⚡ **L298N Motor Driver**
- 🔋 **Battery Pack (7.4V or 12V)**
- 🧠 **Laptop/PC (Python script + camera)**
- 🎥 **Webcam (internal or USB)**
- 🔧 **DC Motors**
- 🧵 **Jumper Wires**

---

## 🛠️ Tech Stack

- Python 3
- OpenCV
- MediaPipe
- Arduino IDE (for ESP8266 firmware)

---

## 💻 How to Run

### On Your Laptop (Python + Camera)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gesture-controlled-bot.git
cd gesture-controlled-bot
Install dependencies:

bash
Copy
Edit
pip install opencv-python mediapipe
Run the Python script:

bash
Copy
Edit
python main.py
This script opens your webcam, detects the hand gesture using MediaPipe, and sends a command wirelessly to the ESP8266.

