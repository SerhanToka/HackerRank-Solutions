# No Given Code
# Answer Below, yes same as union
n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

total_subscribers = english.difference(french)

print(len(total_subscribers))