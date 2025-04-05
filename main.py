#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Timetable Generator

This program generates an optimal weekly timetable for a school based on 
classes, subjects, teachers, and period requirements.
"""
import random

### DO NOT MODIFY THE CODE BELOW THIS LINE ###

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
    # Initialize an empty timetable
    timetable = {day: {period: {} for period in range(1, periods_per_day + 1)} for day in days_of_week}
    
    # TODO: Implement the timetable generation algorithm
    # 1. Check if a valid timetable is possible with the given constraints
    # 2. Assign subjects and teachers to periods for each class
    # 3. Ensure all constraints are satisfied

    """ """
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            for class_name in classes:
                subject = random.choice(subjects)
                teacher = random.choice([t for t in teachers if subject in teachers[t]])
                
                if class_subject_periods[class_name][subject] > 0:
                    timetable[day][period][class_name] = (subject, teacher)
                    class_subject_periods[class_name][subject] -= 1
                else:
                    continue
    
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
    
    # Format: {day: {period: {class: (subject, teacher)}}}

    for day, periods in timetable.items():
        print(f"{day}:")
        for period, classes in periods.items():
            print(f"  Period {period}:")
            for class_name, (subject, teacher) in classes.items():
                print(f"    {class_name}: {subject} ({teacher})")

        print("")  


    pass


def validate_timetable(timetable):
    """
    Validate that the generated timetable meets all constraints.
    
    Args:
        timetable (dict): The generated timetable
        
    Returns:
        bool: True if timetable is valid, False otherwise
        str: Error message if timetable is invalid
    """
    actual_periods = {class_name: {subject: 0 for subject in subjects} for class_name in classes}
    
    for day in days_of_week:
        for period in range(1, periods_per_day + 1):
            # Check for double-booked teachers
            teachers_this_period = {}
            
            for class_name, (subject, teacher) in timetable[day][period].items():
                # Count periods for validation
                actual_periods[class_name][subject] += 1
                
                # Check teacher qualification
                if subject not in teachers[teacher]:
                    return False, f"Teacher {teacher} is not qualified to teach {subject}"
                
                # Check for teacher double-booking
                if teacher in teachers_this_period:
                    other_class = teachers_this_period[teacher]
                    return False, f"Teacher {teacher} is double-booked in {day}, period {period} for classes {class_name} and {other_class}"
                
                teachers_this_period[teacher] = class_name
    
    # Check if all required periods are scheduled
    for class_name in classes:
        for subject, required_periods in class_subject_periods[class_name].items():
            if actual_periods[class_name][subject] < required_periods:
                return False
            elif actual_periods[class_name][subject] > required_periods:
                return False
    
    return True, "Timetable is valid"


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
