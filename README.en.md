[![fr](https://img.shields.io/badge/lang-fr-yellow.svg)](https://github.com/yba01/student-management-cli/blob/main/README.md)
# Student Management CLI

## Description

This project is an object-oriented student management application built in Python. It allows users to read student data from a CSV file, parse grades, validate inputs, and display reports through a command-line interface.

### Objectives
- Load data from a CSV file
- Create student and grade objects
- Validate each student's information
- Display lists of valid or invalid students
- Search for students by number or code
- Edit invalid student information
- Add a new student
- Export valid students to a JSON file

---

## Project Structure

```text
student_management/
  main.py
  interface/
    menu.py
  model/
    date.py
    etudiant.py
    note.py
  services/
    gestion_donnees.py
    validator.py
  utils/
    data_reader.py
    parser_notes.py
  data/
    Donnees_Projet_Python_Dev_Data.csv
  valid.json
```

### Key Modules
- `student_management/main.py` : application entry point
- `student_management/interface/menu.py` : CLI user interface
- `student_management/services/gestion_donnees.py` : display, search, and JSON export logic
- `student_management/services/validator.py` : validation rules for students and grades
- `student_management/utils/data_reader.py` : CSV reading and object transformation
- `student_management/utils/parser_notes.py` : parsing formatted grades
- `student_management/model/etudiant.py` : student model
- `student_management/model/note.py` : grade model
- `student_management/model/date.py` : date normalization and validation

---

## Features

- Read student data from a CSV file
- Validate the following fields:
  - student code (`AAA111`)
  - student number (`7 alphanumeric characters`)
  - first name / last name
  - class (format `3e A`, `4e B`, etc.)
  - birth date in formats `dd/mm/yy`, `dd/mm/yyyy`, or `dd/month_name/yyyy`
  - grades for the following subjects: math, pc, svt, eng, fr, hg
- Export valid students to `valid.json`
- Display valid or invalid students using formatted tables
- Search students by student number or code
- Calculate subject averages for valid students

---

## Requirements

- Python 3.10+
- Python package:
  - `prettytable`

### Installation

```bash
pip install prettytable
```

---

## Usage

1. Open a terminal inside the `student_management` folder
2. Run the application:

```bash
python3 main.py
```

3. Follow the menu options:
- `1` : display data (valid/invalid)
- `2` : add a student (feature not implemented)
- `3` : edit a student (feature not implemented)
- `4` : search for a student by number or code
- `5` : export valid student data
- `6` : quit

---

## Expected Data Format

The CSV file `student_management/data/Donnees_Projet_Python_Dev_Data.csv` must contain structured rows separated by `;` with the following columns:

- code
- numéro
- nom
- prénom
- date
- classe
- note

Each grade must follow this format:

```text
math[assignment1|assignment2:exam]#pc[...]#svt[...]#fr[...]#eng[...]#hg[...]
```

Example:

```text
ABC123;1234XYZ;Dupont;Jean;12/03/2004;4A;math[10|12:15]#pc[11|14:16]#svt[12|13:17]#fr[14|15:16]#ang[10|13:18]#hg[12|14:16]
```

---

## JSON Export

The `Export` option generates `valid.json`, containing valid student data in JSON format.

---

## Possible Improvements

- Implement the `add()` and `edit()` methods in `student_management/interface/menu.py`
- Use relative paths instead of an absolute path in `GestionDonnees`
- Add database management or persistent storage
- Add unit tests
- Improve grade parsing to support more varied formats  
  (*there is no standard grade format, so parsing depends on the available format.*)

---

## Notes

- The project is designed for console usage.
- The CSV file path is currently hardcoded in `student_management/services/gestion_donnees.py`.
- `prettytable` is used to display readable CLI tables.


##  Screenshots
####  CSV file
![csv file](./image/csv.png)

####  CLI Interface
![cli interface du projet](./image/cli.png)

#### Valid data table
![exemple de tableau](./image/table.png)


## What I Learned

Through this project, I learned and practiced:

- Structuring a real Python project using modular architecture
- Applying Object-Oriented Programming (OOP) concepts
- Creating and managing Python classes and objects
- Separating responsibilities between models, services, utilities, and interface layers
- Reading and processing CSV files
- Exporting structured data into JSON format
- Parsing semi-structured text data
- Validating user and student data
- Using regular expressions for input validation
- Building an interactive Command Line Interface (CLI)
- Handling invalid inputs and edge cases
- Implementing search and filtering features
- Organizing business logic into reusable services
- Working with formatted terminal tables using `prettytable`
- Improving code readability and maintainability
- Designing a scalable and maintainable application structure
- Thinking about software architecture and clean code practices


## Auteur

Developed by @yba01.

---

## License

This project is licensed under the MIT License.