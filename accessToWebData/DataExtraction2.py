import re
fhand = input("Write Location of file u want to open\n")
flines = open(fhand)
ftot = 0
fnum = 0
for fline in flines :
    fnums = re.findall('[0-9]+',fline)
    for fnum in fnums:
        ftot = ftot + int(fnum)
print(ftot)
