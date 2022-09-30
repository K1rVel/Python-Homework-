a = {}
for i in range(5): a[i]=None
b = list(a.keys())
a.update({b[0]:a[b[-1]],b[-1]:a[b[0]]})
a.pop(1)
a['new_key']='new_value'
print(a)