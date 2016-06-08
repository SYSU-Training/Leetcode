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
    ListNode* deleteDuplicates(ListNode* head) {
        map <int,int> map;
        ListNode *first=new ListNode(0);
        first->next=head;
        while(first->next!=NULL){
            if(map.find(first->next->val)==map.end()){
                map[first->next->val]=0;
                first=first->next;
            }
            else {
                first->next=first->next->next;
            }
        }
        return head;
    }
};
