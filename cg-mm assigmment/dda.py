import matplotlib.pyplot as plt
x1=int(input("Enter X1"))
y1=int(input("Enter y1 "))
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))

dx=x2-x1
dy=y2-y1

if (abs(dx)>abs(dy)):
    steps=abs(dx)
else:
    steps=abs(dy)

xincr=dx/steps
yincr=dy/steps

xcoor=[]
ycoor=[]
i=0 
while i< steps:
    i+=1
    x1+=xincr
    y1+=yincr
    print("X1:",x1, "Y1:",y1)
    xcoor.append(x1)
    ycoor.append(y2)
    
plt.plot(xcoor,ycoor)

plt.xlabel("X-axis")
plt.ylabel("y-axis")

plt.title("DDA Algorithm")
plt.show()
