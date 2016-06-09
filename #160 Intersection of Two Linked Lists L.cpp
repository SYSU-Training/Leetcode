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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA==NULL||headB==NULL) return NULL;
        ListNode *L1=headA;
        ListNode *L2=headB;
        int l1=0,l2=0;
        while(L1){
            L1=L1->next;
            l1++;
        }
        while(L2){
            L2=L2->next;
            l2++;
        }
        if(l1<l2){
            for(int i=0;i<l2-l1;i++){
                headB=headB->next;
            }
        }
        else if(l1>l2){
            for(int i=0;i<l1-l2;i++){
                headA=headA->next;
            }
        }
        while(headA!=headB){
            headA=headA->next;
            headB=headB->next;
        }
        return headA;
    }
};
