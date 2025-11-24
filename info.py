
def input_single_subject():
    subject = input("Enter subject name: ")
    total = int(input(f"Enter total number of classes for {subject}: "))
    attended = int(input(f"Enter total number of classes attended in {subject}: "))
    min_percentage = 75.0
    return {subject: {'total': total, 'attended': attended, 'min_percentage': min_percentage}}

def input_multiple_subjects():
    n = int(input("Enter total number of subjects: "))
    data = {}
    for _ in range(n):
        subject = input("Enter subject name: ")
        total = int(input(f"Enter total classes for {subject}: "))
        attended = int(input(f"Enter attended classes for {subject}: "))
        min_percentage = 75.0
        data[subject] = {'total': total, 'attended': attended, 'min_percentage': min_percentage}
    return data