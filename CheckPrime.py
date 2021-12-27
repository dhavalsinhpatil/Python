def Prime(a):
    flag=False
    for j in range(2, int(a/2) + 1):  
        if (a % j) == 0:  
            flag=True
            break

    if(flag==False):
        print(a, "is a prime number")  
    else:        
        print(a, "is a Not prime number") 


def main():
    no=0
    no=int(input("Enter the number :"))
    
    ret=Prime(no)

if __name__=="__main__":
    main()
