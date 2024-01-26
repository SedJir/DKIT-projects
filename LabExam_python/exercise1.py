def most_grade(grade):
    # I am finding the most used grade
    max_counter = 0
    most_used_grade = 0
    # in the first loop I take the one number
    # in the second loop I checked that number with other number that are in the list
    for index in range(len(grade)):
        counter = 1
        for j in range(index + 1, len(grade)):
            if grade[index] == grade[j]:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            most_used_grade = grade[index]
    return most_used_grade


# reading file
student_textfile = open("student.txt", "r")

# create lists
student_filelist = []
student_name = []
student_grade = []

# storing file information into list
for i in student_textfile:
    student_filelist.append(i.strip().split("%%"))

student_textfile.close()

# export from list into student list and grade list 
student_name = []
student_grade = []
for i in student_filelist:
    student_name.append(i[0])
    student_grade.append(i[1])

# using function to get most used grade
student_most_used_grade = most_grade(student_grade)

print("Students with the most frequently appearing grade: \n")
# finding the student name with the most frequently appearing grade
for i in range(len(student_grade)):
    if student_grade[i] == student_most_used_grade:
        print(student_name[i])
        
        