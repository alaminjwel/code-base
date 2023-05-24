#include<iostream>
using namespace std;

class Node{
   public:

   int data;
   Node* next;

   Node(){
      data = 0;
      next = NULL;
   }
   Node (int data){
      this->data = data;
      this->next = NULL;
   }
};

class Linkedlist{
   Node* head;
   public:
   Linkedlist(){
      head = NULL;
   }

   void insertNode(int);
   void deleteNode(int);
   void printList();
};

void Linkedlist::insertNode(int data){
   Node* newNode = new Node(data);
   if(head == NULL) {
      head = newNode;
      return;
   }

   Node* cur = head;
   while(cur->next != NULL){
      cur = cur->next;
   }
   cur->next = newNode;
}

void Linkedlist::deleteNode(int index){
   int listLen = 0;
   Node* cur = head;
   Node* cur2 = NULL;
   if(head == NULL) {
      cout << "Failed to delete, list is empty." << endl;
      return;
   }
   while(cur->next != NULL){
      cur = cur->next;
      listLen++;
   }
   if(listLen<index){
      cout << "Index out of range, cant delete." << endl;
      return;
   }
   cur = head;
   if(index==1){
      head = head->next;
      delete cur;
      return;
   }
   while(index-- > 1){
      cur2 = cur;
      cur = cur->next;
   }
   cur2->next = cur->next;
   delete cur;

}

void Linkedlist::printList(){
   Node* cur = head;
   while(cur->next != NULL){
      cur = cur->next;
      cout << cur->data << " ";
   }
}

int main(){

   Linkedlist list;
   list.insertNode(1);
   list.insertNode(2);
   list.insertNode(3);
   list.insertNode(4);
   cout << "\nElements of the list are: ";
   list.printList();
   list.deleteNode(2);
   cout << "\nElements of the list are: ";
   list.printList();

   return 0;
}
