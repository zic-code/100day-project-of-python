student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)


print(max(student_scores))
highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print( highest_score)