from db import c, conn

"""
PK - Primary Key
"""


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    # Finding Employee to the DataBase With Specific ID
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def update(self):   # Updating DataBase with new Employees
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):   # Create employee function
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid
        conn.commit()  # Commit changes to the database after insertion

    def save(self):  # save employee to the database function
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    @classmethod
    # Get employees with different call option
    def get_employee_list(cls, columns=None):
        if columns is None:
            columns = ["name", "surname", "age", "id"]

        query = f"SELECT {', '.join(columns)} FROM employee"
        c.execute(query)

        employee_list = [tuple(row) for row in c.fetchall()]

        return employee_list

    def delete(self):  # Delete user from db function
        if self is not None:
            query = "DELETE FROM employee WHERE id = ?"
            c.execute(query, (self.id,))
            conn.commit()  # Commit changes to the database after deletion
        else:
            print("Cannot delete - Record does not exist in the database")

    # Overload min() and max() function
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.age < other.age
        return NotImplemented

    def __str__(self):
        return f"{self.name} {self.surname}, Age: {self.age}"
