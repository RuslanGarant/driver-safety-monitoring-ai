# Garant-Fleet DSM: Edge AI Driver Monitoring & Fatigue Detection Engine
### Part of the "Garant-Fleet AI" Integrated Intelligent Analytics Ecosystem

![Garant-Fleet AI Banner](https://raw.githubusercontent.com/RuslanGarant/vehicle-faceid-immobilizer/main/assets/banner.png) *(Placeholder for Ecosystem Banner)*

## Platform Overview
**Garant-Fleet DSM** is a high-performance, real-time computer vision monitoring system engineered for commercial transport infrastructure and enterprise fleets. Acting as a core intelligence node within the **Garant-Fleet AI** ecosystem developed by a single founder, this platform executes local, low-latency edge inference to mitigate heavy vehicle accident risks by instantly identifying driver drowsiness, micro-sleep events, and cognitive fatigue patterns.

---

## Technical Positioning & Neural Pipeline
Standard safety scripts rely on cloud computing and heavy processing. Garant-Fleet DSM is deployed as an independent **AI Engine**, operating entirely offline on embedded ARM-based mobile digital video recorders (MDVR) to eliminate data transfer latencies.

### Mathematical Framework & AI Data Pipeline
The engine executes facial landmark localization to dynamically compute the **Eye Aspect Ratio (EAR)** using spatial vector geometry:

```mermaid
graph LR
    A[NIR Camera Stream] --> B[Face Mesh Tracking Node]
    B --> C[Facial Landmark Extraction]
    C --> D[EAR Coordinate Calculation]
    D --> E{EAR < Fatigue Threshold?}
    E -->|No / Normal Blink| F[Reset Temporal Counter]
    E -->|Yes / Eyes Closed| G[Initiate Consecutive Frame Counter]
    G --> H{Duration >= 1.5 Seconds?}
    H -->|No| A
    H -->|Yes / Micro-Sleep| I[Trigger In-Cabin Audio Intervention]
    I --> J[Package Cryptographic Metadata Event]
    J --> K[Telematics Sync to Fleet Cloud via MQTT]
