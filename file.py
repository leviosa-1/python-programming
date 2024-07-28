 
 #writing in file
s="Ayush is very good boy"
with open("test.txt" , "w") as f :
     f.write(s)


s2="\n pranjal meri bestii ha !"
with open("test.txt","a") as f :
    f.write(s2)
    
# read from File
with open("test.txt" , "r") as f :
    g=f.read()
    print("read in text format \n")
    print(g)

# read in binary form 
with open("test.txt", "rb") as f :
    a=f.read()
    print("Read in binary form \n")
    print(a)
    