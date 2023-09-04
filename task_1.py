# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

quantity = int(input("Введите количество монет: "))
orel = gerb = 0
for i in range(quantity):
    side = int(input("Орел(1) или герб(0)? "))
    if side < 0 or side > 1:
        print("Error")
        break
    elif side == 1:
        orel += 1
    else:
        gerb += 1
print()
if orel == 0 or gerb == 0: print("Переворачивать нечего.")
elif orel < gerb: print(f"Переверните {orel} монет(ы) с орла на герб, их меньше всего.")
elif orel == gerb: print(f"Количество орлов и гербов одинаково, по {orel} штук(и), переверните любые.")
elif orel > gerb: print((f"Переверните {gerb} монет(ы) с герба на орла, их меньше всего."))
