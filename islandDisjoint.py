import sys
class disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.n = n
    
    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x
    
    def union(self, u, v):
        xRoot = self.find(u)
        yRoot = self.find(v)
        
        if xRoot == yRoot:
            return
        
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

inp = raw_input().replace("{","[").replace("}","]")
inp = eval(inp)
rlen = len(inp)
clen = len(inp[0])
dis = disjoint(rlen*clen)
#print rlen,clen

row = [-1,-1,-1,0,0,1,1,1]
col = [-1,0,1,-1,1,-1,0,1]

for j in range(rlen):
    for k in range(clen):
        for i in range(8):
            if inp[j][k] != 0:
                if (j+row[i]) < clen and (k+col[i]) < clen and (k+col[i]) >= 0 and (j+row[i]) >= 0 and inp[j+row[i]][k+col[i]]:
                    dis.union(j*clen+k, (j+row[i])*clen+(k+col[i]))

print [dis.parent[x] for x in dis.parent]

count = [0]*(clen*rlen)
islandCount = 0
islandSize = 0
for j in range(rlen):
    for k in range(clen):
        if inp[j][k] != 0:
            x = dis.find(j*clen+k)
            if count[x] == 0:
                islandCount += 1
                count[x] += 1
            else:
                count[x] += 1

print islandCount
print count