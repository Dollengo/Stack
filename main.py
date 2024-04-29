import time

class StaticStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, element):
        if self.top == self.size - 1:
            print("The stack is full. Cannot insert more elements.")
            time.sleep(1)
        else:
            self.top += 1
            self.stack[self.top] = element
            print("")
            print(f"Element {element} pushed onto the stack.")

    def pop(self):
        if self.top == -1:
            print("The stack is empty. No elements to pop.")
            time.sleep(1)
        else:
            popped_element = self.stack[self.top]
            self.top -= 1
            print(f"Element {popped_element} popped from the stack.")
            time.sleep(1)

    def display_elements(self):
        if self.top == -1:
            print("The stack is empty.")
            time.sleep(1)
        else:
            print("Elements of the stack:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
                time.sleep(1)

if __name__ == "__main__":
    stack_size = int(input("Enter the size of the stack: "))
    stack = StaticStack(stack_size)

    while True:
        print("\nMenu:")
        print("1 - Push")
        print("2 - Pop")
        print("3 - Display Stack Elements")
        print("4 - Exit")

        option = input("Choose an option: ")
        print(" ")

        if option == "1":
            element = input("Enter the element to push: ")
            stack.push(element)
        elif option == "2":
            stack.pop()
        elif option == "3":
            stack.display_elements()
        elif option == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Choose a valid option.")
