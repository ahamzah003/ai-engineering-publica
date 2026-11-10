# Week 1 Capstone: Multi-student class report generator

student_counter = 0
sum_final_score = 0.0
pass_counter = 0

while True:
    print("\n--- Add Student (type 'done' as the name to finish) ---")
    user_name = input("Enter student's fullname: ").strip()
    if user_name.lower() == "done":
        break

    exam_score = float(input("Enter student's exam score: "))
    cw_score = float(input("Enter student's coursework score: "))

    # Attendance with up to 3 attempts
    attendance_pct = -1
    for attempt in range(3):
        attendance_pct = float(input("Enter student's attendance percentage score: "))
        if attendance_pct < 0:
            print("  Invalid attendance -- try again.")
        else:
            break
    else:
        print("Skipping student due to invalid attendance entries.")
        continue

    # Compute final score (same weighting as subtask 4)
    final_score = exam_score * 0.6 + cw_score * 0.4

    if not user_name:
        user_name = "Anonymous Student"

    # Grade classification
    if final_score >= 90:
        grade = "A"
    elif final_score >= 80:
        grade = "B"
    elif final_score >= 70:
        grade = "C"
    elif final_score >= 60:
        grade = "D"
    else:
        grade = "F"

    # PASS/FAIL
    if final_score >= 50 and attendance_pct >= 75:
        result = "PASS"
    else:
        result = "FAIL"

    # Update running totals
    student_counter += 1
    sum_final_score += final_score
    if result == "PASS":
        pass_counter += 1

    # Print student report line
    print(student_counter, ". ", user_name, " | ", "Final: ", round(final_score, 1), " | ", "Grade: ", grade, " | ", result, sep="")

# After loop ends, print class summary
print("="*40)
if student_counter > 0:
    class_average = sum_final_score / student_counter
    print("Class average  :", round(class_average, 1))
    print("Students passed:", pass_counter, "/", student_counter)
else:
    print("No students were entered.")
print("="*40)
