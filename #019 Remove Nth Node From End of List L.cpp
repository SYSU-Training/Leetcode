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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        if(head==NULL) return NULL;
        ListNode *p=head,*q=head,*m=0;
        for(int i=0;i<n-1;i++) q=q->next;
        while(q->next){
            m=p;
            p=p->next;
            q=q->next;
        }
        if(m==NULL){
            head=head->next;
            delete p;
        }
        else{
            m->next=p->next;
            delete p;
        }
        return head;
    }
};
