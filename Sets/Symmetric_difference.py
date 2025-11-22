# No Given Code
# Answer Below
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

diff1 = m_set.difference(n_set)
diff2 = n_set.difference(m_set)

result = diff1.symmetric_difference(diff2)

for i in sorted(result):
    print(i)