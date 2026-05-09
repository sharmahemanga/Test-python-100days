# This script to identify the highest score in a list of student scores and print it out. It initializes the highest score to 0 and iterates through each score in the list, updating the highest score whenever it finds a score that is greater than the current highest score. Finally, it prints out the highest score found in the class.

student_scores = [78, 65, 89, 86, 55, 91, 64, 89,99, 53, 78, 97, 82, 88, 94, 77,100, 85, 91, 90, 89]
highest_score = 0
total_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
    else:
        highest_score
print(f"The highest score in the class is: {highest_score}")

# Use the max function to identify the highest score in the list of student scores and print it out. The max function takes an iterable as an argument and returns the largest item in that iterable. In this case, we pass the list of student scores to the max function, which returns the highest score in the class.

max_score = max(student_scores)
print(f"The highest score in the class is: {max_score}")

    