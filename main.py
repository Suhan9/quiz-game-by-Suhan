print("Добро пожаловать в мою викторину!")

playing = input("Хотите сыграть? ")



if playing.lower() != "да":
    quit()

print("Хорошо! Давайте играть: )")
score = 0
answer = input("Столица Италии ? ")
if answer == "Рим":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Германии ? ")
if answer == "Берлин":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Франции ? ")
if answer == "Париж":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Великобритании ? ")
if answer == "Лондон":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Венгрии ? ")
if answer == "Будапешт":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Бельгии ? ")
if answer == "Брюссель":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Турции ? ")
if answer == "Анкара":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Испании ? ")
if answer == "Мадрид":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Польши ? ")
if answer == "Варшава":
    print("Верно!")
    score += 1
else:
    print("Неверно!")
answer = input("Столица Швеции ? ")
if answer == "Стокгольм":
    print("Верно!")
    score += 1

else:
    print("Неверно!")

print(" Вы ответили  правильно на  " + str (score) + " вопросов !")