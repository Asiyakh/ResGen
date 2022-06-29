
#### STEP 1: REMOVE LINUX HEADING ###
"""
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
"""

### STEP 2: SEPERATE BULLET POINTS

# import os
# bigfile = open("smallRes/small_res_1000.txt", "r").readlines()
# line = bigfile[10]
# bulletpoint = open("bulletPoints_1000.txt", "w")
# sol = line.split("√Ø ")
# for s in sol:
#     bulletpoint.write(s)
#     bulletpoint.write("\n")


    

