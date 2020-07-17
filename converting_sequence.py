n=2*int(input())
k=list(input())
l=[]
c=0
for i in range(n):
    if(k[i]=='('):
        l.append('(')
    elif(l==[]):
        for j in range(i+1,n):
            c+=1
            if(k[j]=='('):
                (k[i],k[j])=(k[j],k[i])
                break
        l.append('(')
    else:
        l.pop()
print(c)
