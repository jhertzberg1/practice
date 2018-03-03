from sys import argv
# read the WYSS section for how to run this
script, one, two, three = argv

# script arguements modified from book, same result just different argument names

age = input("how old are you? ")
gender = input("whats your sex? ")
origin = input("where are you from? ")


print("A/S/L", script)
print({age}, one)
print({gender}, two)
print({origin}, three)
