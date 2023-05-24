#include<stdlib.h>
#include<iostream>

using namespace std;

#define MAX 10

class Queue
{
	private:
	int front,rear,items[MAX];

	public:
	Queue(){
		front = rear = -1;
	}

	bool isEmpty(){
		return front==-1;
	}

	bool isFull(){
		if (front == 0 && rear == MAX - 1) {
          return true;
        }
        if (front == rear + 1) {
          return true;
        }
        return false;
	}

	void enQueue(int newitem){
	    if(isFull()) cout << "\nQueue is full, failed to enqueue " << newitem <<endl;
	    else {
	        if(front==-1) front++;
	        rear=(rear+1)%MAX;
	        items[rear] = newitem;
	        cout << "\nEnQueued " << items[rear] << " to queue\n";
	    }

	}

	void deQueue(){
		if(isEmpty()) cout << "\nQueue is empty, failed to deQueue \n";
		else {
			cout << "\nDeQueued " << items[front] << " from queue\n";
			// queue only has one element, reset queue after dequeue
			if (front >= rear) front = rear = -1;
			else front=(front+1)%MAX;
		}
	}

	void peek(){
		if(isEmpty()) cout << "\nQueue is empty, nothing to peek \n";
		else cout << "\nPeeked and found " << items[front] << " in the queue\n";
	}

	void printQueue(){
		if(isEmpty()) cout << "\nQueue is empty, nothing to display\n";
		else{
			printf("\nCurrent Queue: ");

			for(int i=front;i!=rear;i=(i+1)%MAX){
				cout << items[i] << " ";
			}
			cout << endl;
		}
	}

};



int main(){
	Queue q;

	q.enQueue(1);
	q.enQueue(2);
	q.enQueue(3);
	q.enQueue(4);
	q.enQueue(5);
	q.enQueue(6);
	q.enQueue(7);
	q.enQueue(8);
	q.enQueue(9);
	q.enQueue(9);
	q.enQueue(9);
	q.enQueue(9);

	q.printQueue();


	q.deQueue();
	q.peek();
	q.deQueue();
	q.deQueue();
	q.enQueue(10);
	q.enQueue(11);
	q.enQueue(12);
	q.enQueue(13);

	q.printQueue();

}
