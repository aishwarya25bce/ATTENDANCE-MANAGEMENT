import display
import info
import prediction
import report
def main():
     print ("===ATTENDANCE MANAGER===")
     while True:
        print("\nMain Menu:")
        print("1. Check attendance for a particular subject")
        print("2. View overall attendance report")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            data = info.input_single_subject()
            while True:
                print("\nSubject Menu:")
                print("a. View Attendance Report")
                print("b. Predict Needed Classes to Attend")
                print("c. Back to Main Menu")
                sub_choice = input("Enter choice (a/b/c): ").lower()
                subject = list(data.keys())[0]
                if sub_choice == 'a':
                    display.view_attendance_report(subject, data)
                elif sub_choice == 'b':
                    prediction.predict_needed_classes(subject, data)
                elif sub_choice == 'c':
                    break
                else:
                    print("Invalid choice.")
        elif choice == '2':
            data = info.input_multiple_subjects()
            while True:
                report.overall_report(data)
                break
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main() 