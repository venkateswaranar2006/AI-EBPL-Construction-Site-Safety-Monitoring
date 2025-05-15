# 🦺 AI-Powered Construction Site Safety Monitoring System

This project is developed as part of the **AI-EPBL (Engineering Project-Based Learning)** curriculum. It leverages state-of-the-art **AI and Computer Vision** techniques to monitor construction sites in real-time, ensuring that all safety protocols are followed and alerting stakeholders of any safety violations.

---

## 🚧 Project Overview

Construction sites are inherently dangerous environments. This AI-based monitoring system is designed to:

- Detect and classify personal protective equipment (PPE) like helmets and safety vests.
- Identify safety violations such as missing PPE.
- Highlight and monitor predefined **danger zones** on-site.
- Provide visual dashboards with alerts and analytics for better site supervision.

---

## 🎯 Objectives

- Enhance worker safety through automated visual monitoring.
- Reduce human error in PPE compliance checks.
- Enable real-time alerts for unsafe behaviors or zone breaches.
- Collect data to improve future safety protocols using AI insights.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **YOLOv5** (for object detection)
- **OpenCV** (image processing and annotations)
- **PyTorch** (deep learning framework)
- **Matplotlib** / **Plotly** (for sensor and safety analytics)
- **Streamlit / Tkinter** (optional dashboard interface)
- **LabelImg** (for dataset annotation)
- **Custom-trained dataset** of construction site images

---

## 🧠 AI Capabilities

- **PPE Detection**: Identifies whether each worker is wearing a helmet and safety vest.
- **Zone Intrusion**: Detects when workers enter restricted or hazardous zones.
- **Real-time Alerts**: Notifies safety officers about violations through visual overlays.
- **Analytics**: Graphs and statistical summaries of safety trends and sensor data.

---

## 📸 Sample Outputs

### ✅ Proper PPE Detection
- Detected Helmet (Confidence: 0.82)
- Detected Vest (Confidence: 0.83)
- Status: **Safe**

### ❌ Safety Violation
- Missing Equipment or Entry in Danger Zone
- Status: **⚠️ Violation Detected**

### Danger Zone Mapping
- Red overlay highlights hazardous zones with polygon boundaries.
- Live intrusion detection and tracking.

---

## 🧪 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/construction-site-safety-ai.git
   cd construction-site-safety-ai
