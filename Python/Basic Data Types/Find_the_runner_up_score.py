# Given Code
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Answer
    runner_up = sorted(list(set(arr)))
    print(runner_up[-2])