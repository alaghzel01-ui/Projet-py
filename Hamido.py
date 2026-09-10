name = input("What's your name? ")
age = input("How old are you? ")
city = input("Which city are you from? ")
hobby = input("What's your favorite hobby? ")

print("")
print("🌟====== BIO CARD ======🌟")
print("👤 Name:", name)
print("🎂 Age:", age)
print("🌍 City:", city)
print("⚽ Hobby:", hobby)
print("✨=======================✨")

name = input("What's your name? ")
score = int(input("What's your score (0-100)? "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("")
print("====== RESULT ======")
print("Name:", name)
print("Score:", score)
print("Grade:", grade)

if grade == "F":
    print("You need to retake the exam")
else:
    print("Congratulations, you passed!")