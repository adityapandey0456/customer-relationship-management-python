# Customer Relationship Management (CRM) System

Module: TECH6100 – Programming Principles
Organization: NovaTech Solutions

------------------------------------------------------------

Project Overview

This project is a desktop-based Customer Relationship Management (CRM) system developed as part of the TECH6100 – Programming Principles module. The application is designed to manage customer information efficiently using Python 3 and Object-Oriented Programming (OOP) principles.

The system replaces manual customer data handling with an automated solution that supports data validation, age calculation, filtering, exporting customer records, and a graphical user interface for user interaction.

------------------------------------------------------------

Project Objectives

The primary objective of this project is to design and implement a reliable and scalable CRM system that demonstrates intermediate-to-advanced Python programming concepts. The system focuses on clean architecture, modular design, robust error handling, and quality assurance through unit testing.

------------------------------------------------------------

Key Features

Customer data management using Object-Oriented Programming
Automated customer age calculation based on date of birth
Data validation for email addresses, dates, and numeric fields
Advanced filtering by age range and address
Export customer records to CSV or JSON format
Graphical User Interface (GUI) developed using Tkinter
Custom exception handling for improved system stability
Unit testing using Python’s unittest framework

------------------------------------------------------------

System Architecture

The application follows a modular architecture to ensure maintainability and scalability.

Main Modules
customer.py – Defines the Customer class and related logic
customer_manager.py – Manages customer records and filtering
utils.py – Contains reusable validation utilities
exceptions.py – Defines custom exception classes
gui_main.py – Implements the Tkinter-based GUI
tests – Contains unit test files

------------------------------------------------------------

Graphical User Interface

The GUI is implemented using Tkinter, Python’s standard GUI toolkit. The interface provides clearly labeled input fields, interactive buttons, and a dynamic table that updates in real time as customer data is added or filtered. The design emphasizes usability and responsiveness to support daily business operations.

------------------------------------------------------------

Data Validation and Error Handling

The system includes robust validation mechanisms to ensure data integrity. Email addresses and dates are validated before processing. Structured exception handling is implemented throughout the application to manage runtime errors gracefully and display user-friendly error messages.

------------------------------------------------------------

Testing and Quality Assurance

Unit testing is performed using Python’s built-in unittest framework. Tests are designed to verify core functionalities such as customer creation, duplicate prevention, age calculation accuracy, and filtering logic. Edge cases, including leap years and empty datasets, are also tested to ensure consistent behavior.

------------------------------------------------------------

Technologies Used

Python 3
Tkinter
unittest
Object-Oriented Programming

------------------------------------------------------------

How to Run the Project

Clone the repository
git clone https://github.com/your-username/crm-system-python-tech6100.git

Navigate to the project directory
cd crm-system-python-tech6100

Run the application
python gui_main.py

------------------------------------------------------------




License

This project is intended for academic and educational purposes only.
