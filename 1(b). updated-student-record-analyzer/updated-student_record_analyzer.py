def get_details():
    students_details = {}
    number_of_students = int(input('Enter the number of students:'))
    for i in range(number_of_students):
        name = input('Enter Student Name:')
        marks = int(input('Enter Marks:'))
        students_details[name] = marks
    return students_details

def analyze_students(student_record):
    average_marks = sum(student_record.values())/len(student_record)
    topper = max(student_record.items(), key= lambda students: students[1])
    failed_students = [name for name,marks in student_record.items() if marks<40]
    unique_marks = set(student_record.values())
    return {"average":average_marks, "topper":topper, "failed students":failed_students, "unique marks":unique_marks}

def display_result(results):
    print("--------Analysis--------")
    print("Average Marks:",results['average'])
    print("Topper:",results['topper'][0],results['topper'][1],"marks")
    print("Failed Students:",results['failed students'])
    print("Unique Marks:",results['unique marks'])

def main():
    student_record = get_details()
    results = analyze_students(student_record)
    display_result(results)

main()