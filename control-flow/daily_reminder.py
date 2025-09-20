# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"'{task}' is a LOW priority task."
    case _:
        reminder = f"'{task}' has an UNKNOWN priority level."

# Add time-bound check
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print final reminder
print("\nReminder:", reminder)
