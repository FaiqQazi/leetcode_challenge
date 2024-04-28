
// // //   struct ListNode {
// // //       int val;
// // //       ListNode *next;
// // //       ListNode() : val(0), next(nullptr) {}
// // //       ListNode(int x) : val(x), next(nullptr) {}
// // //       ListNode(int x, ListNode *next) : val(x), next(next) {}
// // //   };
 
// // class Solution {
// // public:
// // //  int lengthOfLinkedList(ListNode* head) {
// // //         int length = 0;
// // //         ListNode* current = head;
// // //         while (current != nullptr) {
// // //             cout<<"current head val"<<endl;
// // //             cout<<head->val<<endl;
// // //             length++;
// // //             current = current->next;
// // //         }
// // //         return length;
// // //     }
// // int lengthOfLinkedList(ListNode * head){
// //      ListNode* currentt = head;
     

// //      int len=0;
// //     while (currentt != nullptr) {
// //         cout<<"in lenght thhe head is "<<endl;
// //      cout<<currentt->val<<endl;
// //         std::cout << currentt->val << " ";
// //         currentt = currentt->next; 
// //         len++;

// //     }
// //     std::cout << std::endl;
// //     return len;
// // }
// //     void printLinkedList(ListNode* head) {
// //     ListNode* ccurrent = head;
// //     while (ccurrent != nullptr) {
// //         std::cout << ccurrent->val << " ";
// //         ccurrent = ccurrent->next;
// //     }
// //     std::cout << std::endl;
// // }
// //     ListNode *reverselist(ListNode *head)
// //     {
// //         ListNode * rev=head;
// //         ListNode * prev=nullptr;
// //         ListNode * curr=rev;
// //         ListNode * next;
// //         while(curr!=nullptr){
// //             next=curr->next;
// //             curr->next=prev;
// //             prev=curr;
// //             curr=next;
// //         }
// //         return prev;
// //     }
// //     void reorderList(ListNode* head) {
// //         //first we will reverse list 
// //         ListNode * revhead=nullptr;
// //         revhead=reverselist(head);
// //         cout<<"the reverse list is "<<endl;
// //         printLinkedList(revhead);
// //         cout<<"len of rev"<<endl;
// //         int bb=lengthOfLinkedList(revhead);
// //         cout<<bb<<endl;
// //         // iterating one by one over both 
// //         ListNode* thehead=nullptr;
// //         ListNode * newhead=thehead;

// //         int i=0;
// //         int num=lengthOfLinkedList(head);
// //         cout<<"the num is "<<endl;
// //         cout<<num<<endl;
// //         while(i<=num){
// // if(i%2==0){
// //     newhead=head;
// //     cout<<"headval"<<endl;
// //     cout<<head->val<<endl;
// //     head=head->next;
// //     newhead=newhead->next;
// //     i++;
// // }
// // else if(1%2==1){
// //     newhead=revhead;
// //     cout<<"revhead val"<<endl;
// //     cout<<revhead->val<<endl;
// //     revhead=revhead->next;
// //     newhead=newhead->next;
// //     i++;
// // }
// //         }
// //         cout<<"printing the linked list"<<endl;

// //         printLinkedList(thehead);
// //         head= thehead;
// //     }
// // };
// #include <iostream>

// using namespace std;

// // struct ListNode {
// //     int val;
// //     ListNode *next;
// //     ListNode() : val(0), next(nullptr) {}
// //     ListNode(int x) : val(x), next(nullptr) {}
// //     ListNode(int x, ListNode *next) : val(x), next(next) {}
// // };

// class Solution {
// public:
//     int lengthOfLinkedList(ListNode *head) {
//         ListNode* currentt = head;
//         int len = 0;
//         while (currentt != nullptr) {
//             len++;
//             currentt = currentt->next; 
//         }
//         currentt=nullptr;
//         return len;
//     }

