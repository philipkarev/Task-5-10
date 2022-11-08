def define_array(SInputFile):  # заполнение массива числами из файла

    a = []

    with open(SInputFile) as f:
        while True:
            try:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                for i in range(len(s)):
                    a.append(int(s[i]))
            except ValueError:
                print("Error: bad value.")
            except FileNotFoundError:
                print("Error: file not found.")
    
    return a


def print_array(array, l):

    for i in range(l):
        print(array[i])


def double_minus(a, l):  # a - массив, l - длина этого массива

    i = 0
    while i < l:
        if a[i] >= 0:
            i += 1
            continue

        # a.append(a[l-1])
        # l += 1

        # for j in range(l-1, i, -1): 
        #     a[j] = a[j-1]

        # a[i+1] = a[i]

        a.insert(i + 1, a[i])
        i += 2

    return a


def main():

    arr = []

    print("-------------------")
    print("The original array:")
    arr = define_array("1.txt")
    print_array(arr, len(arr))
    print("-------------------")

    arr = double_minus(arr, len(arr))

    print("--------------")
    print("Changed array:")
    print_array(arr, len(arr))
    print("--------------")

    return 0


main()
