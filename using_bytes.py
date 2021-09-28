# handling byte files
b = bytes( range(0, 256) ) # start at 0 stop before 256

# print(b)

# now lets write them to a file
fout = open('bfile', 'wb') # 'wb' to (over)write bytes
fout.write(b)
fout.close()

# read back
fin = open('bfile', 'rb')
retrieved_b = fin.read()
fin.close()
print(retrieved_b)