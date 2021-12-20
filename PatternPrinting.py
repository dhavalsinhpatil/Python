#Pattern In Python
def Pattern(iValue):
    for i in range(iValue):
         for j in range(iValue+1):
            print("*",end=" ")
         print()

def main():
    no=0
    print("Enter the Number :")
    no=int(input())
    Pattern(no)

if _name=="main_":
    main()
