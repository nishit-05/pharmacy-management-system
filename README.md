# Pharmacy Management System

A full-stack web application designed to manage pharmacy inventory, dispensing operations, and sales records, built with a strong emphasis on **data integrity, business logic correctness, and system design** rather than UI-heavy presentation.

---

## Introduction

The **Pharmacy Management System** was developed to simulate a real-world internal pharmacy software used for tracking medicines, managing stock levels, recording sales, and preventing invalid inventory operations.

The primary purpose of this project was to:
- Move beyond a basic CRUD application
- Introduce real **business rules and constraints**
- Demonstrate **backend system design**, data integrity, and workflow correctness
- Build a usable **end-to-end (frontend + backend)** application suitable for portfolio and interview discussions

This project intentionally prioritizes **correctness, structure, and maintainability** over UI polish, reflecting how early-stage internal tools are often built in real organizations.

---

## Features

- Inventory management with stock quantity tracking  
- Medicine dispensing with automatic stock deduction  
- Sales & order history recording  
- Prevention of over-dispensing and invalid stock states  
- Session-based login flow for controlled access  
- Modular backend architecture (routes, services, models)  
- MySQL-backed relational database  

---

## Project Evolution & Transformation

This project was **not built from scratch**. It was intentionally evolved from a simple learning prototype into a structured system.

### Before (Baseline State)
- Flat Flask app with mixed logic
- SQLite database
- Basic CRUD operations only
- No validation or constraints
- Inventory and orders were not logically connected
- Looked like a learning/demo project

### After (Optimized State)
- Modular Flask architecture (routes, services, models)
- Migration from SQLite to **MySQL**
- Inventory stock tracking with constraints
- Transactional dispense logic
- Sales & order persistence
- Session-based access flow
- Seeded demo data for realistic usage

This transformation is central to the value of the project.

---

## Architecture Overview

pharmacy/
├── routes/ # Request handling (Flask blueprints)
├── services/ # Business logic & validation
├── models/ # Database models
├── templates/ # Frontend views (HTML)
├── static/ # CSS & JavaScript
├── extensions.py # Database initialization
└── init.py # App factory


This structure follows **industry-standard separation of concerns**, making the codebase easier to maintain and extend.

---

## Database Design

- Relational MySQL database
- Primary keys and foreign key relationships
- Orders reference medicines to maintain sales history
- Stock updates and order creation handled atomically

This ensures historical accuracy and prevents inconsistent inventory states.

---

## Metrics & Measured Impact

The following metrics were evaluated in a test environment by comparing the baseline and optimized versions:

### 1. Data Integrity Improvement
- Migrated from unconstrained CRUD operations to relational consistency using MySQL
- Enforced stock constraints and transactional updates

---

### 2. Invalid Operation Reduction
- Added validation for dispense quantity and stock availability
- Blocked negative stock and over-dispensing cases

---

## Demo Data & Testing

- Includes a seed script to populate realistic pharmacy inventory
- Enables meaningful testing of inventory states (OK / Low / Out of stock)
- Supports demonstration without manual data entry

---

## Tech Stack

**Backend**
- Python
- Flask
- SQLAlchemy

**Database**
- MySQL

**Frontend**
- HTML
- CSS
- JavaScript (vanilla)

---

## Notes

- This project focuses on **system design, correctness, and data integrity**
- UI is intentionally simple and functional
- Designed as a backend-heavy, business-logic-driven application
- Suitable for academic, portfolio, and interview discussion

---

## Author

**Nishit Dongre**

- LinkedIn: [http://linkedin.com/in/nishit-dongre-675031382](http://linkedin.com/in/nishit-dongre-675031382)

---

## License

This project is intended for educational and portfolio use.
