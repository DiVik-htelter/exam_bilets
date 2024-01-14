import numpy as np
import matplotlib.pyplot as plt
import random
import math # только в 12 билете используется
import scipy.integrate # только в 15 билете

def blet_1():
  # Ввод последовательности вещественных чисел
  numbers = list(map(float, input("Введите последовательность вещественных чисел через пробел: ").split()))

  # Преобразование чисел в массив numpy
  x = np.array([float(num) for num in numbers])

  # Вычисление значений функции y для каждого x
  y = (x - 2) ** 2 - 5

  # Построение точек графика
  for i in range(len(x)):
    if y[i] < 0:
        plt.plot(x[i], y[i], c="red", marker='o')
    else:
        plt.plot(x[i], y[i], c="green", marker='o')

  plt.plot(x, y, c="black") # построение графика 
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()
  # Вывод координат точек

  for point in range(len(x)):
    print("Координаты точки:",x[point], ' ', y[point])

def blet_2():
  # Ввод чисел a и b
  a, b = map(int, input("Введите два целых числа через пробел: ").split())

  # Проверка условия a < b
  if a >= b:
    print("Ошибка: значение a должно быть меньше значения b.")

  # Создание последовательности значений аргумента функции
  x = []
  for i in range(a, b + 1):
    x.append(i)
    
  # Вычисление значений функции
  y = [-1]
  for i in range(1, len(x)):
    value = y[i] / 3 + 2
    y.append(value)

  # Построение графика функции
  plt.plot(x, y, marker='o')
  plt.xlabel('X')
  plt.ylabel('F(x)')
  plt.show()

  # Вывод последнего значения функции f(b)
  last_value = y[-1]
  print("Последнее значение функции f(b):", last_value)

def blet_3():
  # Ввод чисел a, b и c
  a, b, c = map(float, input("Введите три числа через пробел: ").split())

  # Проверка условий a < b и c > 2
  if a >= b or c <= 2:
    print("Ошибка! Некорректные данные.")

  # Генерация c случайных чисел в диапазоне от a до b
  x = []
  random_numbers = []
  for i in range(int(c)):
    random_numbers.append(random.randint(int(a), int(b)))
    x.append(i)

  # Сортировка последовательности чисел по неубыванию
  random_numbers.sort()

  # Построение графика
  plt.plot(x, random_numbers)
  plt.xlabel('Номер случайного числа')
  plt.ylabel('Значение случайного числа')
  plt.title('График случайных чисел')
  plt.show()

  # Вывод минимального и максимального числа
  min_number = min(random_numbers)
  max_number = max(random_numbers)
  print("Минимальное число =", min_number)
  print("Максимальное число =", max_number)

def blet_4():
  # Ввод диапазонов отрисовки осей x и y
  x_min, x_max = map(float, input("Введите диапазон для оси x (через пробел): ").split())
  y_min, y_max = map(float, input("Введите диапазон для оси y (через пробел): ").split())

  # Создание массива x с шагом 0.2 в заданном диапазоне
  # 8 + 0.2 что бы учитывалось последнее значение 8
  x = np.arange(-2, 8 + 0.2, 0.2)
  # Вычисление значений функции y = -(x - 3)^2 + 1.5
  y = -(x - 3) ** 2 + 1.5

  # Строительство графика
  plt.plot(x, y, '--', color='blue')
  plt.axis([x_min, x_max, y_min, y_max])
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('График функции y = -(x - 3)^2 + 1.5')
  plt.show()

  # Вывод координат всех точек
  for i in range(len(x)):
    print("Точка №", i+1, ": x = ",x[i],", y = ",y[i])

def blet_5(): 
  x = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))
  x.sort()
  n_sort = []
  for i in range(len(x)):
    if x[i] < 0:
      n_sort.append(x[i])
  for i in range(len(n_sort)):
    x.remove(n_sort[i]) 

  f=[]
  f.append(1.01)
  for i in range(1, len(x)):
    f.append(f[i-1]**2+0.5)

  plt.plot(x, f, 'green')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()
  print("Координаты последней точки функции: ",x[-1],' ', f[-1]) 

def blet_6():
  a, b, c = map(int, input("Введите в одну строку через пробел три целых числа: ").split())

  if a >= b or c <= 2:
    print('Данный некорректны!')
  else:
    x = []
    y = []
    for i in range(c):
      y.append(random.uniform(a,b))
      x.append(i)
    y.sort()

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel('y')
    plt.show()
  print('Минимальное число = ', min(y))
  print('Максимальное число = ', max(y))

