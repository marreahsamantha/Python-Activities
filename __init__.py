def create_file():
    try:
        file = open("diary.txt", "x")
        print(" Personal Diary file created successfully!")
        file.close()
    except FileExistsError:
        print(" Personal Diary file already exists.")

def write_entry():
    try:
        date = input("Enter date: ")
        entry = input("Write your diary entry: ")

        file = open("diary.txt", "w")
        file.write(f"[{date}] {entry}\n")
        file.close()

        print(" Diary entry saved successfully!")
    except Exception as e:
        print("Error writing entry:", e)

create_file()
write_entry()
