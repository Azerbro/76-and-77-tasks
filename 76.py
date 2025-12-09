import matplotlib.pyplot as plt


file = open("C:/Users/1/Desktop/opendata.stat.txt", encoding = 'UTF-8')
file.readline()

good = []
dates = []

for string in file:
    cur = string.split(',')
    date = cur[2].split('-')
    
    if cur[0] == 'Средняя пенсия' and cur[1] == 'Забайкальский край' and int(date[0]) == 2018:
        good.append(int(cur[3]))
        dates.append(int(date[1]))

if len(good) == 0:
    print('Пенсии отсутствуют')
    exit()
    
answer = sum(good) / len(good)
print('Средняя пенсия:', round(answer, 1), 'рублей')

plt.plot(dates, good)
plt.title('График изменения пенсии в Забайкальском районе в 2018')
plt.xlabel('Дата')
plt.ylabel('Сумма')
plt.grid(True)
plt.show()

