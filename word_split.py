def count(s): 
    for str in s.split(): 
        s = "&".join(str) 
    return s 

# only gives the last word with & between characters, not the whole string with & between characters of each word
print(count("Python is fun to learn."))



#def count(s):
 #   return " ".join("&".join(word) for word in s.split())

#print(count("Python is fun to learn."))