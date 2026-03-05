# Students data
students = {
    "Alice": [85, 90, 80, 90],
    "Bob": [60, 70, 50, 70],
    "Clara": [95, 98, 92, 100]
}

def calculate_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

print("===== Student Grade Report =====")
passed_count = 0
failed_count = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    status = "PASS" if avg >= 60 else "FAIL"
    
    if status == "PASS":
        passed_count += 1
    else:
        failed_count += 1
        
    print(f"{name:<10} | Avg: {avg:>6.2f} | Grade: {grade} | Status: {status}")

print("================================")
print(f"Total Students : {len(students)}")
print(f"Passed         : {passed_count}")
print(f"Failed         : {failed_count}")
