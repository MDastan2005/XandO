used = [[0] * 3 for i in range(3)]
a = [[0] * 3 for i in range(3)]
a[0][0] = "1"
a[0][1] = "2"
a[0][2] = "3"
a[1][0] = "4"
a[1][1] = "5"
a[1][2] = "6"
a[2][0] = "7"
a[2][1] = "8"
a[2][2] = "9"

def print_table():
	print("-------------")
	for i in range(3):
		print("| ", end = '')
		for j in range(3):
			print(a[i][j], "|", end = ' ')
		print()
		print("-------------")

def cor_by_pos(x):
	for i in range(3):
		for j in range(3):
			if a[i][j] == x and (not used[i][j]):
				return i, j
	return (-1, -1)

def do_move(symbol):
	x = input("Введите номер ячейки на которую поставите " + symbol + ": ")
	i, j = cor_by_pos(x)
	while i == -1 and j == -1:
		print("Вы ошиблись!")
		x = input("Введите число еще раз: ")
		i, j = cor_by_pos(x)
	used[i][j] = 1
	a[i][j] = symbol

def check_win():
	for i in range(3):
		if a[i][0] == a[i][1] and a[i][0] == a[i][2]:
			return True
		if a[0][i] == a[1][i] and a[0][i] == a[2][i]:
			return True
	if (a[0][0] == a[1][1] and a[0][0] == a[2][2]) or (a[0][2] == a[1][1] and a[0][2] == a[2][0]):
		return True
	return False

def check_draw():
	ok = 1
	for i in range(3):
		for j in range(3):
			if used[i][j] == 0:
				ok = 0
	if ok and (not check_win()):
		print("К сожелению у нас ничья")
		exit(0)

def who_win():
	for i in range(3):
		if a[i][0] == a[i][1] and a[i][0] == a[i][2]:
			return a[i][0]
		if a[0][i] == a[1][i] and a[0][i] == a[2][i]:
			return a[0][i]
	if (a[0][0] == a[1][1] and a[0][0] == a[2][2]) or (a[0][2] == a[1][1] and a[0][2] == a[2][0]):
		return a[1][1]

print_table()
num = 1
while (not check_win()):
	check_draw()
	if num % 2 == 1:
		do_move("X")
	else:
		do_move("O")
	num += 1
	print_table()
print("Победил " + who_win() + "!")
print("Ура!")