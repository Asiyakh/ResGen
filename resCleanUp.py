
#### STEP 1: REMOVE LINUX HEADING ###

lines_per_file = 1000
smallfile = None
bigfile = open("resumes.txt", "r", encoding='mac_roman')
with bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_res_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

### STEP 2: SEPERATE BULLET POINTS

import os
bulletpoint = open("trainingSet.txt", "w")
os.chdir("./smallRes")
for file in os.listdir("./"):
    openfile = open(file, encoding="utf8", errors='ignore')
    bigfile = openfile.readlines()
    line = bigfile[10]
    sol = line.split("√Ø ")
    for s in sol[1:]:
        s = s.replace('‚Ä†', '')
        bulletpoint.write(s)
        bulletpoint.write("\n")
    openfile.close()


    

