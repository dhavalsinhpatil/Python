#Accept Two Number and Perform the Addition
#Code By : Dhavalsinh Patil
def Addition(iValue1,iValue2):
    result=0
    result= iValue1+iValue2
    return result
  
def main():
    no1=0
    no2=0
    ret=0
    print("Enter the Value 1 :")
    no1 = int(input())

    print("Enter the Value 2 :")
    no2 = int(input())
    ret=a.Addition(no1,no2)
    print("Addition is :",ret)

if __name__=="__main__":
    main()
