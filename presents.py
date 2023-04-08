Length = int(input())
List = list(map(int, input().split()))
 
for i in range(1, Length+1):
    print(List.index(i) + 1, end=' ')
