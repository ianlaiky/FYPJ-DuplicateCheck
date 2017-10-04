confff = open("nodupefound.txt", 'r')
conf = confff.readlines()
confff.close()


for lines in conf:
    print(lines)