import abc

# Define the abstract base class Person
class Person(abc.ABC):
    """
    Abstract base class for a person.
    """
    def __init__(self, name: str, age: int):
        """
        Initializes a Person object.
        """
        self.name = name
        self.age = age

    @abc.abstractmethod
    def display_details(self):
        pass

# Define the Parent subclass
class Parent(Person):
    def __init__(self, name: str, age: int, children_names: list[str]):
        super().__init__(name, age)
        self.children_names = children_names

    def display_details(self):
        
        print(f"--- Parent Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Children: {', '.join(self.children_names)}")
        print("-" * 25)

# Define the Student subclass
class Student(Person):
    
    def __init__(self, name: str, age: int, student_id: str, major: str):
       
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def display_details(self):
       
        print(f"--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("-" * 25)

# Define the Lecturer subclass
class Lecturer(Person):
   
    def __init__(self, name: str, age: int, employee_id: str, department: str):
       
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        
        print(f"--- Lecturer Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print("-" * 25)

# Define the Staff subclass
class Staff(Person):
    def __init__(self, name: str, age: int, employee_id: str, role: str):
       
        super().__init__(name, age)
        self.employee_id = employee_id
        self.role = role

    def display_details(self):
       
        print(f"--- Staff Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Role: {self.role}")
        print("-" * 25)

# --- Program Execution ---
if __name__ == "__main__":
    print("Creating single instances of each subclass and displaying their details:\n")

   
    parent_instance = Parent("oyenyboth", 42, ["joseph", "Oscar"])
    parent_instance.display_details()

    # Create a single instance of Student
    student_instance = Student("Mugisa Joseph", 22, "S1001", "Software Engineering")
    student_instance.display_details()

    # Create a single instance of Lecturer
    lecturer_instance = Lecturer("Dr. Emily White", 55, "L5005", "Physics")
    lecturer_instance.display_details()

    # Create a single instance of Staff
    staff_instance = Staff("Ayebale Christine", 30, "ST2020", "Administrative Assistant")
    staff_instance.display_details()

    print("\nAll details displayed.")
