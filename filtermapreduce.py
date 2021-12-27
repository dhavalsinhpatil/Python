from functools import reduce

red= lambda a,b : a*b
maps= lambda a : a + 10
filt= lambda a : a>=70 and a<=90

def lists(val):
    nos=int(input("Enter no of  element  which you wants :"))
    for i in range(nos):
        no=int(input("Enter the element :"))
        val.append(no)
    return val
def main():
    data=[]
    
    ret=lists(data)
    print("You entered list is: ",ret)
    #filter
    result=list(filter(filt,ret))
    print("Filtered list : ",result)
    #maps
    result1=list(map(maps,result))
    print("After Mapping : ",result1)
    #reduce
    result2=reduce(red,result1)
    print("After  reduce : ",result2)
if _name=="main_":
    main()
