sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

minValue = sample_dict['Physics']
key = 'Physics'
for x in sample_dict:
    if sample_dict[x] < minValue:
        minValue = sample_dict[x]
        key = x
print(key)
