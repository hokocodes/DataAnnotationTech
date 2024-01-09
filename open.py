def function():
    f = open("coding_qual_input.txt", "r")
    msg = f.read()

    msgSplit = msg.split("\n")

    arr1 = []

    count = 1
    while count <= len(msgSplit):
        for x in msgSplit:
            if int(x[0]) == count:
                arr1.append(x)
        
        count += 1

    #have an array thats empty
    # add arrays with the items to the empty array

    pyramid = []
    pArr = []
    pCount = 0
    # iterate through the first array
    while pCount <= len(arr1):
        
        for x in arr1:
            # if pArr is pyramid is one more than the pArr before
            if len(pyramid) == 0:
                pArr.append(x)
                pyramid.append(pArr)
                pArr = []
            # if last arr in arr pyramid length of 
            # the pyramid will finally have more than one nested array 
            elif pyramid[pyramid[len(pyramid) - 1]]
        pCount += 1

print(function())