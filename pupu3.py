#патер
import numpy as np

class Memento:
    """Класс для хранения состояния."""
    def __init__(self, matrix1, matrix2, result_sum, result_determinant):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result_sum = result_sum
        self.result_determinant = result_determinant

class Originator:
    """Класс для создания и восстановления состояния."""
    def __init__(self):
        self.matrix1 = None
        self.matrix2 = None
        self.result_sum = None
        self.result_determinant = None

    def set_state(self, matrix1, matrix2, result_sum, result_determinant):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result_sum = result_sum
        self.result_determinant = result_determinant

    def save_state(self):
        return Memento(self.matrix1, self.matrix2, self.result_sum, self.result_determinant)

    def restore_state(self, memento):
        self.matrix1 = memento.matrix1
        self.matrix2 = memento.matrix2
        self.result_sum = memento.result_sum
        self.result_determinant = memento.result_determinant

def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")

def input_matrices():
    """Вводит две квадратные матрицы от пользователя."""
    size = int(input("Введите размер матриц (n x n): "))
    
    print("Введите элементы первой матрицы:")
    matrix1 = []
    for i in range(size):
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split()))
        matrix1.append(row)

    print("Введите элементы второй матрицы:")
    matrix2 = []
    for i in range(size):
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split()))
        matrix2.append(row)

    return np.array(matrix1), np.array(matrix2)

def calculate_result(matrix1, matrix2):
    """Выполняет алгоритм: сумма матриц и вычисление их определителя."""
    sum_matrix = matrix1 + matrix2
    determinant = np.linalg.det(sum_matrix)
    return sum_matrix, determinant

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    originator = Originator()
    
    while True:
        print_menu()  # Выводим меню
        choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

        if choice == '1':
            # Ввод исходных данных
            matrix1, matrix2 = input_matrices()
            originator.set_state(matrix1, matrix2, None, None)  # Сохраняем состояние в Originator

        elif choice == '2':
            # Выполнение алгоритма
            if originator.matrix1 is not None and originator.matrix2 is not None:
                result_sum, result_determinant = calculate_result(originator.matrix1, originator.matrix2)
                originator.set_state(originator.matrix1, originator.matrix2, result_sum, result_determinant)  # Обновляем состояние
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите матрицы.")

        elif choice == '3':
            # Вывод результата
            if originator.result_sum is not None and originator.result_determinant is not None:
                print("Сумма матриц:")
                print(originator.result_sum)
                print(f"Определитель суммы матриц: {originator.result_determinant}")
            else:
                print("Результаты отсутствуют. Выполните алгоритм.")

        elif choice == '4':
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла

        else:
            print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта
