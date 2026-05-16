```mermaid
#AI-Powered Driver Fatigue & Drowsiness Detection Module

This repository contains an Edge AI software module designed for Driver Status Monitoring (DSM) systems. It detects commercial driver fatigue, micro-sleep, and prolonged eye closure in real-time to mitigate risks associated with drowsy driving in heavy-duty fleets.

## Technical Methodology
The module monitors the **Eye Aspect Ratio (EAR)** using real-time facial landmark localization. The mathematical model calculates the distance between vertical eye landmarks divided by horizontal landmarks. 

When the driver's eyes remain closed beyond a safety-critical temporal threshold (e.g., >1.5 seconds), the system identifies a micro-sleep event.

## System Workflow & Logic
```mermaid
graph TD
    A[Start DSM Camera Stream] --> B[Detect Driver Facial Landmarks]
    B --> C[Calculate Eye Aspect Ratio - EAR]
    C --> D{EAR < Threshold?}
    D -->|No / Eyes Open| E[Reset Fatigue Timer]
    E --> A
    D -->|Yes / Eyes Closed| F[Start Temporal Counter]
    F --> G{Duration >= 1.5 Seconds?}
    G -->|No| A
    G -->|Yes| H[Trigger Loud In-Cabin Audio Buzzer]
    H --> I[Transmit Critical Safety Event to Fleet Dispatch via Cloud IoT]
