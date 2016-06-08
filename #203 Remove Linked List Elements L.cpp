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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *first=new ListNode(0);
        first->next=head;
        ListNode *p=first;
        ListNode *q=head;
        while(q!=NULL){
            if(q->val==val){
                q=q->next;
                p->next=q;
            }
            else {
                p=q;
                q=q->next;
            }
        }
        return first->next;
    }
};
