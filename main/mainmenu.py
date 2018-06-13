from calculator import Cal
from Series import Series
choice = 0
print(end='')


class MENU:

    def menu(self):
        print("*******MENU*******")
        print(" 1.CALCULATOR")
        print(" 2.SERIES")
        print(" 3.SORTING THE DETAILS")
        print(" 4.EXIT")
        print("  ENTER YOUR CHOICE")

    def main(self):
        choice = 1
        while choice != 4:
            choice = int(input())
            if choice == 1:
                cal = Cal()
                cal.op()
                print("--------------")
                print(cal.choice)
                if cal.choice == 0:
                    self.menu()
            elif choice == 2:
                ser = Series()
                print("--------------")
                if ser.choice == 0:
                    self.menu()
            else:
                break
            #
            # elif choice == 3:
            #
            # elif choice == 4:


obj = MENU()
obj.menu()
obj.main()