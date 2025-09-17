# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
     weight=float(input("Введите число: "))
     height=float(input("Введите число: "))
     bmi=weight/height**2
     print(bmi)
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()