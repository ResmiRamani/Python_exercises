score = int(input("Enter a score between 0 and 100: "))
if score>=90 and score<=100:
    print("grade A")
elif score>=80 and score<=89:
    print("grade B")
elif score>=70 and score<=79:
    print("grade C")
elif score>=60 and score<=69:
    print("grade D")
else:
    print("grade F")