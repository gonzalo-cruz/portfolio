---
title: "Autonomous Object-Avoiding Robot (STM32)"
date: 2023-05-15
description: "A dual-mode robotic vehicle developed in C, featuring real-time interrupt-based control and Bluetooth telemetry."
tags: ["Embedded Systems", "C", "Robotics", "STM32"]
---

## 💡 The Challenge
Design a robotic control system capable of reacting to obstacles in **less than 60ms** while simultaneously processing Bluetooth commands from a mobile app. The constraint: do this on a microcontroller without blocking the CPU.

## ⚙️ System Architecture
Built on the **STM32 Nucleo-L152RE**, the system avoids the "super-loop" architecture by using **Hardware Interrupts**:

* **Distance Sensing:** Uses `TIM2` Input Capture to measure ultrasonic echo width with microsecond precision.
* **Motor Control:** Uses `TIM3` PWM generation for smooth acceleration and "soft braking."
* **Telemetry:** Uses `USART2` Interrupts to receive Bluetooth packets asynchronously.

## 🚀 Outcome
The robot successfully operates in two modes:
1.  **Autonomous:** Navigates environments, slowing down at 20cm and performing an emergency stop at 10cm.
2.  **Manual:** Overrides autonomous logic via an Android app for direct RC control.

This project bridged the gap between code and physical hardware, emphasizing the importance of **Real-Time Operating constraints**.