def blet_7():
  a, b = map(float, input("Вводите два действительных числа в одну строку через пробел: ").split())
  if a < 3 and b < 3:
    print('Данный некорректны!')
  else:
    x = np.linspace(a, b, 40)
    y = (x - 3)**0.5 + 2.5
    plt.plot(x, y, 'orange', marker='3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

  for i in range(len(x)):
    print(i+1, ' точка (', x[i], ';', y[i], ')', sep='')

def blet_8():
  file = '8b.txt'
  f = open(file, "w")
  f.write("x" + "  " + "y" + "\n")
  
  f_x = -1  # Значение функции для x = 0
  while True:
    x = input("построчно вводитe целые числа: ")
    if x == '0' :
        break
    elif x < '0':
        f.write('\n')
    else:
      f_x = round(f_x ** 2 - 0.2, 2)  # Вычисляем значение функции для текущего x
      f.write(str(x)+ " "+str(f_x)+"\n")  # Записываем текущее значение x и соответствующее значение функции в файл
  f.close()

def blet_9():
  file = '9b.txt'
  f = open(file, "w")
  f.write('x' + '\t' + 'y' + '\n')
  f.write("\n")

  while True:
    x = input("построчно вводитe вещественные числа: ")
    if x == "00":
      break
    elif x == "01":
      f.write('\n')
    else:
      def y(x):
        return (x - 0.135)**2 - 4.25
      x = float(x)
      f.write(str(round(x, 5)) + "\t" + str(round(y(x), 5)) + '\n')
  f.close()

def blet_10():
  a, b, c = list(map(int, input("Введите 3 целых числа через пробел: "). split()))

  if a >= b or c <= 2:
    print("Данный некорректны!")
  else:
    y1 = []
    y2 = []
    for i in range(c):
      y1.append(random.randint(a, b))
      y2.append(random.randint(a, b))
  y = list(set(y1) & set(y2))
  y.reverse()

  plt.plot(range(1, len(y) +1), y)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()

  print("min", min(y))
  print("max", max(y))

def blet_11():
  file = '11b.txt'
  f = open(file, 'w')
  f.write('x' + ' ' + ' y' + '\n')

  x = list(map(int, input("в строку через пробел вводите последовательность положительных целых чисел: ").split()))

  x.sort()
  x_d = []
  for i in x:
    if i <= 0:
      x_d.append(i) # находим отрицательные значения

  for i in x_d:
    x.remove(i) # удаляем отрицательные значения

  f_x = 0  # Значение функции для x = 0
  for i in x:
    f_x = round(2 * f_x - 0.2, 1)  # Вычисляем значение функции для текущего x
    f.write(str(i)+ " "+str(f_x)+"\n")  # Записываем текущее значение x и соответствующее значение функции в файл
  f.close()

def blet_12():
  a, b, c, d = map(float, input('в одну строку через пробел вводитe четыре вещественных числа в диапазоне от 0 до 10').split())
  # проверка, все числа должны быть в диапазоне от 0 до 10
  if (a or b or c or d) < 0 and (a or b or c or d) > 10:
    print("Данные некорректны!")
  else:
    dist = math.sqrt((a-c)**2+(b-d)**2)
    plt.plot([a], [b], 'red', marker='o')
    plt.plot([c], [d], 'green', marker='o')
    plt.plot([a,c], [b,d], 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.text((a+c)/2, (d+b)/2, str(dist))
    plt.axis([0, 10, 0, 10])
    plt.show()
    print('расстояние между точками: '+ str(dist))

def blet_13():
  x = list(map(float, input().split()))
  x.sort(reverse=True)

  file = '13b.txt'
  f = open(file, 'w')
  f.write('x' + ' ' + 'y' + '\n')
  
  def func(x):
    return x**3 + 0.5 * x ** 2
  
  for i in x:
    f.write(str(round(i,3)) + ' ' + str(round(func(i), 3)) + '\n')
  f.close()

  print("("+ str(max(x)) +"; "+ str(func(max(x)))+ ")")

def blet_14():
  # Ввод значений M и N
  m, n = map(int, input("Введите два целых числа через пробел: ").split())

  # Создание списка значений функции
  f = []
  f.append(m)
  for i in range(1, n):
    f.append( 2 * f[i-1] - 5.5)

  # Построение графика
  plt.plot(range(n), f, 'r-')  # сплошная красная линия
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()

# Вывод координат всех точек
  for i in range(n):
    print(i+1, " - (",i,"; ",f[i],")")

def blet_15():
  a, b, c = map(float, input("в одну строку через пробел вводитe три числа: два вещественных и одно целое: ").split())
  c=int(c)
  if a>=b or c <=5:
    print('Данные некорректны!')
  else:
    res = scipy.integrate.quad(lambda x:3 - 1.8 * x + 1.2 * x ** 2 - 0.6 * x ** 3 , a, b)
    print("Integral value:", res[0])

  # Plotting the graph
  x = np.arange(a,b,abs(a+b)/c)
  y = 3 - 1.8 * x + 1.2 * x ** 2 - 0.6 * x ** 3
  plt.plot(x, y, 'o')
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.show()

def task_1():
  # Ввод чисел a и n
  a, n = map(int, input("Введите два целых числа через пробел: ").split())
  x=[]
  y=[]
  for i in range(a,a+n):
    x.append(i)
    y.append(0.5*i**2+1)
  
  plt.plot(x, y, c="black") # построение графика 
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()

def task_2():
  # Ввод чисел a и b
  a, b = map(int, input("Введите два целых числа через пробел: ").split())

  x=[]
  y=[]
  for i in range(a*10,b*10,2):
    x.append(i/10)
    y.append(2*(i/10)**2+1)

  plt.plot(x, y, c="black") # построение графика 
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()

def task_3():
  # Ввод чисел a и b
  x1, xn = map(int, input("Введите два целых числа через пробел: ").split())
  file = 'task_3.txt'
  f = open(file, "w")

  for i in range(x1,xn):
    f.write(str(i))
    f.write(' ')
    f.write(str(3*(i)**2-1) + '\n')

  f.close()

#blet_1()
#blet_4()
#blet_3()
#blet_4()
#blet_5()
#blet_6()
#blet_7()
#blet_8()
#blet_9()
#blet_10()
#blet_11()
#blet_14()
#blet_13()
#blet_14()
#blet_15()
#task_1()
#task_2()
#task_3()