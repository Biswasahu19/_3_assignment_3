def str1(str2):
    x={"UPPER_CASE":0, "LOWER_CASE":0}
    for y in str2:
        if y.isupper():
           x["UPPER_CASE"]+=1
        elif y.islower():
           x["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str2)
    print ("No. of Upper case characters : ", x["UPPER_CASE"])
    print ("No. of Lower case Characters : ", x["LOWER_CASE"])

str1('The quick Brow Fox')
