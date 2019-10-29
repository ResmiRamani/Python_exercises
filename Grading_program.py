# Source:http://www.cplusplus.com/forum/articles/12974/
# Grading Program
# Write a program that allows the user to enter the grade scored in a programming class (0-100).
# If the user scored a 100 then notify the user that they got a perfect score.
#
# ★ Modify the program so that if the user scored a 90-100 it informs the user that they scored an A
#
# ★★ Modify the program so that it will notify the user of their letter grade
# 0-59 F 60-69 D 70-79 C 80-89 B 90-100 A

score = int(input("Enter a score between 0 and 100: "))
if score >= 90 and score <= 100:
	print("grade A")
elif score >= 80 and score <= 89:
	print("grade B")
elif score >= 70 and score <= 79:
	print("grade C")
elif score >= 60 and score <= 69:
	print("grade D")
else:
	print("grade F")
