from functools import reduce
func = lambda x,y:x+y
result = reduce(func, [1, 2, 3, 4, 5])
print(result)


result1 = reduce(lambda x,y:x+y, ["aa","bb","cc","dd","ee",])
print(result1)
