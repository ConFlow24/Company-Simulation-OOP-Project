# Company Simulation Game

Welcome to the Company Simulation Game! This is a text-based object-oriented Python program where you play as a newly appointed CEO. Your main objective is to manage your employees, oversee daily tasks, handle the company's inventory, and build a profitable business! 

Your ultimate goal is to reach $1,000,000 in cash without going bankrupt.

---

## What to Expect

This program simulates the daily operations of a business. When you play, you will experience:
*   **Employee Management:** Hiring, firing, promoting, demoting, and managing salaries.
*   **Daily Workflow:** A realistic workday flow where attendance is checked, tasks are generated, and employees spend an 8-hour shift completing them.
*   **Inventory & Finances:** Balancing the cost of buying stock against the profits of selling it, all while ensuring you have enough money to pay your employees at the end of the week.
*   **Unpredictability:** Random events happen throughout the week similar to real life workplace challenges.

---

## How to Play

### Getting Started
1. Run `main.py` in your terminal or command prompt.
2. Enter a name for your company.
3. Choose your starting number of employees (between 5 and 10).
4. The simulation will begin at Day 1.

### The Daily Loop
Each simulated day follows a strict schedule:
1. **Attendance:** Employees clock in. Based on their "Punctuality" stat, they may be Present, Late, or Absent.
2. **Events:** The system checks if any random events occur today.
3. **Task Generation:** The game generates necessary tasks for the company to function.
4. **Task Assignment:** You must assign these tasks to your available employees. You can do this manually, or set the game to "Auto-Simulation" to let the system assign tasks based on roles.
5. **Work Hours:** Employees spend 8 hours working. If tasks are not finished, they will work overtime.
6. **End of Day:** Completed tasks affect your inventory and cash. Employee stats update. You are then taken to the End of Day Menu.

### Winning and Losing
*   **Bankruptcy (Loss):** Every 7 days (1 week), employee salaries are deducted from your total cash. If your cash drops to $0 or below, your company goes bankrupt and the game ends.
*   **Success (Win):** If you reach $1,000,000, you have built a highly successful company. You will be congratulated and given the option to keep playing or retire.

---

## Core Features & Mechanics

### Employees
Every employee has a Name, Role, Pay, Speed, and Punctuality. 
*   **Speed:** Determines how fast they complete tasks. Employees level up their speed every 8 completed tasks.
*   **Punctuality:** Determines how likely they are to show up on time. Excessive lates or absences will result in automatic salary deductions.

**Roles in the Company:**
*   **Intern:** Lowest pay and speed. Sometimes given "Unique" tasks like learning (which permanently boosts their stats) or useless errands.
*   **Employee:** The standard workforce. Reliable and steady.
*   **Senior:** Fast workers. They can trigger "Unique" tasks to mentor lower-level employees, temporarily boosting their speed.
*   **Manager:** Very fast workers. They can manage teams to provide large temporary speed boosts. Limited to a maximum of 5 per company.
*   **CEO (You):** You cannot be fired. You occasionally perform automatic strategic tasks like giving bonuses, or emergency hiring/firing.

### Tasks
There are three main types of operational tasks:
1.  **Buy:** Costs money. Purchases an item and puts it in the "Store Buffer."
2.  **Store:** Takes items from the "Store Buffer" and officially adds them to your Inventory.
3.  **Sell:** Takes an item from your Inventory and sells it for a 20% profit.

### The CEO Panel
At the End of Day menu, you can access the CEO Panel. Here you can:
*   Hire new staff from a list of generated candidates.
*   Fire underperforming staff.
*   Promote your employees
*   Demote employees.
*   Manually increase or decrease salaries.
*   Manually buy or sell inventory items bypassing the daily task system.

### Random Events
The simulation includes a random event system:
*   **Productivity Changes:** A 15% chance for a bad event (like a broken AC or internet outage) that halves work speed. A 15% chance for a good event (like free donuts or bonus incentives) that doubles work speed.
*   **Order Spikes:** A 15% chance for a sudden influx of customer orders, which generates four times the usual amount of "Sell" tasks for the day.
*   **Buy Spikes:** A 15% chance for supplier discounts, generating a massive wave of "Buy" tasks.

---

## Tips for Beginners

*   **Watch Your Cash Flow:** Do not spend all your money on buying inventory. Every 7 days, salaries are deducted. Always keep a cash reserve to survive payday.
*   **Automate When Stable:** Manually assigning tasks is great for early optimization, but as your company grows, use the "Auto-Simulation" feature from the End of Day menu to run multiple days automatically!
*   **Promote Wisely:** Promoting an Intern to an Employee increases their salary. Make sure your daily profits can handle the new payroll before promoting staff.
*   **Pay Attention to Warnings:** If the game tells you that you have too many tasks per employee, visit the CEO Panel and hire someone immediately. Overworked employees will struggle to keep up.
*   **Check Reports Regularly:** Use the "View Reports" option at the end of the day to see your total inventory value, cash, and employee list. It helps you decide if you need to manually intervene.

---

## How to Run

Requirements:
* Python 3.10 or higher.

Steps:
1. Open your terminal/command prompt.
2. Navigate to the project directory.
3. Run the following command:
   `python main.py`
