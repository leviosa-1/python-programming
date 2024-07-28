# use to open a file 
with open('File IO/sample.txt','r') as f :
    data=f.read()
print(data)

with open('File IO/sample.txt','a') as f :
    f.write("Ayush is very good boy")


