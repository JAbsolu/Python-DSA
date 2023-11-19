'''
 Author: John Absolu
 CSC 212
 Programming Assignment: Project 6

 Program Description: A program to create a linkedlist that contains student information and their course registration records

 Challenges: Main problem was adding the courses to the correct student. I spent some time trying to get that done
 Datastructure used in this project are Classe, Linked list, Lists
''' 

'''
    Student record class
    def __init__ ------------ this line is the constructor whi takes, the parameter, self, name and courses with a default vaulue of null
    self.name = name -------- set name to equal the name passed as the argument when a new instance of studentRec is created
    self.courses = courses if courses else [] ------- This line uses ternary if else statement to find out if courses is not null upon
    the creation of a new StudentRec instance. If it's a null value, then set self.course to an empty list

    def set_name(self, name): ---------- setter function to set the name of a student
        self.name = name --------------- set the name to equal to the argument passed in the set method when its called

    def getName(self):  --------------- Set method to get the name of a student
        return self.name --------------- returns the name of a student

    def register(self, courses): ------- set method to set a student's courses
        self.courses = courses --------- set student courses to the courses' list passed in the argument of the method

    def __str__(self): ----------------- Method to print out the student's name and schedule in the terminal/shell
        return f"Name: {self.name} \n Schdedule: {''.join(self.courses)} " ------ returns student name and schedule as a string
'''

class StudentRec:
    def __init__(self, name, courses=None):
        self.name = name
        self.courses = courses if courses else [] #simple ternary if else statement

    def set_name(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getCourses(self):
        return self.courses

    def register(self, courses):
        self.courses = courses

    def __str__(self):
        return f"Name: {self.name}\nCourses: {self.courses}\n"


'''
    Node class
    Whenever this class is called, it creates a new istance of the Node class 
    which is added to the linked list.
    getData() returns the data in the node
    getNext() returns the value of the next node in the linked list
    setData() Adds the data passed as argument to the node when it's called
    setNext() Sets the next node in the list, takes a node as an argument
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, new_next):
        self.next = new_next


'''
    Ordered Linked List Class - An ordered linked list that add nodes to the list in order
    isEmpty() - Checks if the list is empty by returning a true or false boolean
    getLength() - Returns the length of the list, uses a counter that increment for every new node found
    addNode() - Adds a new node to the list in order
    deleteNode() - Deletes a node from the linked list
    printList() - Prints the list when called, uses while loop to traverse the list
    search() - Searches the list, uses parameters to determine which node to look for, uses a wile to 
    traverse the list and breaks out of the while loop when the node is found
'''

class OrderdLinkedList:
    def __init__(self):
        self.head = None
    '''
        Checks if Linkedlist is empty
    '''
    def isEmpty(self):
        return self.head == None
    '''
        Get length method
    '''
    def getLength(self):
        current = self.head
        length = 0

        while current != None:
            length += 1
            current = current.getNext()
        return length
    '''
        Add node method
    '''
    def addNode(self, item):
        new_node = Node(item)

        if not self.head or item.getName() < self.head.data.getName():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.getNext() and item.getName() > current.next.data.getName():
                current = current.next
            new_node.next = current.next
            current.next = new_node
    '''
        Delete node method
    '''
    def deleteNode(self, data):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.data == data: #same this as sayin current.getData()
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.next)
    '''
        print list method
    '''
    def printList(self):
        current = self.head

        while current:
            print(current.getData())
            current = current.getNext()
    '''
        Search method
    '''
    def search(self, name):
        current = self.head
        name = name.title()

        while current:
            if name in current.data.name or name == current.data.name and current.data.name.find(name):
                return current
                break
            current = current.getNext()


'''
    Create ordered list using names.txt
    studentsList - A new instance of the OrderedLinkedList saves as studentsList
    namesFile - The file to open and read
    next steps - Loop through the file
    name - selects the line and remove leading and trailing space, replaces the comma with a space
    new_student - create a new student record instance and pass the name as argument
    studentsList.addNode(new_student) - Get the previously created linked list, call the addNode method
    and pass our new student as an argument
    last line - closes  the file

'''

studentsList = OrderdLinkedList()
namesFile = open("names.txt", "r")

for student in namesFile:
    name = student.strip().replace(',', ' ')
    new_student = StudentRec(name)
    studentsList.addNode(new_student)
namesFile.close()


'''
    A few print tests
'''
print(f"Linked list data before registering students\n{'-'*60}")
studentsList.printList()



'''
    Get student course schedules from course.txt
    courseFiles - The file to open and read
    Next steps - loop the file and look at each line
    data - Contains the line read from the file, remove leading and trailing spaces and convert it to a list
    name -  Contains the first item in the list, which is the name. replace the comma to a space
    courses - Contains the remainder of the list starting from index 1
    student = Contains the result of the search. It will be a node if found, if not it will be null
    Next steps - Checks if a student is found, if yes. re call the register method and pass courses
'''

courseFiles = open("courses.txt", "r")

for line in courseFiles:
    data = line.strip().split()
    name = data[0].replace(',', ' ')
    courses = data[1:]
    student = studentsList.search(name)

    if student:
        student.data.register(courses)        

'''
    Print tests from the above block of code
    studentsList.printList() - Prints out the list to the terminal/shell
'''
print(f"\nLinked list data after registering students\n{'-'*60}")
studentsList.printList()




'''
    Deleting withdrawn student from the list
    withdrawal_list - Contains a list of student who request withdrawal
    For Loop - Loops throught he withdrawal list
    student_name - Contains the selection of each item in the list, replaces the comma to a space
    student - Contains the result of searching for the student

    Next steps - If the student is found, call the deleteNode method and delete the student. the student
    data is passed as the argument which will be used to delete the node
    studentsList.printList() - Prints the updated list each time a student is deleted
'''

print('-'*60)
withdrawal_list = ["Google,Lens", "Apple,Siri", "Amazon,Alexa"]

for student_name in withdrawal_list:
    student_name = student_name.replace(',', ' ')
    student = studentsList.search(student_name)

    if student:
        print(f"\n\n\nWithdrawing {student.data.name}\n{'='*60}\n")
        studentsList.deleteNode(student.data)

        print(F"UPDATED LIST AFTER DELETING STUDENT\n{'-'*60}")
        studentsList.printList()




'''
    Output Students planning on taking Math252 next term
    current - Contains the head of the studentList Linkedlist
    While loop - Loops as look as current is not null
    If Statement - Checks if a student is taking the course MAT252
    If yes, prints out the data and move the pointer to the next node.
'''

print(f"\n\n{'='*60}")
print('\nSTUDENTS TAKING MATH252\n')

current = studentsList.head

while current:
    if "MAT252" in current.data.courses: #same as writing current.getData().getCourses()
        print(current.getData())

    current = current.next

'''
    Print the length of the Linked List
'''
print(f"\n{'='*60}\nThe length of the Linked List: {studentsList.getLength()}\n\n")
