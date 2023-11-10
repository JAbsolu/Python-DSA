class Employee:

  def __init__(self, ID, name, dept):
    self.__id = ID
    self.__name = name
    self.__dept = dept

  def set_id(self, ID):
    self.__ID = ID

  def set_name(self, name):
    self.__name = name

  def set_dept(self, dept):
    self.__dept = dept

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_dept(self):
    return self.__dept


# EMployee List
employee_list = []


# Create employees
def create_employee():
  for i in range(2):
    emp_id = i  #make the index the id so i can have unique ids automatically
    emp_name = input("Enter employee name: ")
    emp_dept = input("Enter employee dept: ")

    new_employee = Employee(emp_id, emp_name, emp_dept)
    employee_list.append(new_employee)

    print(f"The new employee's name is: {emp_name}")
    print(f"The new eployee's ID is: {emp_id}")
    print(f"The new employee's department is: {emp_dept}\n")


#Invoke the create emp function
create_employee()

# Create dictionary of employees
employee_dict = {}


def add_to_dictionary(arr):
  for emp in arr:
    print(emp)
    employee_dict[emp.get_id()] = emp


#invoke dictionary function
add_to_dictionary(employee_list)

# Print the dictionary to see result
print(employee_dict)
print(f"{'*' * 50} \n")
john = Employee(1, "John", "Sales")
john.set_name("Jack")
print("Manually created employee ", john.get_name())

if __name__ == "__Employee__":
  Employee()

if __name__ == "__create_employee__":
  create_employee()
