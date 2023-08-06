# EnergyUsageMonitor - - End-to-End Project

This is an energy consumption monitoring project that uses real or simulated data to analyze and control energy consumption over time. The project is developed in Python and follows a modular structure to facilitate implementation and maintenance.

# Project Structure

The project is organized as follows:

```
energy_consumption_monitoring/
│
├── data/
│   ├── consumption_energy.csv          # CSV file with real energy consumption data (or simulated data)
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py          # Module for processing consumption data
│   ├── database.py                 # Module to handle SQLite database (not implemented)
│   ├── analysis.py                 # Module for data analysis (not implemented)
│   ├── user_interface.py           # Module for user interface (not implemented)
│   ├── control_system.py           # Module for consumption control system
│
├── main.py                         # Main file for program execution
├── requirements.txt               # File with project dependencies
├── README.md                      # This file, containing information about the project
├── generate_simulated_data.py     # File to generate simulated energy consumption data (optional)
```

# Features

The project includes the following features:

Data Loading and Processing: The data_processing.py module is responsible for loading energy consumption data from a CSV file and performing initial data processing, such as converting the date column to the datetime format.

Consumption Control: The control_system.py module implements the consumption control system. It allows you to set daily, weekly, and monthly consumption goals, calculate energy savings based on goals and consumption history, generate feedback on performance against goals, and display consumption history charts.

Trend Analysis: Trend analysis of consumption over time can be added to the analysis.py module, using techniques such as moving averages or linear regression. (This feature is not implemented, only mentioned as a suggested improvement).

User Interface: The user interface can be implemented in the user_interface.py module, using the customtkinter library or another of your choice to create a user-friendly graphical interface. (This feature is not implemented, only mentioned as a suggested improvement).

Database: Data persistence can be implemented in the database.py module, using an SQLite database to store consumption goals and history. (This feature is not implemented, only mentioned as a suggested improvement).

# Programming Languages Used

![Python](https://link_da_imagem/python.png)
![SQLite](https://link_da_imagem/sqlite.png)

How to Run the Project
Prerequisites: Make sure you have Python installed on your system.

Install Dependencies: Open a terminal or command prompt, navigate to the project directory, and execute the following command to install the dependencies:

```
pip install -r requirements.txt
```
Generate Simulated Data (optional): If you want to generate simulated data for testing the project, execute the following command:

```
python generate_simulated_data.py
```

Run the Project: To run the project, execute the following command: 

 ```
python main.py
```
Interact with the Project: The user interface allows you to set consumption goals and view consumption history over time. Use it to control energy consumption and analyze performance against the goals.

# Notes

This project is a basic framework that can be expanded and improved according to the specific needs of your use case.
Feel free to add more features, enhance the user interface, implement advanced analyses, or persist data in a database according to your requirements.

# Author

Thiago Ribeiro.






