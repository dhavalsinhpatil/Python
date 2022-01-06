def multiplication(value):
    mult=1
    for i in range(len(value)):
        mult=mult*value[i]
    return mult

def addition(value1):
    add=0
    for i in range(len(value1)):
        add=add+value1[i]
    return add
def main():
    data=[5,3,8,2]
    
    mult=multiplication(data)
    
    add=addition(data)
    
    ret=mult-add
    print("Ans is: ",ret)
    
if _name=="main_":
  main()
