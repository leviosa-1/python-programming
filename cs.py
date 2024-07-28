qty=int(input("Enter the quantity"))
if qty<=2 :
    print("Qty cost : INR ",qty*20)
elif qty >=3 and qty<6 :
    print("qty cost : INR ",qty*18)
elif qty>=6 and qty<10 :
    print("qty cost : INR ",qty*15)
else :
    print("qty cost : INR ",qty*10)
    
    