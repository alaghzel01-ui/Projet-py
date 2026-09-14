file = open("notes.txt", "a")
file.write("This is a new line added later!\n")
file.close()

file = open("notes.txt", "r")
content = file.read()
file.close()

print("File content:")
print(content)