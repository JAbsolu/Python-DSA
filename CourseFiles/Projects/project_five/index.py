
'''
 Author: John Absolu
 CSC 212
 Programming Assignment: Project 5

 Program Description: This program builds a queue as an abstract data type to simulate and study
 the wait time and service time at a bank over a half-hour period.
 Datastructure used in this project are Queue, and class
''' 

import random

'''
    class Customer:  ---------------------> Creates the Customer class
    def __init__(self): ------------------> Creates the constructor, 
    self refers to the current instance of class

    self.name = name ---------------------> Assigns the value of the name parameter passed 
    when creating a Customer object to the name attribute of that specific Customer instance.

    self.arrival_time = arrival_time -----> Assigns the value of the arrival_time parameter passed 
    when creating a Customer object to the arrival_time attribute of that specific Customer instance.

    self.service_time = None -------------> Assigns the value of the service_time parameter passed 
    when creating a Customer to null by default.


    self.waiting_time = None -------------> Assigns the value of the waiting_time parameter passed 
    when creating a Customer to null by default.
'''

class Customer:
    def __init__(self, name, arrival_time):
        self.name = name
        self.arrival_time = arrival_time
        self.service_time = None
        self.wait_time = None

'''
    class BankQueue: ---------------> Creates the class BankQueue
    def __init__(self): ------------> Creates the constructor, 
    self refers to the current instance of class

    self.queue = [] ----------------> Creates the default value of the queue, an empty list

    def is_empty(self): -------------> Creates a method to check if the queue is empty
    return len(self.queue) == 0 ----> Returns True or False based on the size of the queue

    def size(self): ----------------> Creates a method to check the size of the queue
    return len(self.queue) ---------> returns the length of the queue (size)

    def enqueue(self, item): -------> Creates a method to add a customer to the end of the queue
    self.queue.append(customer) ----> Adds the customer to the end of the queue

    def dequeue(self): -------------> Creates a method to remove customer in the begining of the queue
    self.queue.pop(0) ---------------> Removes the first item in the queue (in FIFO order)
'''

class BankQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

'''
def simulate_bank_queue(): -------------> Creates function 
    bank_queue = BankQueue() -----------> Creates a new istance of BankQueue as bank_queue
    total_wait_time = 0 ----------------> Sets total wait time to 0 as default
    total_service_time = 0 -------------> Sets total service time to 0 as default
    remaining_customers = [] -----------> An empty list to hold remaining customers from the queue

    for minute , cust_number in enumurate(range(30)): ---------------> A for loop with two steppers that will loop 30 times
        if random.randint(0, 1) == 1:    ----------------------------> Checks for a random num between 1 and 0, if it's 1, proceed to next line
            customer = Customer(f'Customer {minute}', minute) -------> Create a new istance of the Customer class
            bank_queue.enqueue(customer) ----------------------------> Adds the new customer to the queue

        if not bank_queue.is_empty(): -------------------------------> Checks if the queue is not empty
            current_customer = bank_queue.dequeue() -----------------> Remove a customer at the begining of the queue, save it as vurrent_customer
            current_customer.arrival_time = random.randint(minute, 30) --------> Sets the arrival time for the current customer
            current_customer.service_time = random.randint(1, 10) -------------> Sets the current customer's service time to a random integer between 1 to 10
            current_customer.wait_time = current_customer.arrival_time - minute ------------> Sets the wait time to be arrival time minus the minute from the loop

            total_wait_time += current_customer.wait_time ----------------------------------> Increments the total wait time by wait time
            total_service_time += current_customer.service_time ----------------------------> Increments the total service time by service time

            print(f'{current_customer.name} - Wait Time: {current_customer.wait_time} minutes, Service Time: {current_customer.service_time} minutes')

    while not bank_queue.is_empty(): --------------------------------------> Loops while the bank queue is not empty
        remaining_customers.append(bank_queue.dequeue()) ------------------> Adds the removed customer to the remaining cust list

    avg_wait_time = total_wait_time / 30  ---------------------------------> Calclulates the average wait time
    avg_service_time = total_service_time / 30 ----------------------------> Calculate the avg service time

    return avg_wait_time, avg_service_time, remaining_customers -----------> Returns the following
'''

def simulate_bank_queue():
    bank_queue = BankQueue()
    total_wait_time = 0
    total_service_time = 0
    remaining_customers = []

    for minute, cust_number in enumerate(range(30)):
        if random.randint(0, 1) == 1:
            customer = Customer(f'Customer {cust_number}', minute)
            bank_queue.enqueue(customer)

        if not bank_queue.is_empty():
            current_customer = bank_queue.dequeue()
            current_customer.arrival_time = random.randint(minute, 30)
            current_customer.service_time = random.randint(1, 10)
            current_customer.wait_time = current_customer.arrival_time - minute

            total_wait_time += current_customer.wait_time
            total_service_time += current_customer.service_time

            print(f'{current_customer.name} - Wait Time: {current_customer.wait_time} minutes Later, Service Time: {current_customer.service_time} minutes')

    while not bank_queue.is_empty():
        remaining_customers.append(bank_queue.dequeue())

    avg_wait_time = total_wait_time / 30
    avg_service_time = total_service_time / 30

    return avg_wait_time, avg_service_time, remaining_customers

if __name__ == "__main__":
    avg_wait_time, avg_service_time, remaining_customers = simulate_bank_queue()

    print(f'\nAverage Wait Time: {avg_wait_time} minutes')
    print(f'Average Service Time: {avg_service_time} minutes')

    if remaining_customers:
        print(f'\n{len(remaining_customers)} customer(s) still waiting:')
        for customer in remaining_customers:
            print(f'{customer.name} - Wait Time: {customer.wait_time} minutes (Arrival Time till End)')
