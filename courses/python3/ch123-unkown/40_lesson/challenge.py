string = '012345678901234567890123456789012345678901234567890123456789'

n = 10
list_ = [string[i: i + n] for i in range(0, len(string), n)]

return_ = '.'.join(list_)

print(return_)