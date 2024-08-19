
with open(r"C:\Users\Фаина\OneDrive\Рабочий стол\Faina.txt", 'a') as file:
    file.write('Hello!!!\n')
    file.write('I`m Faina\n')
    file.write('I`m 17\n')
    file.write('I study in IT-STEP\n')

with open(r"C:\Users\Фаина\OneDrive\Рабочий стол\Faina.txt", 'r') as file:
    print(file.read())

file.close()
