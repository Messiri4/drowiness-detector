# Drowsiness Detection System

A real-time drowsiness detection system that uses MediaPipe for facial landmark tracking, eye aspect ratio (EAR) for blink detection, and head pose estimation to identify signs of fatigue. If signs of drowsiness are detected—such as frequent blinking or nodding—the system triggers an alarm to alert the user.

---

## 🔍 Features

* 👁️ **Blink Detection** using Eye Aspect Ratio (EAR)
* 🧠 **Head Pose Estimation** to detect nodding
* 🔊 **Alarm System** that activates when drowsiness is detected
* 🧪 **Testing & Fine-tuning** modules for reliable performance
* 🗂️ **Modular File Structure** for easy maintenance and scaling

---

## 📁 Project Structure

```
.
├── alarms/             # Alarm handling logic
├── logs/               # (Reserved) Logging module for future enhancements
├── utils/              # Utility scripts (blink detection, head pose)
├── __pycache__/        # Python bytecode cache
├── .gitignore          # Ignore unnecessary files like venv, __pycache__
├── README.md           # Project documentation
├── config.py           # Configurable constants (thresholds, parameters)
├── main.py             # Main entry point for running the detection system
├── requirements.txt    # Python dependencies
├── test_alarm.py       # Standalone test for the alarm module
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone git@github.com:Messiri4/drowiness-detector.git
cd drowsiness-detector
```

2. Create a virtual environment and activate it:

```bash
python -m venv drowsy-venv
source drowsy-venv/bin/activate   # On Windows: drowsy-venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Ensure you have an `alarm.wav` file placed in the root directory or `alarms/` folder.
2. Run the main detection system:

```bash
python3 main.py
```

3. To test the alarm sound independently:

```bash
python3 test_alarm.py
```

---

## 📦 Dependencies

* `opencv-python`
* `mediapipe`
* `numpy`
* `playsound` *(Consider using `pygame` or `simpleaudio` if issues occur on macOS)*

*All dependencies are listed in `requirements.txt`.*

---

## 🧠 How It Works

* **Face Landmarks** are extracted using MediaPipe.
* **EAR (Eye Aspect Ratio)** is calculated to detect prolonged eye closure.
* **Head Pose Estimation** checks if the user is nodding (indicating drowsiness).
* If either is detected beyond set thresholds, an **alarm is triggered in a separate thread**.

---

## 🛠 Future Improvements

* Add logging for performance metrics and false positives.
* Integrate camera calibration for more accurate head pose.
* Deploy on mobile or Raspberry Pi for in-car usage.

---

## 👤 Author

**Messiri4**
AI Developer & Researcher
[GitHub Profile](https://github.com/Messiri4)

---

## 📜 License

This project is licensed under the MIT License.

