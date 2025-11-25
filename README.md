# ATTENDANCE-MANAGEMENT

## Overview of the Project:

Attendance Manager is a modular, console-based Python application for students to track subject-wise attendance, generate reports, and predict how many future classes are needed to reach a target attendance percentage. The app is intentionally simple, easy to extend, and suitable as a small academic project or portfolio piece.

## Features:

- Check attendance for a single subject (attendance %, status).

- Generate an overall attendance report across multiple subjects.

- Predict classes required to meet a target attendance percentage (e.g., 75%).

- Clean CLI menu-driven interface.

- Input validation and user-friendly messages.

- Modular architecture for easy extension (GUI, CSV import/export, DB)


## Technologies/Tools Used:

- Python 3.7+

- Optional: matplotlib (for adding graphs later)

- Project modules:

  - main.py — entry point and menu flow. (/mnt/data/main.py)

  - info.py — handles validated user input. (/mnt/data/info.py)

  - display.py — printing / formatting (tables, messages). (/mnt/data/display.py)

  - report.py — generates summary & reports. (/mnt/data/report.py)

  - prediction.py — forecasting logic for targets. (/mnt/data/prediction.py)


## Steps to Install & Run the Project

- Steps to install & run the project

- Clone or copy the project folder (or ensure the uploaded files are in one folder).

- (Optional) Create & activate a virtual environment

    python -m venv venv
    #### Windows
    venv\Scripts\activate
    #### macOS / Linux
    source venv/bin/activate

- Install optional dependencies (if you plan to use graphics)
    pip install matplotlib
- Run the app
    python /mnt/data/main.py

## Instructions for Testing

Manual test scenarios (recommended):

- Single subject check

    - From main menu choose 1 (Check attendance for a particular subject).

    - Enter subject name: Maths

    - Total classes: 40

    - Attended classes: 30

    - Expect: percentage 75.00% (or similar) and status/suggestion.

- Multiple subjects / overall report

    - Choose 2 (View overall attendance report).

    - Enter two or more subjects (example values):

        - Physics — total 45, attended 30

        - Chemistry — total 40, attended 28

        - Expect: list of subjects with percentages and an aggregate summary.

- Prediction

    - For a subject with low percentage, use prediction logic to compute how many consecutive future classes to attend to reach target (e.g., 75%).

    - Validate the math using manual calculation:

        Required formula: find smallest x such that (attended + x) / (total + x) >= target.

- Invalid inputs

    - Try invalid inputs: negative numbers, non-integers, attended > total.

    - Expect clear validation messages and re-prompt.

- Edge cases

    - 0 total classes (new subject).

    - Already above target (prediction returns 0 or appropriate message).

   ## ASCII Architecture Diagram (module relationships)

    ![architecture](https://github.com/user-attachments/assets/75a78d58-16c8-4e2e-a9bb-0514dbf8031b)

  ## Screenshots

  ![OUTPUT 1](https://github.com/user-attachments/assets/a3ef914b-fb11-420b-889f-32ce3efd687c)
  ![OUTPUT 2](https://github.com/user-attachments/assets/0a5d8bd1-4eef-42ea-a4b7-2ff58a9fd9dc)
