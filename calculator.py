class Cal:
    def __init__(self):

        print("Enter the first number")
        self.a = input()
        while not self.a.isdigit():
            print("Enter digits as your input for first number")
            self.a = input()
        self.a = int(self.a)
        print("Enter the second number")
        self.b = input()
        while not self.b.isdigit():
            print("Enter digits as your input for first number")
            self.b = input()
        self.b = int(self.b)
        self.choice = 1

    def op(self):

        while self.choice != 0:
            print("0. Exit")
            print("1. Add")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. Exponent")
            print("7. Floor")

            self.choice = int(input("Enter choice: "))
            if self.choice == 1:
                print("Result: ", self.add())
            elif self.choice == 2:
                print("Result: ", self.sub())
            elif self.choice == 3:
                print("Result: ", self.mul())
            elif self.choice == 4:
                print("Result: ", round(self.div(), 2))
            elif self.choice == 5:
                print("Result: ", self.mod())
            elif self.choice == 6:
                print("Result: ", self.exp())
            elif self.choice == 7:
                print("Result: ", self.floor())

            elif self.choice == 0:
                print("Exiting!")
                self.choice
                ##break
                continue
            else:
                print("Invalid choice!!")

        else:
            return self.choice

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

    def mod(self):
        return self.a % self.b

    def floor(self):
        return self.a // self.b

    def exp(self):
        return self.a ** self.b