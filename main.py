print("Приветствую тебя в игре-квиз!")
points = 0

if input("Земля круглая? ") == "да": points += 1
else: points -= 1

if input("20//4 == 5? ") == "да": points += 1
else: points -= 1

if input("2+2 == 4? ") == "да": points += 1
else: points -= 1

if input("Паук - это насекомое? ") == "да": points += 1
else: points -= 1

print(f"Ваше количество очков: {points}")

if points >= 4: print("Поздравляю! Вы победили!")
elif points >= 2: print("Вы могли справиться лучше!")
elif points >= 0: print("Вы старались...")
else: print("Вы проиграли! Попробуйте снова!")