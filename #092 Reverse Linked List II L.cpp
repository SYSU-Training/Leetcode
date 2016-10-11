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
    void reverse(ListNode *head) {
        if(head->next!=NULL){
        ListNode *p=NULL;
        while (head!=NULL) {
            ListNode *L=head->next;
            head->next=p;
            p=head;
            head=L;
        }
        }
    }
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        if(head==NULL) return NULL;
        if(head->next==NULL) return head;
        ListNode *first=new ListNode(-1);
        first->next=head;
        ListNode *p=first;
        for(int i=0;i<m-1;i++) p=p->next;
        ListNode *q=first;
        ListNode *begin = p->next;
        for (int i=0;i<n;i++) q=q->next;
        ListNode *end = q->next;
        q->next = NULL;
        reverse(begin);
        p->next=q;
        begin->next=end;
        return first->next;
    }
};
