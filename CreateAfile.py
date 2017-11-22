#this is how we create a file in pycharm

#open a file and write to it
fw=open("sample.txt","w")
fw.write("msdcfsscsdvs\n")
fw.write("nvksdnvskdnvlsvknfdsfkfvsfsdd\n")
fw.close()



#READ A FILE
fr=open('sample.txt' ,'r')
text=fr.read()
print(text)
fr.close()
