# No Code Given
# Answer Below
input()
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd = input().split()[0]
    other_set = set(map(int, input().split()))
    
    if cmd == 'intersection_update':
        A.intersection_update(other_set)
    elif cmd == 'update':
        A.update(other_set)
    elif cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif cmd == 'difference_update':
        A.difference_update(other_set)

print(sum(A))