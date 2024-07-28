def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)


word1=input('Enter the first word : ')
word2=input("Enter second word : ")


if are_anagrams(word1,word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")