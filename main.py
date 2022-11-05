def define_array(SInputFile):

    import array
    a = array.array('i', [])

    with open(SInputFile) as f:
        while True:
            s = f.readline()  # считываем символ

            if not s:  # выходим, если конец
                break

            s = s.split()

            for i in range(len(s)):
                a.append(int(s[i]))

    return a


def print_array(array, len):

    for i in range(len):
        print(array[i])


def double_minus(a, l):  # a - массив, l - длина этого массива

    count_move = 0  # счётчик перемещений

    for i in range(l):
        if a[i] >= 0:
            continue

        tmp = a[i+1] #  tmp = 1
        a[i+1] = a[i] # a[i+1] = -2
        #  2 -2 1 2 3 4 -> 2 -2 -2 1 2 3 4
        # -2 -> -2 -2

    return a


def main():

    import array
    arr = array.array('i', [])

    print("-------------------")
    print("The original array:")
    arr = define_array("1.txt")
    print_array(arr, len(arr))
    print("-------------------")

    arr = double_minus(arr);

    print("--------------")
    print("Changed array:")
    print_array(arr, len(arr))
    print("--------------")

    return 0


main()

"""def task(SInputFile):
	maximum = 0
	summa = 0 # сумма всех эл-ов
	x = 0 # в x записываем текущий символ в типе int
	k = 0 #для рассм.1-го эл-та
	summa_do = 0 # сумма до 1-го глоб.макс.
	with open(SInputFile) as f:
		while True:
			x_input = f.readline() # в x_int считываем символ
			if not x_input: # выходим, если конец
				break
			x = int(x_input) # преобразуемуем x_input - переменную типа str в целочисл. переменную x
			#print("x = ", x)
			summa = summa + x
			#print("summa = ", summa)
			if k == 0: #если встретился 1-ый эл-т
				k = k + 1
				maximum = x #он автоматически становится максимумом
				summa_do = summa - x
			elif x > maximum:
				maximum = x # обновляем максимум
				summa_do = summa - x # обновляем сумму до данного эл-та
	return summa_do


def main():
	iskomaya_summa = task("1.txt")
	print("summa do maximuma = ", iskomaya_summa)
	return 0

main()"""