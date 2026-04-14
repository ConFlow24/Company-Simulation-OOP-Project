# Workplace Simulation System 🏢

## 📌 Overview

The **Workplace Simulation System** is an Object-Oriented Programming (OOP) project that simulates the daily operations of a business. Instead of simply storing data, the system models how employees behave, how workdays progress, and how business performance evolves over time.

This project demonstrates core OOP principles such as **encapsulation, inheritance, polymorphism, and abstraction** through a dynamic and interactive simulation.

---

## 🎯 Objectives

* Simulate day-to-day workplace operations
* Track employee attendance, performance, and salary
* Manage inventory and process daily orders
* Generate reports based on daily outcomes
* Apply OOP concepts in a real-world scenario

---

## ⚙️ Core Features

### 👨‍💼 Employee Management

* Add, remove, and view employees
* Roles (e.g., Manager, Staff)
* Attributes:

  * Punctuality
  * Productivity
  * Salary rate

### 🗓️ Workday Simulation

* Start and end a workday
* Employees may:

  * Arrive on time, late, or be absent
  * Generate performance output
* Randomized behavior based on employee attributes

### 💰 Payroll System

* Salary calculation based on:

  * Attendance
  * Performance
* Bonuses:

  * Perfect attendance
  * High productivity
* Deductions:

  * Late or absences

### 📦 Inventory & Orders

* Manage product stock
* Simulate daily orders
* Automatically update inventory levels

### 📊 Reports

* Daily summary:

  * Attendance
  * Employee performance
  * Profit/loss
  * Inventory changes

---

## 🧠 OOP Concepts Demonstrated

* **Encapsulation** – Private fields with controlled access
* **Inheritance** – Base `Employee` class extended by roles
* **Polymorphism** – Different salary/behavior logic per role
* **Abstraction** – Simulation engine handling system processes

---

## 🧩 System Structure (Simplified)

```
Employee (abstract)
 ├── Manager
 ├── Staff

SimulationEngine
WorkDay

AttendanceRecord
PerformanceRecord

PayrollSystem

Product
Order
InventoryManager

ReportGenerator
SystemController
```

---

## 👥 Team Roles

* **Simulation Engine Developer** – Handles day cycle and logic flow
* **Employee System Developer** – Manages employee data and behavior
* **Payroll Developer** – Computes salary, bonuses, and deductions
* **Inventory Developer** – Handles products and order processing
* **UI/Integration Developer** – Connects modules and displays output

---

## 🚀 Future Improvements

* Save/Load system (file handling)
* Promotion and ranking system
* Random workplace events
* Graphical User Interface (GUI)

---

## 🛠️ Tech Stack

*(To be decided by the team)*

* Language: Java / Python / C++
* Interface: CLI or GUI

---

## 📅 Project Status

🚧 In Development – Initial design and planning phase

---

## ✨ Notes

This project focuses on transforming a traditional management system into a **dynamic simulation**, making it more interactive, scalable, and suitable for demonstrating advanced OOP design.




Dependencies:
Faker - on cmd enter "pip install faker"