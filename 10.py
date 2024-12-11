class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue
    
    def enqueue(self, value):
        # Add element to the end of the list
        self.queue.append(value)
        print(f"After enqueue {value}: {self.queue}")
    
    def dequeue(self):
        # Check if the queue is not empty
        if len(self.queue) > 0:
            removed = self.queue.pop(0)  # Remove and return the first element
            print(f"After dequeue: {self.queue}")
        else:
            print("Queue is empty")  # Print message if the queue is empty

# Function to process commands
def process_commands(commands):
    queue = Queue()
    for command in commands:
        if command.startswith("enqueue"):
            # Extract the number from the command and call enqueue
            value = int(command.split()[1])
            queue.enqueue(value)
        elif command == "dequeue":
            queue.dequeue()

# Example commands
commands = ["enqueue 5", "enqueue 10", "dequeue", "enqueue 15"]
process_commands(commands)
