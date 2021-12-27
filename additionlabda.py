addition = lambda a,b: a+b

def main():
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the Second Number :"))

    add=addition(No1,No2)
    print("The Addition is", add)

if __name__=="__main__":
    main()
