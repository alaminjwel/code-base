#include<stdlib.h>
#include<iostream>

using namespace std;

#define MAX 10

int stackSize = 0;


struct stack {
	int top;
	int items[MAX];
};
typedef struct stack st;

void createEmptyStarck(st *s){
	s->top = -1;
}

bool isEmpty(st *s){
	return s->top==-1;
}

bool isFull(st *s){
    return s->top==MAX-1;
}

void push(st *s,int newitem){
	if(isFull(s)) cout << "\nStack is full, failed to push : " << newitem << endl;
	else{
		s->top++;
		s->items[s->top] = newitem;
		stackSize++;
		cout << "\nPushed " << s->items[s->top] << " to stack\n";
	}
}

void pop(st *s){
	if(isEmpty(s)) cout << "\nStack is empty, failed to pop \n";
	else{
		cout << "\nPoped " << s->items[s->top] << " from stack\n";
		s->top--;
		stackSize--;
	}
}


void printStack(st *s) {
	if(isEmpty(s)) cout << "\nStack is empty, nothign to display \n";
	else{		
		printf("\nCurrent Stack: ");
		for (int i = 0; i < stackSize; i++) {
		  cout << s->items[i] << " ";
		}
		cout << endl;
	}
}

int main(){
	st *s = (st *)malloc(sizeof(st));
	createEmptyStarck(s);

	push(s,1);
	push(s,2);
	push(s,3);
	push(s,4);
	push(s,5);
	push(s,6);
	push(s,7);
	push(s,8);
	push(s,9);
	push(s,10);
	push(s,11);
	push(s,11);
	push(s,11);
	push(s,11);
	push(s,11);

	printStack(s);

	pop(s);
	pop(s);
	pop(s);
	push(s,11);
	push(s,11);
	push(s,11);
	push(s,11);
	push(s,11);
	push(s,11);

	printStack(s);
}
