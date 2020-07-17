for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==len(set(l))):
        print('Yes')
    else:
        print('No')
