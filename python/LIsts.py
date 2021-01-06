class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        temp = Node(data)#call a new empty node with data and address as null
        if head is None:#check if this is the first node if yes it means copy the data part in the head and return it
            head = temp
            return head
        current_pos=head #else take the a variable current_post and point it to head
        while current_pos.next is not None:#travel through the list untill the last node of the list
            current_pos = current_pos.next#move your temporaray current position to last node
        current_pos.next=temp#in the last node copy the address of the newly created data
        return head#return the head first
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);