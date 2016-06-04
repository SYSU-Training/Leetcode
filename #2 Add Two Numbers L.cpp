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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *first=new ListNode(0);
        ListNode *l=first;
        int val=0;
        while(1){
            if(l1!=NULL) {val=val+l1->val;l1=l1->next;}
            if(l2!=NULL) {val=val+l2->val;l2=l2->next;}
            l->val=val%10;
            val=val/10;
            if(l1!=NULL||l2!=NULL||val!=0)
            {
            l->next=new ListNode(0);
            l=l->next;}
            else break;
        }
        return first;
    }
};
