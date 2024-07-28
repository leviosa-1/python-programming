# WAP to read a Twinkel poem and find Twinkel in the poem

with open('File IO\poem.txt','r') as f :
    text=f.read()
    if 'Twinkle' in text :
        print("Twinkle is present in File")
    else :
        print("Twinkel is not present in file")