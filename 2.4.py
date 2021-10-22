q = input()
w = q.count('(')
e = q.count(')')
if w > e:
	print('не хватает', w - e, 'закр. скобки' )
elif w < e:
	print('не хватает', e - w, 'откр. скобки' )
else:
	print('все работает')
