file = read = open("Codingal_txt.txt", "r")
print( file.read())
file.close()

file = open("Codingal_txt.txt", "r")
print("\n read in parts\n")
print( file.read(8))
file.close()

file = open("Codingal_txt.txt", "a")
print (file.write("Hi iam a cat "))
file.close()

