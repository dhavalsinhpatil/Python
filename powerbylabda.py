power= lambda a : 2**a

def main():
    no=int(input("Enter the number : "))
    
    ret=power(no)
    print("Power of entered number: ",ret)

if _name=="main_":
    main()
