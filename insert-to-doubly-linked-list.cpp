#include <iostream>

/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as*/
struct Node{
  int data;
  Node *next;
  Node *prev;
};

using namespace std;

Node* SortedInsert(Node* head, int data)
{
    Node* temp = new Node;
    temp->data = data;

    // empty list
    if (head == NULL){
        head = temp;
        temp->next = NULL;
        temp->prev = NULL;
    }

    // insert at head
    else if (data <= head->data){
      // pointers inside new node
      temp->next = head;
      temp->prev = NULL;
      
      // set pointers to new node
      head->prev = temp;  // old head
      head = temp;        // new head
    }
    else{
      Node* curr = head;
      
      while (curr != NULL){

        // insert node at the end or in between
        if (curr->next == NULL || \
          ((curr->data <= data) && (data <= curr->next->data))){
          // pointers inside new node
          temp->next = curr->next;
          temp->prev = curr;

          // set pointers to new node
          if (curr->next != NULL) // if not at the end of the list
            curr->next->prev = temp;
          curr->next = temp;
          return head;
        }
        
        curr = curr->next;
      }

    }

    return head;
}

void printList(Node* head){
  if (head != NULL){
    cout << head->data << endl;
    printList(head->next);
  }
}

int main(){
  Node* head = NULL;
  
  head = SortedInsert(head, 5);
  head = SortedInsert(head, 2);
  head = SortedInsert(head, 6);
  head = SortedInsert(head, 0);
  
  printList(head);
  cout << "goodbye" << endl;
}
