def attendance(roll_no):
    records = {
        1: "present",
        2: "absent",
        3: "present",
        4: "present",     
    }   
    if roll_no in records:
        return f"Student with roll number {roll_no} is {records[roll_no]}"
    else:
        return f"No attendance record found for roll number {roll_no}"

roll_no = int(input("Enter roll number to check attendance: "))
attendance_status = attendance(roll_no)
print(attendance_status)
