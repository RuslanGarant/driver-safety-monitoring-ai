# Garant-Fleet DSM: Edge AI Driver Monitoring & Fatigue Detection Platform
### Part of the "Garant-Fleet AI" Integrated Intelligent Analytics Ecosystem

---

**GARANT-FLEET AI PLATFORM** *Enterprise Infrastructure for Commercial Fleet Safety, Computer Vision Telematics & Driver Status Monitoring* `[ Framework: Garant-Fleet ID ]` • `[ Engine: Garant-Fleet DSM ]` • `[ System: Garant-Fleet Fuel ]`

---

<div style="page-break-after: always; break-after: page;"></div>

## Platform Overview
**Garant-Fleet DSM** is a high-performance, real-time computer vision monitoring platform engineered for commercial transport infrastructure, industrial logistics, and enterprise fleets. Developed as a core intelligence pillar of the unified **Garant-Fleet AI** ecosystem by a single founder, this platform executes low-latency edge inference to mitigate heavy vehicle accident risks by instantly identifying driver drowsiness, micro-sleep events, distraction vectors, and cognitive fatigue patterns.

The platform wraps bare-metal mathematical logic into an enterprise-grade safety countermeasure, translating raw facial feature metrics into physical in-cabin intervention and real-time fleet telematics alarms.

---

## 1. System Level Architecture
The platform operates as a localized hardware-software loop, moving seamlessly from optical pixel ingestion to commercial telematics data synchronization.

```mermaid
graph TD
    A[Near-Infrared Camera Input] -->|High-FPS Video Stream| B[Face Mesh & Landmark Locator]
    B -->|Spatial Point Extraction| C[Mathematical Vector Analyzer / EAR]
    C -->|Continuous Metric Tracking| D[Temporal Counter & Anomaly Filter]
    D -->|Fatigue Verification Layer| E[In-Cabin Decision Engine]
    E -->|GPIO Low-Latency Signal| F[Audio Buzzer / Safety Hardware]
    E -->|Secure MQTT JSON Payload| G[Fleet Management Cloud Server]
