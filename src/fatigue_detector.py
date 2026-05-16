import cv2
import time
import math

class DriverFatigueAlertSystem:
    def __init__(self, ear_threshold=0.25, consec_frames_limit=3):
        self.EAR_THRESHOLD = ear_threshold  # Threshold below which eyes are considered closed
        self.CONSEC_FRAMES_LIMIT = consec_frames_limit  # Number of seconds/frames before triggering alert
        self.eye_closed_start_time = None
        self.alarm_active = False

    def trigger_in_cabin_alarm(self):
        self.alarm_active = True
        print("[HARDWARE ALERT] !!! WAKE UP AUDIO ALARM ACTIVATED !!!")

    def clear_alarm(self):
        self.alarm_active = False
        print("[SYSTEM] Driver alert state restored to normal.")

    def process_dsm_stream(self):
        # Initialize In-Cabin DSM Infrared Camera
        video_capture = cv2.VideoCapture(0)
        print("[SYSTEM] Monitoring driver fatigue levels via Edge AI...")

        # Simulated loop reading camera frames
        for frame_idx in range(10):
            time.sleep(0.5)  # Simulate frame processing intervals
            
            # Simulated Eye Aspect Ratio (EAR). 
            # In real deployment, this is calculated using facial landmarks: (p2+p6)/(2*p1)
            simulated_ear = 0.30 if frame_idx < 4 else 0.20  # Driver starts closing eyes at frame 4
            print(f"[FRAME {frame_idx}] Current Eye Aspect Ratio (EAR): {simulated_ear:.2f}")

            if simulated_ear < self.EAR_THRESHOLD:
                if self.eye_closed_start_time is None:
                    self.eye_closed_start_time = time.time()
                
                duration = time.time() - self.eye_closed_start_time
                if duration >= self.CONSEC_FRAMES_LIMIT and not self.alarm_active:
                    print(f"[ALERT] Eyes closed for {duration:.1f}s. Fatigue detected!")
                    self.trigger_in_cabin_alarm()
            else:
                if self.eye_closed_start_time is None:
                     if self.alarm_active:
                         self.clear_alarm()
                self.eye_closed_start_time = None

        video_capture.release()

if __name__ == "__main__":
    detector = DriverFatigueAlertSystem(ear_threshold=0.25, consec_frames_limit=1.5)
    detector.process_dsm_stream()
