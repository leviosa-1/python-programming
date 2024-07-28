# for checking num is rime or not
def is_prime (num):
    if num<2 :
        return False
    for i in range(2,num+1):
        if num%2==0:
            return False
    else:
        return True

# find prime number under user defined limit !!
def print_prime(limit):
    for i in range(2,limit+1):
        if is_prime(i):
            print(i,end=" ")
        

limit=int(input('ENter limit'))
print_prime(limit)
