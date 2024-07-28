def fib(n):
    a,b = 0,1
    if n<=0 :
        print("Enter the positive value")
    elif n==1:
        print(a,end=" ")
    else :
        print(a,end=" ")
        print(b,end=" ")
        for  i in range(2,n):
            c=a+b
            print(c,end=" ")
            a,b=b,c

def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
    
        return 1 
    #f(n)=f(n-1)+f(n-2)
    else :
        return fibonaci(n-1) + fibonaci(n-2)

n=int(input("Enter the no. of terms uh want fibonadci series :"))
fibonacci_sequence = [fibonaci(i) for i in range(n)]
print(f"Fibonacci sequence with {n} is : {fib(n)}")
 
fib(n)



