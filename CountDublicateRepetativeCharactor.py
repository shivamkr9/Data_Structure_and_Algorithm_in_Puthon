def check(strValue):
    dublicateCount = 0
    filterDub = []
    if strValue == "":
        return dublicateCount

    # Convert string into list
    for letter in strValue:
        filterDub.append(letter)

    for checkLetter in range(0, len(filterDub)):
        isWordFound = 0
        for x in range(checkLetter + 1, len(filterDub)):
            if filterDub[checkLetter] == filterDub[x]:
                isWordFound += 1

        # check if more then dublicate char is found 
        if isWordFound == 1:
            dublicateCount += 1

    return dublicateCount


strValue = "indiaia"
foundDublicateNo = check(strValue)
print(foundDublicateNo)
