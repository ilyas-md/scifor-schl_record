while True:
    print("press n to create new file")
    print("press o to open a file")
    print("press d to delete file")
    a = input("TYPE HERE:")
    if a == "n":
        file_name = str(input("FILE NAME: "))
        stud = file_name

        def new_file():
            stud = {
                "name": str(input("ENTER STUDENT NAME: ")),
                "std": input("ENTER THE CLASS AND SECTION: "),
                "dob": input("ENTER DATE OF BIRTH: "),
                "place": str(input("ENTER THE PLACE: ")),
                "yoj": input("YEAR OF JOIN: "),
                "paid": input("FEE PAID: "),
                "due": input("AMOUNT TO BE PAID: ")
            }
            text_file = str(stud)
            file = open(file_name, "w")
            file.write(text_file)
            file.close()
            print("CREATED SUCCESSFULLY!")
        new_file()
    elif a == "o":
        open_file = str(input("OPEN FILE: "))
        file = open(open_file, "r")
        print(file.read())
        file.close()
    elif a == "d":
        delete_file = str(input("DELETE FILE: "))
        del delete_file
