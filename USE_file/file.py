file = open("file_test.txt", "a+")


while True:

    line = input("Enter your desired text: ")

    if line == "SAVE":
        file.close()
        file = open("file_test.txt", "a+")
    elif line == "CLOSE":
        file.close()
        break
    else: 
        file.write(line + "\n")