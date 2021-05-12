student_list = []

for x in range (10):
    student_score = int(input("Student score : "))
    student_list.append(student_score)

print("Students scores are : ", student_list)

count_one = 0
for i in student_list :
    if i > 0 and i < 11:
        count_one = count_one + 1

count_two = 0
for i in student_list :
    if i > 10 and i < 21:
        count_two = count_two + 1

count_three = 0
for i in student_list :
    if i > 20 and i < 31:
        count_three = count_three + 1

count_four = 0
for i in student_list :
    if i > 30 and i < 41:
        count_four = count_four + 1

count_five = 0
for i in student_list :
    if i > 40 and i < 51:
        count_five = count_five + 1

print("Scores 0 - 10 : ", count_one)
print("Scores 11 - 20 : ", count_two)
print("Scores 21 - 30 : ", count_three)
print("Scores 31 - 40 : ", count_four)
print("Scores 41 - 50 : ", count_five)
