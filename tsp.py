#code
#a = ['A', 'B', 'C']
#l = 0
#r = len(a)

arr = []
graph = [[ 0, 10, 15, 20 ],
         [ 10, 0, 35, 25 ],
         [ 15, 35, 0, 30 ],
         [ 20, 25, 30, 0 ]];

a = [i for i in range(len(graph)) if i!=0]
l = 0
r = len(graph)-1

def perm(a,l,r):
    for i in range(l,r):
        #print i,l,r
        if l==r-1:
            #print a
            arr.append(a[:])
        else:
            a[l],a[i] = a[i],a[l]
            perm(a,l+1,r)
            a[l],a[i] = a[i],a[l]

perm(a,l,r)
print arr

min_path = 1000
path_wt = 0
for a in arr:
    k = 0
    for i in a:
        path_wt += graph[k][i]
        k = i
    path_wt += graph[k][0]
    #print path_wt
    if path_wt < min_path:
        min_path = path_wt
    path_wt = 0

print min_path

