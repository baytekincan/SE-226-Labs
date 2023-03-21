#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node *next;
};

class Queue {
private:
    Node *front;
    Node *rear;
    int count;
public:
    Queue() {
        front = nullptr;
        rear = nullptr;
        count = 0;
    }

    void enqueue(int data) {
        Node *newNode = new Node();
        newNode->data = data;
        newNode->next = nullptr;
        if (front == nullptr && rear == nullptr) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        } else if (front == rear) {
            front = rear = nullptr;
        } else {
            Node *temp = front;
            front = front->next;
            delete temp;
        }
        count--;
    }

    int top() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return -1;
        }
        return front->data;
    }

    bool isEmpty() {
        return (front == nullptr && rear == nullptr);
    }

    [[nodiscard]] int size() const {
        return count;
    }
};

int main() {
    Queue q;

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(6);
    q.enqueue(7);
    q.enqueue(8);

    cout << "Top element: " << q.top() << endl;
    cout << "Size of queue: " << q.size() << endl;
    cout << "isEmpty: " << q.isEmpty() << endl;

    cout << "" << endl;

    cout << "Removing an item from the queue..." << endl;
    cout << "" << endl;
    q.dequeue();

    cout << "Top element: " << q.top() << endl;
    cout << "Size of queue: " << q.size() << endl;
    cout << "isEmpty: " << q.isEmpty();

    return 0;
}