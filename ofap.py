
import sys

input_file = "input.ofap"

if len(sys.argv) > 1:
	input_file = sys.argv[1]
else:
	print("Usage: python ofap.py <input_file> <flags>")
	quit()

verbose = "verbose" in sys.argv

def get_command(grid, x, y):
	if (y + 1 < len(grid) and y >= 0 and x >= 0 and x + 1 < len(grid[y+1]) and x < len(grid[y])):
		return sum([grid[y][x], grid[y+1][x], grid[y][x+1], grid[y+1][x+1]])
	quit()

def move_pointer(pointer):
	if pointer["dir"] == 1:
		pointer["x"] += 1
	elif pointer["dir"] == 2:
		pointer["y"] += 1
	elif pointer["dir"] == 3:
		pointer["x"] -= 1
	else:
		pointer["y"] -= 1
	return pointer

def turn_pointer(pointer, direction):
	pointer["dir"] = (pointer["dir"] + direction) % 4
	return pointer

with open(input_file, 'r') as f:
	data = []

	for l in f.readlines():
		data.append([])
		for c in l.strip():
			if c >= "1" and c <= "9":
				data[-1].append(int(c))
			else:
				data[-1].append(0)

	if verbose:
		for d in data:
			print(''.join([str(x) for x in d]))

	stack = []
	pointer = {"x": 0, "y": 0, "dir": 1}
	running = True

	while running:
		command = get_command(data, pointer["x"], pointer["y"])

		if verbose:
			print(command, stack)

		if command == 4:
			stack.append(1)

		elif command == 5:
			pass

		elif command == 6:
			pointer = turn_pointer(pointer, 1)

		elif command == 7:
			pass

		elif command == 8:
			stack.append(2)

		elif command == 9:
			a = stack.pop()
			b = stack.pop()
			stack.append(a)
			stack.append(b)

		elif command == 10:
			pass

		elif command == 11:
			pass

		elif command == 12:
			stack.append(3)

		elif command == 13:
			if stack[-1]:
				pointer = turn_pointer(pointer, 1)
			else:
				pointer = turn_pointer(pointer, -1)

		elif command == 14:
			stack.append(stack.pop() + stack.pop())

		elif command == 15:
			pass

		elif command == 16:
			stack.append(4)

		elif command == 17:
			pass

		elif command == 18:
			a = stack.pop()
			stack.append(a // stack.pop())

		elif command == 19:
			a = stack.pop()
			stack.append(a)
			stack.append(a)

		elif command == 20:
			stack.append(5)

		elif command == 21:
			stack.pop()

		elif command == 22:
			stack.append(stack.pop() * stack.pop())

		elif command == 23:
			pass

		elif command == 24:
			stack.append(6)

		elif command == 25:
			pass

		elif command == 26:
			a = stack.pop()
			stack.append(a - stack.pop())

		elif command == 27:
			pass

		elif command == 28:
			stack.append(7)

		elif command == 29:
			pass

		elif command == 30:
			if verbose:
				print('"%s"' % chr(stack.pop()))
			else:
				print(chr(stack.pop()), end="")

		elif command == 31:
			pass

		elif command == 32:
			stack.append(8)

		elif command == 33:
			pass

		elif command == 34:
			pointer = turn_pointer(pointer, -1)

		elif command == 35:
			pass

		elif command == 36:
			stack.append(9)

		pointer = move_pointer(pointer)
