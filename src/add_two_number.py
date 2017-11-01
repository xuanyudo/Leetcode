# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = []
        arr2 = []
        ans = []
        while l1.next!=None:
            arr1.append(l1.val)
            l1 = l1.next
        arr1.append(l1.val)
        
        while l2.next!=None:
            arr2.append(l2.val)
            l2 = l2.next
        arr2.append(l2.val)
        carry = 0
        while len(arr1)!=0 or len(arr2)!=0:
            val1 = 0
            val2 = 0
            if len(arr1)!=0:
                val1 = arr1.pop(0)
            if len(arr2)!=0:
                val2 = arr2.pop(0)
            val3 = val1+val2+carry
            print(val3)
            if val3>=10:
                val3 -=10
                carry = 1
            else:
                carry = 0
            ans.append(val3)
        if carry:
            ans.append(carry)
            
        return ans