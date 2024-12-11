#обычный
import numpy as np

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
    matrix1 = None
    matrix2 = None
    result_sum = None
    result_determinant = None

    while True:
        print_menu()  # Выводим меню
        choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

        if choice == '1':
            # Ввод исходных данных
            matrix1, matrix2 = input_matrices()
            result_sum = None  # Сбрасываем результаты
            result_determinant = None

        elif choice == '2':
            # Выполнение алгоритма
            if matrix1 is not None and matrix2 is not None:
                result_sum, result_determinant = calculate_result(matrix1, matrix2)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите матрицы.")

        elif choice == '3':
            # Вывод результата
            if result_sum is not None and result_determinant is not None:
                print("Сумма матриц:")
                print(result_sum)
                print(f"Определитель суммы матриц: {result_determinant}")
            else:
                print("Результаты отсутствуют. Выполните алгоритм.")

        elif choice == '4':
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла

        else:
            print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта
