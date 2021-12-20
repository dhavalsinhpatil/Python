#Write a program which accept one number and display below pattern. 
#Input : 5 
#Output : 
 # * * * * * 
 # * * * * 
 # * * * 
 # * * 
 # *
 #####################################################################
def Pattern(value):
    for i in range(value,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\n")
def main():
    print("Enter the number : ")
    no = int(input())
    Pattern(no)
if _name_ == "_main_":
    main()
