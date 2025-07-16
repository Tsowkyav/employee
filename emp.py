def add_employee():
    name = input("Enter employee name: ")
    id = input("Enter id  number: ")
    data = []

    # Enter marks for 3 subjects
    for i in range(3):
        data= input(f"Enter data for employee {i + 1}: ")
    

    print("employee record added successfully!\n")


def display_employee():
    print("\nemployee Records:")
    try:
        with open("employee.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return

            for line in lines:
                data = line.strip().split(",")
                print(f"ID: {data[0]}, Name: {data[1]}, "
                      f"data: [{data[2]}, {data[3]}, {data[4]}], "
                      f"Total: {data[5]}, Average: {data[6]}")
    except FileNotFoundError:
        print("No records found. Please add employee first.")


def main():
    while True:
        print("\nemployee data Management System")
        print("1. Add employee")
        print("2. Display All employee")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employee()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
