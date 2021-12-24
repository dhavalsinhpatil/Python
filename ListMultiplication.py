def ListMultiplication(iList):
    sum=1
    for i in range(len(iList)):
        sum =sum*iList[i]
    return sum

def List(iValue):
    myList = []
    print("Enter The Elements :")
    for i in range(iValue):
        myList.append(int(input()))

    iRet = ListMultiplication(myList)
    print("The Multiplication of List :",iRet)

def main():
    print("Enter the Total number of List :")
    N= int(input())
    List(N)
    
if __name__ == "__main__":
    main()
