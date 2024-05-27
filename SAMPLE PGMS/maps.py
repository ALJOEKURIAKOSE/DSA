
values = input()
phone_book = {}
for i in range(int(values)):
 name_and_phone = input()

 spiltvalue = name_and_phone.split(' ')
 name = spiltvalue[0]
 phonenum = spiltvalue[1]
 phone_book[name] = phonenum

lines = []
while True:
   line = input().strip()
   if line.lower() == "":
        break
   lines.append(line)
#  nametocheck = input("Enter your name:")
for line in lines:
 if (line in phone_book):
  print(line + "="+ phone_book[line] )
else:
  print("Not found")  

