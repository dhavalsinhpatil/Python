#PYTHON List PROGRAM 
# Input : Size =5  (1,2,3,4,5)
# Entered Data is : [1, 2, 3, 4, 5]
#Code By : Dhavalsinh Patil


def main():
    size=0
    i=0
    Data= []
    
    print("How Many elements do you want to enter : ")
    size = int(input())
    
    print("Enter the elements :")
    for i in range (size):
        Data.append(int(input()))
    
    print("Entered Data is :", Data)

if __name__=="__main__":
    main()
