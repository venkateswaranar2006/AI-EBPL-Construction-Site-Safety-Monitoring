# 🦺 AI-Powered Construction Site Safety Monitoring System

This project is developed as part of the **AI-EPBL (Engineering Project-Based Learning)** curriculum. It leverages state-of-the-art **AI and Computer Vision** techniques to monitor construction sites in real-time, ensuring that all safety protocols are followed and alerting stakeholders of any safety violations.

# SafeSite AI – Real-Time Safety Monitoring for Construction Sites

## Team Members:
1. VENKATESWARAN A
2. DEV SAMSON S
3. NISHANTH S
4. BALAJI M
5. THARUNKUMAR I

## Problem Statement:
Construction sites present significant safety hazards, including falls, equipment-related injuries, and exposure to harmful substances. Traditional manual safety oversight is often inconsistent and reactive. There is a critical need for a proactive, real-time monitoring system to improve safety compliance and reduce accidents.

## Proposed Solution:
SafeSite AI is an AI-powered system leveraging computer vision and IoT technologies for real-time construction site monitoring. The system aims to ensure adherence to safety protocols and promptly identify potential hazards, thereby enhancing overall site safety.

## Objectives:
* Detect whether workers are wearing appropriate Personal Protective Equipment (PPE) such as helmets, gloves, and safety vests.
* Monitor worker proximity to hazardous zones and machinery.
* Provide real-time alerts to site supervisors upon detecting safety violations.
* Generate analytical reports to identify recurring safety issues and areas for improvement.

## System Architecture:
* **Input Devices:** High-definition cameras and IoT sensors strategically placed around the construction site.
* **Processing Unit:** Edge computing devices running trained deep learning models for real-time analysis.
* **User Interface:** Dashboard accessible via web and mobile applications for real-time monitoring and alerts.

## Technologies Used:
* **Computer Vision:** YOLOv7 for object detection to identify PPE compliance.
* **IoT:** Sensors to detect environmental hazards like gas leaks or temperature anomalies.
* **Backend:** Python with Flask framework for API development.
* **Frontend:** React.js for dashboard interface.
* **Database:** MongoDB for storing incident logs and analytics.

## Implementation Details:
* **Data Collection:** Gathered and annotated images from construction sites to train the YOLOv7 model for detecting PPE compliance.
* **Model Training:** Trained the model with a dataset comprising various scenarios, achieving an accuracy of 92% in PPE detection.
* **Sensor Integration:** Integrated IoT sensors to monitor environmental conditions, triggering alerts when thresholds are exceeded.
* **Dashboard Development:** Developed a user-friendly interface displaying real-time video feeds, alerts, and analytics.

## Results:
* **PPE Detection Accuracy:** 92%
* **Hazard Proximity Alerts:** System successfully alerted supervisors within 2 seconds of detecting a worker entering a hazardous zone.
* **User Feedback:** Site supervisors reported improved compliance and quicker response times to potential hazards.

## Challenges Faced:
* Variability in lighting conditions affecting camera feed quality.
* Ensuring real-time processing with limited computational resources on-site.
* Integrating diverse sensor data into a cohesive monitoring system.

## Future Enhancements:
* Incorporate predictive analytics to foresee potential hazards based on historical data.
* Expand the system to monitor ergonomic practices, reducing long-term injuries.
* Implement multilingual support for broader accessibility.

## Conclusion:
The SafeSite AI system demonstrates the potential of integrating AI and IoT technologies to enhance safety on construction sites. By providing real-time monitoring and alerts, the system proactively addresses safety violations, aiming to reduce accidents and promote a culture of safety compliance.
   git clone https://github.com/your-username/construction-site-safety-ai.git
   cd construction-site-safety-ai
