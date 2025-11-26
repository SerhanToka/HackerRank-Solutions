# No Code Given
# Answer Below
A = set(map(int, input().split()))
N = int(input())

result = True

for _ in range(N):
    other_set = set(map(int, input().split()))
    
    if not (A > other_set):
        result = False
        break

print(result)