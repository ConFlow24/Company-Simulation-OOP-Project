ok legit na to. AKo gumawa ng lahat ng concept pinaganda ko lang kay GPT. Pag may mali siya may kasalanan.


# 🏢 Company Simulation System

## 📌 Overview

This program simulates the daily operations of a company over a user-defined number of days. At the start, the user selects how many days to simulate and how many employees to begin with.

Each day represents a full business cycle involving employee attendance, task execution, inventory management, and financial updates.

The system is **primarily user-driven**, where the player acts as the CEO and directly manages company decisions. However, an **auto-simulation option** is available for selected day ranges.

---

# 🧠 Core Daily Flow

Each simulated day follows this structure:

```plaintext id="flow3"
1. Start of Day
2. Generate Tasks / Orders
3. Employee Clock-in (attendance check)
4. CEO Task Assignment (manual default)
5. Task Execution (based on speed + punctuality)
6. Inventory & Money Updates
7. Random Events
8. Promotions / Demotions
9. End-of-Day Report
10. CEO Action Menu
```

---

# 👑 CEO Control System (DEFAULT MODE)

The player always acts as the CEO by default and directly controls company decisions.

## 🎮 CEO Responsibilities:

* Assign tasks to employees manually
* Hire new employees
* Fire employees or managers
* Promote or demote employees
* Give bonuses or apply deductions
* Buy and sell inventory manually
* Manage stock levels
* Review employee performance

---

# ⚙️ Auto-Simulation Mode

The system allows the CEO to enable **automatic simulation** for a selected number of days.

During auto-mode:

* Tasks are assigned automatically
* Inventory decisions are system-generated
* Employee actions are simulated without input

The user can return to manual control after the selected period ends.

---

# 📋 Daily CEO Menu (UI FLOW)

At the end of each day, the user is presented with the main control menu:

```plaintext id="menu1"
===== END OF DAY MENU =====

1. Start Next Day
2. CEO Management Panel
3. View Reports
4. View Inventory
5. View Employees
6. Enable Auto-Simulation (Select Day Range)
7. Exit Simulation
```

---

## 🧑‍💼 CEO Management Panel (Option 2)

Inside this panel, the user can:

### Employee Control

* Hire employee
* Fire employee
* Promote / demote employee
* Assign tasks manually

### Financial Control

* Give bonuses
* Apply deductions

### Inventory Control

* Buy stock
* Sell stock
* Adjust inventory

---

## 📊 Reports Menu (Option 3)

Displays:

* Daily profit/loss
* Task completion rate
* Employee performance rankings
* Best and worst employees
* Company efficiency score
* Attendance summary

---

## 📦 Inventory View (Option 4)

Shows:

* Current stock levels
* Product status
* Inventory value

---

## 👥 Employee View (Option 5)

Shows:

* All employees
* Role hierarchy
* Speed and punctuality stats
* Attendance record

---

# 👨‍💼 Employee System

## 🧍 Roles:

* Intern → low efficiency, training stage
* Employee → standard worker
* Senior → high efficiency worker
* Manager → supervises staff and supports CEO decisions
* CEO → player-controlled role

---

## 📊 Stats:

### ⚡ Speed

* Determines task completion rate

### ⏰ Punctuality

* Affects attendance (late/absent probability)

---

# 📦 Inventory & Finance System

The company manages:

* product stock
* buying and selling operations
* cash balance

Employees and CEO actions directly affect:

* inventory levels
* company profit

---

# 🎲 Random Events System  (OPTIONAL)

Each day may include events such as:

* employee sickness
* sudden increase in orders
* supply shortages
* productivity changes

---

# 🧱 System Architecture (OOP Structure)

```plaintext id="arch3"
Employee (base class)
 ├── Intern
 ├── Employee
 │     └── Senior
 ├── Manager
 └── CEO (player-controlled role)

SimulationEngine
TaskGenerator
InventorySystem
FinanceSystem
ReportSystem
CEOInterface (command handler)
AutoSimulationController
```

---

# 🎯 Purpose of the Project

This project demonstrates:

* Object-Oriented Programming principles (inheritance, polymorphism, encapsulation)
* Simulation of real-world business operations
* Human decision-making integrated with automated systems
* System modularity and structured design

---

# 📌 Footnote (Optional Expansion Ideas)

A significantly larger extension of this project could include:

* A full graphical user interface (GUI) instead of a console-based system
* Persistent data storage using JSON files (saving/loading simulation states)
* Charts or visual analytics for company performance over time
* Enhanced AI-based employee decision-making systems
