f = open('MyData_for_FH', 'r')
# print(f.read())     # for read all the data
print(f.readline(),end="")     # print one line, end="" for not go for a new line
print(f.readline())

f1 = open('write_file_FH', 'w')
f1.write("Hi,good night\n")             # r is read ,w is written ,a is appended

f1 = open('write_file_FH', 'a')
f1.write("Have a sweet dream ")
for data in f:              # for copy Mydata all data in write file
    f1.write(data)

# f2 = open('picOfMy.jpg','rb')
# f3 = open('myPic.jpg', 'wb')         # for copy img into f3 file from f2 file
# for i in f2:
   # f3.write(i)