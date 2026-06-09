"r"(read)
"w"(write)
"a"(append)

w(mode)
file = open("my_dairytext","w")
file.write("hello python! this is my first file")
file.close()


r(mode)
file = open("my_dairy.text","r")
content = file.read()
print(content)
file.close()

with ka use
with open ("my_dairy.text","r") as file:
  print(file.read())










