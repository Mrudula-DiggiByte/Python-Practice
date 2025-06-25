str1 = "This is a string.\t   we are creating it in python."
print(str1)

str1 = "apna"
str2 = "college"
print(str1+str2)
print(len(str1))
print(len(str2))


# #Negative Index
s="apple"
print(s[-3:-1])

#String Functions
st= "i am studying python from ApnaCollege"
print(st.endswith("ege"))
print(st.endswith("at"))
print(st.capitalize())
print(st.replace("o","a"))
print(st.replace("python","javascript"))
print(st.find("o"))
print(st.find("from"))
print(st.find("Q"))


#WAP to input user's first name and print its length
string= input("Enter your name")
print(len(string))

#WAP to find the occurrence of $ in a string
a="Hi I am $,Nice to meet u $"
print(a.count("$"))