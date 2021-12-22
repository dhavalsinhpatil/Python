#Code By : Dhavalsinh Patil

def ChkPrime(List):
    for i in range(0,len(List)):
        No= List[i]
        if No>1:
            prime=True
            for j in range(2, int(No/2)+1):
                if No%j==0:
                    prime=False
                    break
            if prime==True:
                print(No)            

def main():
    size=0
    Data= []
    
    print("How Many elements do you want to enter : ")
    size = int(input())
    
    print("Enter the elements :")
    for i in range (size):
        Data.append(int(input()))
    
    print("Entered Data is :", Data)

    ChkPrime(Data)

if __name__=="__main__":
    main()
