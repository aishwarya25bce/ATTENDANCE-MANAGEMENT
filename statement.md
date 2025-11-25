# Project Statement – Attendance Manager

## 1. Project Title

Attendance Manager (Python-Based Console Application)

## 2. Problem Statement

Students often struggle to manually calculate their attendance percentage across multiple subjects and keep track of how many more classes they must attend to meet mandatory attendance criteria (commonly 75%). Manual tracking is error-prone, time-consuming, and does not provide predictive insights.

- There is a need for a simple and accurate system that:

- Calculates attendance automatically

- Generates clear reports

- Predicts future attendance requirements

This project aims to create such a solution using Python.

## 3. Objectives of the Project

- To develop a user-friendly attendance management tool.

- To accurately calculate attendance percentages for subjects.

- To provide overall attendance reports.

- To predict the number of future classes needed to reach a target percentage.

- To validate all user inputs to avoid errors.

- To implement the project using a modular programming approach.

## 4. Scope of the Project

The project covers:

- Managing attendance for any number of subjects

- Displaying individual and overall attendance status

- Predicting attendance progress

- Providing suggestions based on calculations

- Text-based user interaction via menus

The project does not cover:

- Storing attendance long-term

- GUI or mobile interface

- Automatic attendance tracking

- Integration with databases or sensors

- These can be added as future enhancements.

## 5. Project Description

The Attendance Manager is divided into multiple Python modules:

### main.py

Contains the main menu, controls program flow, and connects all modules.

### info.py

Handles user input for subject details, validating values before returning them.

### display.py

Formats and displays results, ensuring user-friendly output.

### report.py

Generates attendance percentages and overall attendance analysis.

### prediction.py

Calculates how many more classes a student must attend to meet a specific attendance percentage.

The modular structure ensures clarity, readability, and easy maintenance.

## 6. Methodology

1. User selects an option from the menu:

    - Check attendance for one subject

    - View overall report

2. Program collects required inputs using info.py.

3. Attendance calculations and predictions are performed.

4. Output is displayed using the display.py module.

5. User may repeat actions until choosing to exit.

## 7. Expected Output

- Attendance percentage for each subject

- Overall attendance report

- Prediction showing required future attendance

- Validation warnings for incorrect inputs

## 8. Conclusion

The Attendance Manager meets the core requirements of automating attendance calculations and providing predictive insights. Its modular design makes it extendable, accurate, and suitable for academic demonstration or future development into a full-scale attendance system.