//     void printLinkedList(ListNode* head) {
//         ListNode* current = head;
//         while (current != nullptr) {
//             cout << current->val << " ";
//             current = current->next;
//         }
//         current=nullptr;
//         cout << endl;
//     }

//     ListNode *reverselist(ListNode *head) {
//         ListNode *rev = nullptr;
//         ListNode *prev = nullptr;
//         ListNode *curr = head;
//         ListNode *next;
//         while(curr != nullptr){
//             next = curr->next;
//             curr->next = prev;
//             prev = curr;
//             curr = next;
//         }
//         return prev;
//     }

//     // void reorderList(ListNode* head) {
//     //             int num = lengthOfLinkedList(head);
                
//     //     ListNode *revhead = reverselist(head);
//     //     cout << "Reversed List: ";
//     //     printLinkedList(revhead);
//     //     cout << "Length of reversed list: " << lengthOfLinkedList(revhead) << endl;

//     //     ListNode* newhead = nullptr;
//     //     int i = 0;
//     //     cout << "Length of original list: " << num << endl;

//     //     while (i < num) {
//     //         if (i % 2 == 0) {
//     //             // cout << "Original head val: " << head->val << endl;
//     //             // newhead=head;
//     //             cout<<head->val<<" ";
//     //             head = head->next;
//     //             cout<<head->val<<" ";
//     //             // newhead = newhead->next;
//     //             i++;
//     //         } else {
//     //             // newhead = revhead;
//     //             // cout << "Reversed head val: " << revhead->val << endl;
//     //             cout<<revhead->val<<" ";
//     //             revhead = revhead->next;
//     //             cout<<revhead->val<<" ";
//     //             // newhead = newhead->next;
//     //             i++;
//     //         }
//     //     }

//     //     cout << "Reordered List: ";
//     //     printLinkedList(newhead);
//     // }
// //     void reorderList(ListNode* head) {
//    void reorderList(ListNode* head) {
//     int num = lengthOfLinkedList(head);
//     cout << "Length of original list: " << num << endl;
//     ListNode* revhead = reverselist(head);
//     cout << "Reversed List: ";
//     printLinkedList(revhead);

//     int i = 0;

//     ListNode* currentHead = head;
//     ListNode* currentRevhead = revhead;

//     while (i < num) {
//         if (i % 2 == 0) {
//             ListNode* temp = currentHead->next;
//             currentHead->next = currentRevhead;
//             currentHead = temp;
//         } else {
//             ListNode* temp = currentRevhead->next;
//             currentRevhead->next = currentHead;
//             currentRevhead = temp;
//         }
//         i++;
//     }

//     // Set the next of the last node to NULL to avoid cycles in the list
//     if (currentHead)
//         currentHead->next = nullptr;

//     cout << "Reordered List: ";
//     printLinkedList(head);
// }


// };

// // int main() {
// //     ListNode* n1 = new ListNode(1);
// //     ListNode* n2 = new ListNode(2);
// //     ListNode* n3 = new ListNode(3);
// //     ListNode* n4 = new ListNode(4);
// //     n1->next = n2;
// //     n2->next = n3;
// //     n3->next = n4;

// //     Solution sol;
// //     cout << "Original List: ";
// //     sol.printLinkedList(n1);

// //     cout << "Reorder Result: ";
// //     sol.reorderList(n1);

// //     return 0;
// // }
class Solution {
public:
void reorderList(ListNode* head) {
    if (!head || !head->next) return;

    // Step 1: Find the middle of the list
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Split the list into two halves
    ListNode *second_half = slow->next;
    slow->next = nullptr;

    // Step 2: Reverse the second half of the list
    ListNode *prev = nullptr;
    while (second_half) {
        ListNode *temp = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = temp;
    }

    // Step 3: Merge the two halves alternatively
    ListNode *first_half = head;
    while (prev) {
        ListNode *temp1 = first_half->next;
        ListNode *temp2 = prev->next;
        first_half->next = prev;
        prev->next = temp1;
        first_half = temp1;
        prev = temp2;
    }
}
};