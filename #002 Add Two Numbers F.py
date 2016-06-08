# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ln=l1
        lm=l2
        n=0
        m=0
        
        i_n=0
        while(ln!=None):
            n=n+ln.val*(10**i_n)
            i_n=i_n+1
            ln=ln.next
        
        i_m=0
        while(lm!=None):
            m=m+lm.val*(10**i_m)
            i_m=i_m+1
            lm=lm.next
            
        res=m+n
        
        res2=list(str(res))
        res3=list()
        l=len(res2)
        for i in range(l):
            num=int(res2[l-i-1])
            res3.append(num)
        return res3
        

# Method 2 
'''
https://code.csdn.net/snippets/608498#snippets608498
'''
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)
        cur = ret

        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            cur.val = sum % 10
            sum /= 10
            if l1 != None or l2 != None or sum != 0:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return ret
