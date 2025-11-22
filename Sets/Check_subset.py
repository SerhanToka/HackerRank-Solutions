# No Code Given
# Answer Below
t = int(input())

for _ in range(t):
    num_a = int(input())
    a = set(map(int, input().split()))
    
    num_b = int(input())
    b = set(map(int, input().split()))
    
    print(a.issubset(b))