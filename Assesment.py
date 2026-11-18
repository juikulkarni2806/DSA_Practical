
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    # 1. Add Process
    def enqueue(self, pid, name, priority):
        new = Node(pid, name, priority)

        if self.front == None or priority < self.front.priority:
            new.next = self.front
            self.front = new
        else:
            temp = self.front

            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next

            new.next = temp.next
            temp.next = new

        print("Process Added")

    # 2. Execute Process
    def dequeue(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Executed Process:", temp.pid, temp.name)
            self.front = self.front.next

    # 3. View Next Process
    def display_next(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            print("Next Process:", self.front.pid,
                  self.front.name, self.front.priority)

    # 4. Display All Processes
    def display_all(self):
        if self.front == None:
            print("Queue is Empty")
            return

        temp = self.front

        while temp != None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next

    # 5. Count Processes
    def count(self):
        temp = self.front
        c = 0

        while temp != None:
            c = c + 1
            temp = temp.next

        print("Total Processes:", c)


# Main Program
pq = PriorityQueue()

pq.enqueue(101, "Chrome", 2)
pq.enqueue(102, "System", 1)
pq.enqueue(103, "Music", 3)
pq.enqueue(104, "Notepad", 4)

print("\nAll Processes:")
pq.display_all()

print("\nNext Process:")
pq.display_next()

print("\nExecute Process:")
pq.dequeue()

print("\nRemaining Processes:")
pq.display_all()

pq.count()
