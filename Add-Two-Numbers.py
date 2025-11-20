# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head node to make it easy to build results list
        dummy = ListNode()
        outputNode = dummy #This will move along the result list

        #Variables to walk through two linked lists
        currentNode = l1
        compareNode = l2

        #Keeps track of any carry over for next sum
        carryOver = 0

        #Keep looping as long as there are nodes left in l1, l2 or there is a non-zero CarryOver
        while currentNode or compareNode or carryOver:
            cv = currentNode.val if currentNode else 0 #if current node exists, use its value, otherwise 0
            cp = compareNode.val if compareNode else 0 #if compare node exists, use its value, otherwise 0
            total = cv + cp + carryOver # Add both node values together plus any carry over
            carryOver = total // 10 #take the first digit to carry over
            digit = total % 10 #take the final digit to carry over
            outputNode.next = ListNode(digit) #add new node with the digit and attach to results list
            outputNode = outputNode.next #move output node list forward
            if currentNode:
                currentNode = currentNode.next
            if compareNode:
                compareNode = compareNode.next
        return dummy.next