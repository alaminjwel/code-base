#include<stdlib.h>
#include<iostream>

using namespace std;

#define MAX 10

struct queue {
	int front;
	int rear;
	int items[MAX];
};
typedef struct queue qu;

void createEmptyQueue(qu *q){
	q->front=-1;
	q->rear=-1;
}

bool isEmpty(qu *q){
	return q->front==-1;
}

bool isFull(qu *q){
	return q->rear==MAX-1;
}

void enQueue(qu *q,int newitem){
    if(isFull(q)) cout << "\nQueue is full, failed to enqueue " << newitem <<endl;
    else {
        if(q->front==-1) q->front++;
        q->rear++;
        q->items[q->rear] = newitem;
        cout << "\nEnQueued " << q->items[q->rear] << " to queue\n";
    }

}

void deQueue(qu *q){
	if(isEmpty(q)) cout << "\nQueue is empty, failed to deQueue \n";
	else {
		cout << "\nDeQueued " << q->items[q->front] << " from queue\n";
		// queue only has one element, reset queue after dequeue
		if (q->front >= q->rear) createEmptyQueue(q);
		else  q->front++;

	}
}

void peek(qu *q){
	if(isEmpty(q)) cout << "\nQueue is empty, nothing to peek \n";
	else cout << "\nPeeked and found " << q->items[q->front] << " in the queue\n";
}

void printQueue(qu *q){
	if(isEmpty(q)) cout << "\nQueue is empty, nothing to display\n";
	else{
		printf("\nCurrent Queue: ");

		for(int i=q->front;i<=q->rear;i++){
			cout << q->items[i] << " ";
		}
		cout << endl;
	}
}

int main(){
	qu *q = (qu *)malloc(sizeof(qu));
	createEmptyQueue(q);

	enQueue(q,1);
	enQueue(q,2);
	enQueue(q,3);
	enQueue(q,4);
	enQueue(q,5);
	enQueue(q,6);
	enQueue(q,7);
	enQueue(q,8);
	enQueue(q,9);
	enQueue(q,9);
	enQueue(q,9);
	enQueue(q,9);

	printQueue(q);


	deQueue(q);
	peek(q);
	deQueue(q);
	deQueue(q);
	enQueue(q,10);
	enQueue(q,11);
	enQueue(q,12);
	enQueue(q,13);

	printQueue(q);

}
