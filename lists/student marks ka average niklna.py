# Empty list to store marks
marks = []

# Taking number of subjects
n = int(input("Enter number of subjects: "))

# Taking marks input and adding into list
for i in range(n):
    score = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(score)

# Print list of marks
print("Marks List =", marks)

# Calculate average
average = sum(marks) / len(marks)

print("Average Marks =", average)

