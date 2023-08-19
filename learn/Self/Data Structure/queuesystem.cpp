#include<stdlib.h>
#include<queue>
#include<iostream>
using namespace std;

void displayQueue(queue<string> q){
    while(!q.empty()){
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

int main(){
    queue<string> myqueue;

    myqueue.push("alamin");
    myqueue.push("jwel");
    myqueue.push("jasmin");
    myqueue.push("sultana");

    cout << "\nCurrent queue elements : ";
    displayQueue(myqueue);

    myqueue.pop();
    myqueue.pop();

    cout << "\nCurrent queue elements : ";
    displayQueue(myqueue);

    return 0;
}

