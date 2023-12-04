import random

'''

 Author: John Absolu
 CSC 212
 Programming Assignment: Project 7
 Program Description: This program is a sorting algorithm that sort a list based on smaller to larger values.
 Challenges: No challenges.
 Datastructure used in this project: A List is used in this project. The list is mutated to sort it's items from smallest to largest.

'''


def select_sort(a_list):
    for i in range(len(a_list)):
        min = i
        for j in range(i + 1, len(a_list)):
            if a_list[i] > a_list[j]:
                temp = a_list[min]
                a_list[i] = a_list[j]
                a_list[j] = temp
    return a_list

print(f"\n{'-' * 95}")

testCases = [[random.randint(1,100) for i in range(15)], [10,9,8,7,6,5,4,3,2,1], ['P','Y','T','H','O','N']]

for test in testCases:
    print("\nOriginal list:", test)
    print(f"Sorted List: {select_sort(test)}\n")
    print(f"{'-' * 95}\n")


'''

Code Explaination

The selection sor algorithm works by using a two pointer system.
1. The first pointer is stored in a variable. The value in this pointer is assumed to be the min value in the list
at this point.

2. The second pointer then keeps incremeting, searching for a value lower than the value at the index stored in min.

3. An if statement is used to compare each new value seen at moving pointer (index j in the nested loop) in the list to the current min. 
If a value lower than the min value is found.

4. A new variarable is created to save the temporary minimum value at index min.

5. Perform a variable swap and swap the value of index i (the assumed min) to the value at index j (The new minimum value found).

6. This step repeats until index i reach the end of the list, sorting the whole list.

'''

'''
Big O Notation

The time complexity of this algorithm is Big O(n^2), because there is a nested loop of 2.
As one loop runs, it must waits for its nested loop to finish before it can move to its next iteration, slowing down the time.

The best case scenario for this algorithm would be in a case when the list is already sorted, however the 
algorithm still need to check all elements in the list in the inner loop, which would still make the time O(n^2).

The worst case is when the list is in reverse order and the minimum value is always found at the end of the list.
But the time complexity would still be Big O(n^2) as the inner loop always travers the whole list.

'''