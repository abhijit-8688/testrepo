def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
s = "JavaTpoint"  
  
print ("The original string is : ",s)   
print ("The reversed string using reversed() is : ",reverse(s) )  