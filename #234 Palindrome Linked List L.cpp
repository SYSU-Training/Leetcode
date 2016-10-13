/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
    ListNode *q;
    ListNode *p;
    ListNode *newhead;
    p=head;
    q=head;
    if(head==NULL) return 1;
    while(q->next!=NULL)
    {
        p=p->next;
        q=q->next;
        if(q->next==NULL)
        break;
        q=q->next;
        
    }
    newhead=p;
    while(p!=q) 
    {
         newhead=newhead->next;
         p->next=q->next;
         q->next=p;
         p=newhead;
    }
    while(newhead!=NULL)
    {
       if(head->val!=newhead->val) return 0;
       head=head->next;
       newhead=newhead->next;
    }return 1;
}
};
