# Week 1 Python Foundations Capstone — Student Grade Report Generator

## 📖 What the project is about

It allows a teacher to process students' scores and attendance, determine their grades and PASS/FAIL status, and generate a class summary showing the **class average and number of students who passed**.

### 🔄 Project Workflow
🚀 Download and run the [[script](https://github.com/ahamzah003/ai-engineering-publica/blob/master/python/projects/week1/StudentGradeReportGenerator.py)] to see the workflow in action.
 
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

## 💡 Python Concepts Applied

This project is a progressively built **Student Grade Profile System** developed across five tasks during Week 1 of the Introduction to Python Programming course at Publica-AI Academy. Each task introduces another group of Python concepts, and the final Task 5 combines them into a multi-student grade report generator.

The progression is:

| Stage | Main purpose | Python concepts introduced |
|---|---|---|
| **Task 1** | Personal introduction card | `print()`, `input()`, comments, indentation |
| **Task 2** | Student profile | Variables, data types, `type()`, casting |
| **Task 3** | Grade & eligibility calculations | Arithmetic, comparisons, logical operators, `+=`, `//`, `%` |
| **Task 4** | Single-student grade classifier | `if`, `elif`, `else`, truthy/falsy checks |
| **Task 5 — Capstone** | Multi-student class report | `while`, `for`, `range()`, `break`, `continue` |

Thus, the final capstone is essentially the **Task 4 single-student grade classifier** expanded into a **small class-level reporting system** in Task 5.

## 🚦 Instructions and restrictions

The instructor deliberately restricted the project to concepts that had been taught up to each point in Week 1. In particular, the project **must not use**:

- f-strings or other string-formatting shortcuts such as `.format()` and `%`;
- lists, tuples, sets, or dictionaries;
- user-defined functions (`def`).

These concepts were reserved for later weeks. Consequently, Task 5 cannot store all student records in a list. Instead, it **reports each student immediately and maintains running totals** using variables and augmented assignment.

## 🧠 Overall project idea

In simple terms, **this week's capstone is a student grade-reporting system that demonstrates how progressively introduced Python fundamentals can be combined into a practical application.**

The project moves from collecting and displaying basic information about one student to processing multiple students, applying grading and attendance rules, and producing a class-wide summary. It demonstrates the progression from basic syntax and data types through calculations and conditionals, and finally to **iteration and control flow** with `while`, `for`, `break`, and `continue`.
