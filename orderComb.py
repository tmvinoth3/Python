import string

def mapAlpha(st):
    alpha = string.ascii_uppercase
    arr = st.split(' ')
    s = ""
    #print arr
    flag = all(int(a)<=26 for a in arr if a!='')
    if flag:
        for a in arr:
            if a != '':
                if int(a) > 26:
                    break
                s += ' '+alpha[int(a)-1]
    print s

def orderComb(inp,i,out,j):
    if i==len(inp):
        m = map(str,out)
        st = "".join(m)
        mapAlpha(st)
        return
    out[j] = inp[i]
    out[j+1] = " "
    orderComb(inp,i+1,out,j+2)
    
    if i+1 != len(inp):
        orderComb(inp,i+1,out,j+1)

inp = [1,2,3,4]
l = len(inp)
out = [' '] * (l*2)
orderComb(inp,0,out,0)