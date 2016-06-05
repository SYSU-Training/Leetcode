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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *first=new ListNode(0);
        ListNode *l=first;
        while(l1&&l2){
            if(l1->val<l2->val){
                l->next=l1;
                l1=l1->next;
            }
            else {
                l->next=l2;
                l2=l2->next;
            }
            l=l->next;
        }
        if(l1){
            l->next=l1;
            l1=l1->next;
        }
        if(l2){
            l->next=l2;
            l2=l2->next;
        }
        return first->next;
    }
};
