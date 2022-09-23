#Jessica Noel
# September 18, 2022
#CS-555 Agile Methods for Software Development

with open("/Users/jessica/Desktop/School/CS-555/M2.B3 Project 2/tree.ged") as f:
    lines = f.readlines()

#List of all supported tags including start, note, end
valid_tags =["TRLR", "HEAD", "NOTE", "SEX", "BIRT", "DEAT", "FAMC", "FAMS","MARR", "HUSB", "WIFE", "CHIL","DIV"]

for line in lines:
    sepLine = line.split()

    #Checks if tag is supported, if yes Y, if not N
    if (sepLine[1] in valid_tags):
        validTag = "Y"

    #Cover the two excpetions, for when INDI and FAM are 3rd token/second index
    elif (len(sepLine) == 3):
        if ((sepLine[2] == "INDI") or (sepLine[2] == "FAM")):
            sepLine[1] = sepLine[2]
            validTag = "Y"

    #Cover 2 DATE, but not 1 DATE
    elif ((sepLine[0] == "2") and (sepLine[1] == "DATE")):
        validTag = "Y"
    
    #Cover 1 NAME, but not 2 NAME
    elif ((sepLine[0] == "1") and (sepLine[1] == "NAME")):
        validTag = "Y"
    
    #All other variations are not supported or valid
    else:
        validTag = "N"

    args = ""
    for x in sepLine[2:len(sepLine)]:
        args += (x + " ")

    print("--> " + line)
    print("<-- " + sepLine[0] + "|" + sepLine[1] + "|" + validTag + "|" + args + "\n")

f.close()


    
    