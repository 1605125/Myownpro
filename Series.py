class Series:
    def __init__(self):

        self.n = int(input("enter the value of n"))
        self.choice = 1
        while self.choice != 0:
            print("0. Exit")
            print("1. square star pattern")
            print("2. left right triangle pattern")
            print("3. right right triangle pattern")
            print("4. equilateral triangle pattern")
            print("5. number right triangle pattern")
            print("6. alphabet right triangle pattern")
            self.choice = int(input("Enter choice: "))
            if self.choice == 1:
                print(self.series1())
            elif self.choice == 2:
                print(self.series2())
            elif self.choice == 3:
                print(self.series3())
            elif self.choice == 4:
                print(self.series4())
            elif self.choice == 5:
                print(self.series5())
            elif self.choice == 6:
                print(self.series6())

            elif self.choice == 0:
                print("Exiting!")
                self.choice
                continue
            else:
                print("Invalid choice!!")
        else:
            self.choice

    def series1(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                print("*", end=' ')

    def series2(self):
        for i in range(0, self.n):
            for j in range(0, i+1):
                print("*", end=' ')
            print()

    def series3(self):
        for i in range(0, self.n):
            for k in range(0, self.n - i):
                print(" ", end=" ")
            for j in range(0, i + 1):
                print("*", end=' ')
            print()

    def series4(self):
        for i in range(0, self.n):
            for k in range(0, self.n - i):
                print(" ", end="")
            for j in range(0, i + 1):
                print("*", end=' ')
            print()

    def series5(self):
        for i in range(0, self.n + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()

    def series6(self):
        for i in range(0, self.n):
            for j in range(65, 65 + i + 1):
                print(chr(j), end=' ')
            print()

