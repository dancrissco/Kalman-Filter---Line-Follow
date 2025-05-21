
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_dashed_line_sequence(num_frames=30, width=640, height=480):
    frames = []
    for i in range(num_frames):
        img = np.zeros((height, width), dtype=np.uint8)
        for j in range(0, height, 60):
            if ((j // 60) + i // 5) % 2 == 0:
                x = width // 2 + (i - num_frames // 2) * 5
                cv2.line(img, (x, j), (x, j + 30), 255, 2)
        frames.append(img)
    return frames

def create_kalman_filter():
    kf = cv2.KalmanFilter(2, 1)
    kf.transitionMatrix = np.array([[1, 1],
                                     [0, 1]], np.float32)
    kf.measurementMatrix = np.array([[1, 0]], np.float32)
    kf.processNoiseCov = np.eye(2, dtype=np.float32) * 0.03
    kf.measurementNoiseCov = np.array([[1]], np.float32) * 1
    kf.statePre = np.array([[320], [0]], dtype=np.float32)
    return kf

def simulate_kalman_tracking(frames):
    kf = create_kalman_filter()
    predictions = []
    measurements = []

    for frame in frames:
        contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        centroid_x = None
        if contours:
            largest = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest)
            if M['m00'] != 0:
                centroid_x = int(M['m10'] / M['m00'])

        predicted = kf.predict()
        if centroid_x is not None:
            corrected = kf.correct(np.array([[np.float32(centroid_x)]]))
            predictions.append(corrected[0, 0])
            measurements.append(centroid_x)
        else:
            predictions.append(predicted[0, 0])
            measurements.append(None)

    return predictions, measurements, frames

def run_simulation(predictions, measurements, frames_used):
    fig, ax = plt.subplots()
    img_plot = ax.imshow(frames_used[0], cmap='gray')
    line_measured, = ax.plot([], [], 'ro', label='Measured')
    line_predicted, = ax.plot([], [], 'go', label='Predicted')
    ax.set_title("Kalman Filter Tracking of Broken Lane Line")
    ax.legend()

    def update(frame_idx):
        frame = frames_used[frame_idx].copy()
        img_plot.set_array(frame)

        y = frame.shape[0] - 30
        measured_x = measurements[frame_idx]
        predicted_x = predictions[frame_idx]

        line_measured.set_data([measured_x] if measured_x is not None else [], [y] if measured_x is not None else [])
        line_predicted.set_data([predicted_x], [y])
        return img_plot, line_measured, line_predicted

    ani = animation.FuncAnimation(fig, update, frames=len(frames_used), interval=200, blit=True)
    plt.show()

def show_statistics(predictions, measurements):
    errors = []
    frame_indices = []

    for i, (meas, pred) in enumerate(zip(measurements, predictions)):
        if meas is not None:
            error = abs(meas - pred)
            errors.append(error)
            frame_indices.append(i)

    plt.figure(figsize=(10, 4))
    plt.plot(frame_indices, errors, label="Prediction Error", color="blue", marker='o')
    plt.title("Kalman Filter Prediction Error Over Time")
    plt.xlabel("Frame")
    plt.ylabel("Deviation (pixels)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    frames = generate_dashed_line_sequence()
    predictions, measurements, frames_used = simulate_kalman_tracking(frames)
    run_simulation(predictions, measurements, frames_used)
    show_statistics(predictions, measurements)
