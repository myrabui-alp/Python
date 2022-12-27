# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = dict()
for x in range(len(keys)):
    dic.update({keys[x]: values[x]})
print(dic)
