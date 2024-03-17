from employee import Employee
from db import conn

try:
    add_user_input = input("Would you like to add Employee to DataBase? \"yes or no\": ")
    if add_user_input == "yes":
        while True:
            user_input = input("Enter values to db \"name, surname, age\": ")
            if user_input:
                name, surname, age = user_input.split(", ")

                # Create and save Employee object
                new_employee = Employee(name, surname, age)
                print("Adding new employee:",
                      new_employee)  # Add this line to check if the employee is created correctly
                new_employee.save()
                print("Employee added successfully")  # Add this line to check if the save operation is successful
            user_exit = input("Would you like to finish adding users to database: \"yes or no\"? ")
            if user_exit == "yes":
                break
            else:
                continue
    else:
        # Filter Employee with Different option from db
        user_input_to_filter_data = input(
            "How  do you like to filter DataBase? \"With id?, name?, surname?, or with age\": ")
        if user_input_to_filter_data == "id" or 'name' or 'surname' or 'age':
            employees = Employee.get_employee_list([user_input_to_filter_data])
            print(employees)  # here we can check that our users really exit to db and filtered with input data

        # Delete Employee from Database
        user_input_to_delete_data = input("Would you like to Delete Employee from DataBase? \"yes or no\"? ")
        if user_input_to_delete_data == "yes":
            print("Choose how you want to identify to delete employee")
            print("1. By ID")
            print("2. By Name")
            print("3. By Surname")
            print("4. By Age")

            choice = input("Enter your choice (1, 2, 3 or 4): ")
            # Get the data based on Employees choice
            if choice == "1":
                identifier = int(input("Enter the employee ID: "))
                employees = Employee.get_employee_list(["id", "name", "surname", "age"])
                identifier_index = 0  # ID is at index 0
            elif choice == "2":
                identifier = input("Enter the employee name: ")
                employees = Employee.get_employee_list(["id", "name", "surname", "age"])
                identifier_index = 1  # Name is at index 1
            elif choice == "3":
                identifier = input("Enter the employee surname: ")
                employees = Employee.get_employee_list(["id", "name", "surname", "age"])
                identifier_index = 2  # Surname is at index 2
            elif choice == "4":
                identifier = int(input("Enter the employee Age: "))
                employees = Employee.get_employee_list(["id", "name", "surname", "age"])
                identifier_index = 3  # Age is at index 3
            else:
                print("Invalid choice.")
                exit()  # Exit the program if the choice is invalid

            # Find the employee with the specified identifier
            employee_to_delete = None
            for employee in employees:
                if employee[identifier_index] == identifier:
                    employee_to_delete = Employee.get(employee[0])  # Get employee by ID
                    break

            if employee_to_delete:
                employee_to_delete.delete()
                print(f"Employee with {choice} '{identifier}' deleted successfully.")
            else:
                print("Employee not found.")
        else:
            print("No data will be deleted.")

            # Find the oldest and youngest employees
            oldest_employee = max(employees)
            youngest_employee = min(employees)

            print("Oldest employee:")
            print(oldest_employee)

            print("\nYoungest employee:")
            print(youngest_employee)

            conn.commit()
finally:
    conn.close()
