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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL) return NULL;
        ListNode *first=new ListNode(0);
        first->next=head;
        ListNode *tmp=head;
        int len=1;
        while(tmp->next){
            tmp=tmp->next;
            len++;
        }
        k=k%len;
        if(k==0) return head;
        for(int i=0;i<len-k-1;i++){
            head=head->next;
        }
        ListNode *newhead=head->next;
        head->next=NULL;
        tmp->next=first->next;
        return newhead;
    }
};
