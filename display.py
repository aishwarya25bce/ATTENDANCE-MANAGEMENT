
import matplotlib.pyplot as plt
def view_attendance_report(subject, data):
    info = data.get(subject)
    if not info:
        print(f"No data found for {subject}.")
        return
    total = info['total']
    attended = info['attended']
    perc = (attended / total) * 100 if total > 0 else 0
    status = "SAFE" if perc >= info['min_percentage'] else "RISK"
    print(f"\nAttendance Report for {subject}:")
    print(f"Attended Classes: {attended}")
    print(f"Total Classes: {total}")
    print(f"Attendance Percentage: {perc:.2f}%")
    print(f"Status: {status}")
    # Pie chart
    plt.figure(figsize=(5,5))
    labels = ['Attended', 'Missed']
    sizes = [attended, total - attended]
    colors = ['#4CAF50', '#FF6347']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f"Attendance for {subject}")
    plt.show()
