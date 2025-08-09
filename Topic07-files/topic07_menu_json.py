import json
FILENAME = "students.json"

def add_student(students):
    name = input("Student name: ")
    students.append(name)

def view_students(students):
    if not students:
        print("No students yet.")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")

def save_students(students):
    with open(FILENAME, "w") as f:
        json.dump(students, f)

def load_students():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def display_menu():
    print("\nWhat would you like to do?")
    print("(a) Add new student")
    print("(v) View students")
    print("(s) Save students")
    print("(l) Load students")
    print("(q) Quit")
    return input("Type one letter (a/v/s/l/q): ").strip().lower()

def main():
    students = []
    while True:
        choice = display_menu()
        if choice == "a":
            add_student(students)
        elif choice == "v":
            view_students(students)
        elif choice == "s":
            save_students(students)
        elif choice == "l":
            students = load_students()
            print(f"Loaded {len(students)} students.")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Please select either a, v, s, l, or q.")

if __name__ == "__main__":
    main()