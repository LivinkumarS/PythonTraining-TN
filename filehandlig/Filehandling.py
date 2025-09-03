# file=open("text.txt",'r')
# # content=file.read()
# line1=file.readline()
# line2=file.readline()
# line3=file.readline()
# print(line3)

# file.close()

# file = open("text.txt",'w')
# content='''
# Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. \nPython 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. \nRecent versions, such as Python 3.12, have added capabilites and keywords for typing (and more; e.g. increasing speed); helping with (optional) static typing.\n Currently only versions in the 3.x series are supported.
# '''

# file.write(content)

# file.close()




# file=open("text.txt",'a')

# content='''
# Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. \nPython 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. \nRecent versions, such as Python 3.12, have added capabilites and keywords for typing (and more; e.g. increasing speed); helping with (optional) static typing.\n Currently only versions in the 3.x series are supported.
# '''

# file.write(content)

# file.close()


file = open("text.txt",'r')

print(file.readlines())


file.close()