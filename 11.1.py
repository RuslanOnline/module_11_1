import requests
import pandas as pd
import matplotlib.pyplot as plt

"""Requests — это библиотека  Python, которая позволяет взаимодействовать с веб-ресурсами и глобальной сетью.
Она предоставляет разработчику обширный пул функций для работы со всеми видами HTTP-запросов."""

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")


"""Pandas — это библиотека Python, используется для анализа данных в форме таблиц (датафреймов). Функциональность 
pandas включает в себя преобразование данных. Например, при помощи pandas можно сортировать строки и выделять 
подмножества, вычислять сводную статистику, например, среднее значение, изменять формы фреймов и объединять их."""

Data = [1, 3, 4, 5, 6, 2, 9]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")


"""Matplotlib — это библиотека для визуализации данных в Python. Она используется для создания любых видов графиков: 
линейных, круговых диаграмм, построчных гистограмм и других — в зависимости от поставленных задач."""

x = [1, 2, 3, 4, 5]
y = [2, 10, 5, 10, 2]

plt.plot(x, y, marker='1')

plt.title('график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
print("\n код matplotlib  \n")