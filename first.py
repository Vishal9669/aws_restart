f1=open('demo.txt','r')
print(f1.read())
f1.close()

f1=open('demo2.txt','w')
f1.write("This is demo2 file")
f1.close()