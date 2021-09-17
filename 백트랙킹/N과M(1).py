# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
from itertools import permutations

n, m = map(int, input().split())
visited = [False] * n
array = [i for i in range(1,n+1)]
a =permutations(array,m);
for i in a:
    print(' '.join(map(str,i)))
