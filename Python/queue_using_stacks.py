class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

def process_queries(queries):
    queue = Queue()
    for query in queries:
        if query[0] == 1:
            queue.enqueue(query[1])
        elif query[0] == 2:
            queue.dequeue()
        elif query[0] == 3:
            print(queue.print_front())

input_string = input()
input_list = input_string.split(',')
queries = []
for item in input_list:
    query = item.split()
    queries.append((int(query[0]), int(query[1])) if len(query) > 1 else (int(query[0]),))

process_queries(queries)