# 📦 Routing Optimization Program

An optimized Python-based package delivery routing system developed. This program determines efficient delivery routes using custom data structures and heuristics to ensure all packages arrive on time while maintaining a combined truck travel distance under 140 miles.

---

## Features

- Custom-built hash table for package storage and lookup
- Delivery status tracking by time and package ID
- Support for up to 3 trucks and 2 drivers with capacity constraints
- Real-time simulation of package delivery by minute
- Mileage calculation and delivery time logging
- Intuitive console interface to query package status at any time

---

## Developer Contributions

This program was developed from scratch using only native Python data structures (excluding `dict`) to demonstrate efficient algorithm design and problem-solving using:

- A fully implemented hash table with insertion and lookup by package ID
- A routing algorithm customized to fit real-world constraints and delivery requirements
- Manual time simulation to track truck progress minute-by-minute
- Conditional logic for delayed or corrected addresses (e.g., package #9)
- A user interface to check package statuses at any specific time
- Mileage tracking for validation of delivery efficiency
- Detailed in-line comments and structured design for maintainability

---

## Technologies Used

- **Python 3**
- **Custom hash table implementation**
- **Greedy/heuristic-based routing algorithm**
- **Console-based UI**

---

## Project Structure

```
.
├── main.py                # Entry point with simulation and CLI interface
├── hashtable.py           # Custom hash table implementation for package storage
├── package.py             # Package class with delivery attributes
├── truck.py               # Truck class to manage loads, routes, and mileage
├── ui.py                  # User interface for package lookups and delivery simulation
├── structure.txt          # File containing structure reference (not used by app)
├── csv/
│   ├── addresses.csv       # Raw address/location data
│   ├── distances.csv       # Distance matrix for route calculations
│   └── packages.csv        # Package info and delivery constraints
├── __pycache__/           # Python bytecode cache (auto-generated)
└── .idea/                 # IntelliJ project settings (ignored in version control)
```


---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/hjlinto/delivery-route-optimization.git
```
2. Run the main program
```bash
python main.py
```

---

## Reflections
- In a future version, I would explore implementing logic to handle the delegation of packages for each truck based on delivery deadlines and other restrictions as input, rather than the manual loading process it's currently set up to work by.

---

## Author
Created by: Hunter J Linton
