import matplotlib.pyplot as plt
import display
import prediction
import main
def overall_report(data):
    while True:
        print("\nOverall Report Menu:")
        print("a. View attendance report for a subject")
       
        print("b. Show full report with bar graph")
        print("c. Predict classes for a subject")
        print("d. Back to Main Menu")
        choice = input("Enter choice (a/b/c/d): ").lower()
        if choice == 'a':
            subject = input("Enter subject name: ")
            display.view_attendance_report(subject, data)
        elif choice == 'b':
            print("\nFull Attendance Report:")
            print(f"{'Subject':<20}{'Attended':<10}{'Total':<10}{'Percentage':<12}")
            subjects = []
            percentages = []
            for sub, info in data.items():
                perc = (info['attended'] / info['total']) * 100 if info['total'] > 0 else 0
                print(f"{sub:<20}{info['attended']:<10}{info['total']:<10}{perc:<12.2f}")
                subjects.append(sub)
                percentages.append(perc)
            # Bar graph
            plt.figure(figsize=(10,5))
            plt.bar(subjects, percentages, color='#4CAF50')
            plt.axhline(y=75, color='r', linestyle='--', label="Minimum Required (75%)")
            plt.xlabel("Subjects")
            plt.ylabel("Attendance Percentage")
            plt.title("Overall Attendance Percentage per Subject")
            plt.legend()
            plt.show()
        elif choice == 'c':
            subject = input("Enter subject name: ")
            prediction.predict_needed_classes(subject, data)
        
        elif choice == 'd':
            print("Returning to Main Menu.")
            main.main()
        else:
            print("Invalid choice.")
            