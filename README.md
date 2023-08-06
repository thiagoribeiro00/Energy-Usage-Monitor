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

![Python](data:image/png;base64,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)
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






