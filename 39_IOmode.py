f=open('2_heloworld.py','r')
text=f.read()
# it give the text in its actual form
print(text)
f.close()

# fi=open('1_heloworld.py','w')
# fi.write('Hello, world!')
# fi.close()
with open('1_heloworld.py','w') as f:
    f.write("I am inside within file")