# put your python code here
student_marks = input()
count_space = student_marks.split(" ")
# print(count_space)
count_a = count_space.count("A")
# print(count_a)
percentage = count_a / len(count_space)
# print(percentage)
print(round(percentage, 2))