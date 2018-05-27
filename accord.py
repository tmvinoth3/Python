insig = input()
sig = input("\n")
#print insig
#print sig
insigList = insig.split(' ')
sigList = sig.split(' ')
abb = sigList[0]
abbLen = len(abb)
sigList = [sigList[i] for i in range(1,len(sigList))]
for ins in insigList:
    if ins in sigList:
        sigList.remove(ins)
print(sigList)

def checkAtleastOneChar():
    flag = False
    found = False
    count = 0
    for sig in sigList:
        for s in sig:
            if s.upper() in abb:
                count += 1
                break
            #for a in abb:
                #if s.upper() == a:
                #    count += 1
                #    found = True
                #    break
            #if found:
            #    break
    if count == len(sigList):
        flag = True
    return flag
    

def checkList():
    count = k =0
    for  i in range(len(sigList)):
        for index,s in enumerate(sigList[i]):
            #print(s)
            #print "Before {}".format(sig)
            if s.upper() == abb[k]:
                print("{} {}".format(s,abb[k]))
                k += 1
                sigList[i] = sigList[i].replace(s,"",1)
                #print sig
                if k == abbLen:
                    count += 1
                    k=0
    return count

abbCount = 0
if checkAtleastOneChar() == True:
    res = checkList()
    print(sigList)
    print(res)
    if res > 0:
        abbCount += res
    while res > 0:
         print("While loop executed")
         res = checkList()
         if res > 0:
             abbCount += res

    if abbCount == 0:
        print("Not found")
    else:
        print(abbCount)
else:
    print("Check one char Not found")
