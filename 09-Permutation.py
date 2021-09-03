# def swap(p,a,b):
#     tmp = p[a]
#     p[a] = p[b]
#     p[b] = tmp

# p = [1,2,3,4] # [int(i) for i in input().split()]

# swap(p,1,2)
# print(p)

# for i in range(len(p)):
#     for j in range(i):

# def permutation(p):
#     l = []
#     for i in range(len(p)):
#         x = p[i]
#         xs = p[:i] + p[i+1:]
#         for j in permutation(xs):
#             l.append([x]+j)
#     return l
# print "Test"
# print(permutation(['a','b','c']))