import time
import math
from typing import List

def sieve_of_eratosthenes_full(n: int) -> List[int]:
    # Решето Эратосфена для отрезка [2, ..., N]
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i]]


def sieve_eratosthenes_range(a: int, n: int) -> List[int]:
    # Def1: Модифицированное решето Эратосфена для отрезка [A, ..., N]
    # Создаем полное решето до N, затем фильтруем от A
    if a < 2:
        a = 2
    if n < a:
        return []
    
    primes_full = sieve_of_eratosthenes_full(n)
    return [p for p in primes_full if p >= a]


def segmented_sieve(a: int, n: int) -> List[int]:
    # Def2: Сегментированное решето Эратосфена для отрезка [A, ..., N]
    # Эффективно для больших A, когда A близко к N
    if a < 2:
        a = 2
    if n < a:
        return []
    
    # Находим все простые до sqrt(N)
    limit = int(math.sqrt(n)) + 1
    base_primes = sieve_of_eratosthenes_full(limit)
    
    # Создаем булев массив для отрезка [A, N]
    segment_size = n - a + 1
    segment = [True] * segment_size
    
    # Отмечаем составные числа в отрезке
    for prime in base_primes:
        # Находим первое число в отрезке, кратное prime
        first_multiple = max(prime * prime, ((a + prime - 1) // prime) * prime)
        
        for j in range(first_multiple, n + 1, prime):
            segment[j - a] = False
    
    # Собираем простые числа из отрезка
    return [i for i in range(a, n + 1) if segment[i - a]]


def benchmark(func, a: int, n: int, name: str):
    # Функция для замера скорости
    start_time = time.perf_counter()
    result = func(a, n)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"{name} [{a}, {n}]: {len(result)} простых чисел, время: {elapsed:.6f} сек")
    return elapsed


def run_tests():
    # Тестовые случаи
    test_cases = [
        (2, 10_000),
        (1_000, 10_000),
        (2, 100_000),
        (10_000, 100_000),
        # Дополнительные тесты для больших значений
        (2, 1_000_000),
        (500_000, 1_000_000),
    ]
    
    print("СРАВНЕНИЕ АЛГОРИТМОВ ПОИСКА ПРОСТЫХ ЧИСЕЛ НА ОТРЕЗКЕ")
    print("=" * 60)
    
    for a, n in test_cases:
        print(f"\nОтрезок [{a}, ..., {n}]:")
        print("-" * 40)
        
        # Def1: Полное решето + фильтрация
        time_def1 = benchmark(sieve_eratosthenes_range, a, n, "Def1 (полное решето + фильтр)")
        
        # Def2: Сегментированное решето
        time_def2 = benchmark(segmented_sieve, a, n, "Def2 (сегментированное решето)")
        
        # Сравнение
        if time_def1 > 0 and time_def2 > 0:
            speedup = time_def1 / time_def2
            if speedup > 1:
                print(f"  => Def2 быстрее в {speedup:.2f} раз(а)")
            else:
                print(f"  => Def1 быстрее в {1/speedup:.2f} раз(а)")


# Запуск тестов
if __name__ == "__main__":
    run_tests()