
# Kalman Filter Line Tracking Demo

This project demonstrates how to use a **Kalman Filter** with **OpenCV** to track a **broken (dashed) lane line**, similar to road markings used in traffic. It's ideal for robotics, self-driving vehicle simulations, and educational use.

## 🎯 Features

- Tracks vertical dashed lines across frames
- Smooths noisy detections using a Kalman Filter
- Predicts line position when segments are missing
- Visualizes measured vs predicted positions
- Plots prediction error over time

## 🧠 Concepts Demonstrated

- Kalman Filtering in 2D space (`x` and `dx`)
- Object tracking in discontinuous visual input
- Simulated video feed generation using OpenCV
- Visualization with Matplotlib (animation + statistics)

## 📦 Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

Install dependencies using:

```bash
pip install opencv-python numpy matplotlib
```

## 🚀 How to Run

1. Clone this repository or download the ZIP.
2. Run the script:

```bash
python kalman_dashed_line_tracker.py
```

3. View the live tracking animation.
4. See a plot showing the deviation between predicted and actual line positions.

## 📷 Output Preview

- Red dot: Measured line position (when visible)
- Green dot: Kalman filter prediction (used when line is missing)
- Error graph: Deviation between measured and predicted positions

## 📌 Use Cases

- Line following robots (even with occlusion or gaps)
- Lane tracking in autonomous vehicle simulators
- Teaching Kalman filters with intuitive visuals
- Vision-based control systems in robotics

## 🤖 Credits

Created as a demo to illustrate Kalman filtering for line tracking in a noisy or partial-visibility environment.

---

Feel free to fork and adapt this for your own robot or simulation!

