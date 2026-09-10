name = input("What's your name? ")
score = int(input("What's your score (0-100)? "))

if score >= 90:
    grade = "Eccelent"
elif score >= 80:
    grade = "Good"
elif score >= 70:
    grade = "Average"
elif score >= 60:
    grade = "Pass"
else:
    grade = "Fail"

print("")
print("====== RESULT ======")
print("Name:", name)
print("Score:", score)
print("Grade:", grade)

if grade == "Fail":
    print("You need to retake the exam")
else:
    print("Congratulations, you passed!")