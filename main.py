#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Timetable Generator

This program generates an optimal weekly timetable for a school based on 
classes, subjects, teachers, and period requirements.
"""

### DO NOT MODIFY THE CODE BELOW THIS LINE ###


import random
from collections import defaultdict

# Define the input constraints
# Classes
classes = ["Class 6A", "Class 6B", "Class 7A", "Class 7B"]

# Subjects
subjects = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "Physical Education"]

# Weekly period requirements for each class and subject
# {class_name: {subject_name: number_of_periods_per_week}}
class_subject_periods = {
    "Class 6A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 6B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 3, "Physical Education": 3},
    "Class 7A": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2},
    "Class 7B": {"Mathematics": 6, "Science": 6, "English": 6, "Social Studies": 6, "Computer Science": 4, "Physical Education": 2}
}

# Teachers and their teaching capabilities
# {teacher_name: [list_of_subjects_they_can_teach]}
teachers = {
    "Mr. Kumar": ["Mathematics"],
    "Mrs. Sharma": ["Mathematics"],
    "Ms. Gupta": ["Science"],
    "Mr. Singh": ["Science", "Social Studies"],
    "Mrs. Patel": ["English"],
    "Mr. Joshi": ["English", "Social Studies"],
    "Mr. Malhotra": ["Computer Science"],
    "Mr. Chauhan": ["Physical Education"]
}

# School timing configuration
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 6

### DO NOT MODIFY THE CODE ABOVE THIS LINE ###

def generate_timetable():
    """
    Generate a weekly timetable for the school based on the given constraints.
    
    Returns:
        dict: A data structure representing the complete timetable
              Format: {day: {period: {class: (subject, teacher)}}}
    """
    # # Initialize an empty timetable
    # timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    
    # TODO: Implement the timetable generation algorithm
    # 1. Check if a valid timetable is possible with the given constraints
    # 2. Assign subjects and teachers to periods for each class
    # 3. Ensure all constraints are satisfied
    while True:
        timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
        class_subject_pool = {}

        for cls in classes:
            pool = []
            for subject, count in class_subject_periods[cls].items():
                eligible_teachers = [t for t, sub in teachers.items() if subject in sub]
                for _ in range(count):
                    teacher = random.choice(eligible_teachers)
                    pool.append((subject, teacher))
            random.shuffle(pool)
            class_subject_pool[cls] = pool

        for day in days_of_week:
            used_teachers = {period: set() for period in range(1, periods_per_day + 1)}
            for period in range(1, periods_per_day + 1):
                for cls in classes:
                    assigned = False
                    for idx, (subject, teacher) in enumerate(class_subject_pool[cls]):
                        if teacher not in used_teachers[period]:
                            timetable[day][period][cls] = (subject, teacher)
                            used_teachers[period].add(teacher)
                            class_subject_pool[cls].pop(idx)
                            assigned = True
                            break
                    if not assigned:
                        timetable[day][period][cls] = ("Free", "None")

        is_valid, msg = validate_timetable(timetable)
        if is_valid:
            return timetable
 
    


def display_timetable(timetable):
    """
    Display the generated timetable in a readable format.
    
    Args:
        timetable (dict): The generated timetable
    """
    # TODO: Implement timetable display logic
    # Display the timetable for each class
    # Display the timetable for each teacher
    for cls in classes:
        print(f"\nTimetable for {cls}")
        print("-" * 40)
        for day in days_of_week:
            print(f"\n{day}:")
            for period in range(1, periods_per_day + 1):
                subject, teacher = timetable[day][period].get(cls, ("Free", "None"))
                print(f"  Period {period}: {subject} ({teacher})")




def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    # TODO: Implement validation logic
    # Check if all classes have their required number of periods for each subject
    # Check if teachers are not double-booked
    # Check if teachers are only teaching subjects they can teach
    
    class_period_counter = defaultdict(lambda: defaultdict(int))
    teacher_assigned = {day: {period: set() for period in range(1, periods_per_day + 1)} for day in days_of_week}

    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for cls, (subject, teacher) in timetable[day][period].items():
                if subject == "Free":
                    continue
                class_period_counter[cls][subject] += 1

                if teacher in teacher_assigned[day][period]:
                    return False, f"{teacher} is double-booked on {day}, period {period}"
                teacher_assigned[day][period].add(teacher)

                if subject not in teachers.get(teacher, []):
                    return False, f"{teacher} cannot teach {subject} to {cls} on {day} period {period}"

    for cls, subjects_needed in class_subject_periods.items():
        for subject, required in subjects_needed.items():
            actual = class_period_counter[cls][subject]
            if actual != required:
                return False, f"{cls} has {actual}/{required} periods of {subject}"

    return True, "OK"

def main():
    """
    Main function to generate and display the timetable.
    """
    print("Generating school timetable...")
    
    # Generate the timetable
    timetable = generate_timetable()
    
    # Validate the timetable
    is_valid, message = validate_timetable(timetable)
    
    if is_valid:
        # Display the timetable
        display_timetable(timetable)
    else:
        print(f"Failed to generate valid timetable: {message}")


if __name__ == "__main__":
    main()