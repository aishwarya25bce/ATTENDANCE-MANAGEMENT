import matplotlib.pyplot as plt
def predict_needed_classes(subject, data):
    info = data.get(subject)
    if not info:
        print(f"No data for {subject}")
        return
    total = info['total']
    attended = info['attended']
    min_perc = info['min_percentage']
    print("\nPrediction Options:")
    print("1. Classes needed to attend to meet requirement")
    print("2. Classes can skip and still meet requirement")
    choice = input("Enter choice (1 or 2): ")
    if choice == '1':
        remaining = int(input("Enter number of remaining classes: "))
        target_ratio = min_perc / 100
        needed = 0
        while needed <= remaining:
            if (attended + needed) / (total + remaining) >= target_ratio:
                break
            needed += 1
        if needed > remaining:
            print("Not possible to reach minimum attendance even if all remaining classes are attended.")
        else:
            print(f"You need to attend at least {needed} out of {remaining} remaining classes.")
    elif choice == '2':
        max_skips = 0
        while max_skips <= total - attended:
            if attended / (total - max_skips) < (min_perc / 100):
                break
            max_skips += 1
        max_skips -= 1
        print(f"You can skip up to {max_skips} classes and still maintain minimum attendance.")
    else:
        print("Invalid choice.")