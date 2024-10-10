class CustomStack:
    def __init__(self):
        self.text = ""
        self.history = []

    def insert(self, value):
        self.history.append(('insert', len(value)))
        self.text += value

    def delete(self, value):
        removed = self.text[-value:]
        self.text = self.text[:-value]
        self.history.append(('delete', removed))

    def get(self, value):
        return self.text[value - 1]

    def undo(self):
        if not self.history:
            return
        last_operation, value = self.history.pop()
        if last_operation == 'insert':
            self.text = self.text[:-value]
        elif last_operation == 'delete':
            self.text += value

def process_commands(input_commands):
    stack = CustomStack()
    commands = input_commands.split(',')
    output = []
    for command in commands:
        if command[0] == '1':
            stack.insert(command[2:])
        elif command[0] == '2':
            stack.delete(int(command[2:]))
        elif command[0] == '3':
            output.append(stack.get(int(command[2:])))
        elif command[0] == '4':
            stack.undo()
    return output

input_commands = input("Enter commands: ")
output = process_commands(input_commands)
print('\n'.join(output))
