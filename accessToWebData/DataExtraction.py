import re
fhand = input("Write Location of file u want to open\n")
flines = open(fhand)
ftot = 0
fnum = 0
flist = []
count = 0
for fline in flines :
    flist = fline.rstrip().split()
    for fword in flist :
        if re.findall('[0-9]+', fword) :
            count = count + 1
            try :
                fnum = int(fword)
            except :
                fnum = 0
            ftot = ftot + fnum
print(ftot)
print(count)
