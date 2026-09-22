# Week 1 Python Foundations Capstone — Student Grade Report Generator

## What the project is about

This capstone is a progressively built **Student Grade Profile System** that I developed during Week 1 of the Introduction to Python Programming course @Publica-AI Academy. The Tasks 1–5 build on one another, with each task introducing another set of Python concepts until the final task becomes a **multi-student class grade report generator**.

The final program allows a user to enter students one after another, calculate each student's final score, assign a letter grade, determine PASS/FAIL status using both score and attendance, and produce a summary showing the **class average and number of students who passed**.

## How the project develops

| Stage | Main purpose | Python concepts introduced |
|---|---|---|
| **Task 1** | Personal introduction card | `print()`, `input()`, comments, indentation |
| **Task 2** | Student profile | Variables, data types, `type()`, casting |
| **Task 3** | Grade & eligibility calculations | Arithmetic, comparisons, logical operators, `+=`, `//`, `%` |
| **Task 4** | Single-student grade classifier | `if`, `elif`, `else`, truthy/falsy checks |
| **Task 5 — Capstone** | Multi-student class report | `while`, `for`, `range()`, `break`, `continue` |

Thus, the final capstone is essentially the **Task 4 single-student grade classifier** expanded into a **small class-level reporting system** in Task 5.

## What the final capstone does

For each student, the program:

1. Requests the student's name. Entering **`Done` (case insensitive)** ends data collection.
2. Collects the exam and coursework scores.
3. Collects attendance, allowing up to **three attempts** if a negative value is entered.
4. Skips the student if all three attendance attempts are invalid.
5. Calculates the final score using:
   - **60% exam score**
   - **40% coursework score**
6. Assigns a grade:
   - `A` — 90 and above
   - `B` — 80–89.99
   - `C` — 70–79.99
   - `D` — 60–69.99
   - `F` — below 60
7. Determines PASS/FAIL:
   - PASS requires a final score of at least **50** **and** attendance of at least **75%**.
8. Immediately prints the student's numbered report.
9. Maintains running totals for:
   - number of students,
   - total final scores,
   - number of students who passed.
10. When data entry ends, calculates and displays the **class average** and **pass count**.

## Important design constraint

The instructions deliberately restricted the project to concepts that have been taught up to each point in Week 1. In particular, the project **must not use**:

- f-strings or other string-formatting shortcuts such as `.format()` and `%`;
- lists, tuples, sets, or dictionaries;
- user-defined functions (`def`).

These concepts were reserved for later weeks. Consequently, Task 5 cannot store all student records in a list. Instead, it **reports each student immediately and maintains running totals** using variables and augmented assignment.

## Overall project idea

In simple terms, this project demonstrates how a basic Python program can evolve from **collecting and displaying information about one student** into a **loop-driven system capable of processing an entire class**.

The capstone therefore serves as a practical demonstration of the Week 1 progression from basic Python syntax and data types through calculations and conditionals, and finally to **iteration and control flow** with `while`, `for`, `break`, and `continue`.

