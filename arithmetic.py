op, first, second = input().split()
first = int(first)
second = int(second)
if op == 'A': 
	print(first + second)
elif op == 'S':	
	print(first - second)
elif op == '%':	
	print(first % second)
elif op == '>':	
	print(int(first > second))
elif op == '<':	
	print(int(first < second))
else: 
	print("Invalid operation!")
