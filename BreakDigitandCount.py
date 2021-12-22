#Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 
#Output : 7
#Code By : Dhavalsinh Patil


def DigitBreak(iValue):
    iCnt=-1
    while (iValue>0):
        iDigit = iValue%10
        iValue=int(iValue)/10
        iCnt=iCnt+1
    return iCnt

def main():
    no=0
    iRet=0
    print("Enter number :")
    no = int(input())
    iRet= DigitBreak(no)
    print("The Count of Digit Is :",iRet)

if _name=="main_":
    main()
