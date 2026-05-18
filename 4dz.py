# ==================== АЛГОРИТМ ПОИСКА ПРОСТЫХ ЦИКЛОВ ====================

def build_adjacency_list(n, edges):
    # Построение списка смежности из списка ребер
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    return adj


def find_cycles_dfs(adj, start, current, visited, path, cycles, K):
    # DFS для поиска простых циклов через заданную вершину
    # start - вершина, через которую должен проходить цикл
    # current - текущая вершина в обходе
    # visited - множество посещенных вершин
    # path - текущий путь
    # cycles - список найденных циклов
    # K - максимальная длина цикла
    
    # Если путь слишком длинный, останавливаемся
    if len(path) > K:
        return
    
    # Перебираем соседей текущей вершины
    for neighbor in adj[current]:
        # Нашли цикл: вернулись в стартовую вершину
        if neighbor == start and len(path) >= 2:
            cycle = path + [start]
            cycles.append(cycle)
        # Продолжаем поиск, если вершина не посещена и не стартовая
        # (стартовую посещаем только в начале и в конце)
        elif neighbor != start and neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            find_cycles_dfs(adj, start, neighbor, visited, path, cycles, K)
            path.pop()
            visited.remove(neighbor)


def normalize_cycle(cycle):
    # Нормализация цикла для удаления дубликатов (сдвигов)
    # Находим минимальный элемент и его позицию
    # Цикл без последней вершины (она равна первой)
    cycle_body = cycle[:-1]
    
    if not cycle_body:
        return tuple(cycle)
    
    min_val = min(cycle_body)
    min_indices = [i for i, val in enumerate(cycle_body) if val == min_val]
    
    # Пробуем все возможные нормализации (для случаев с одинаковыми минимальными)
    candidates = []
    for min_idx in min_indices:
        normalized = cycle_body[min_idx:] + cycle_body[:min_idx] + [min_val]
        candidates.append(tuple(normalized))
    
    # Возвращаем лексикографически минимальный вариант
    return min(candidates)


def remove_duplicate_cycles(cycles):
    # Удаление дубликатов циклов (циклы, отличающиеся сдвигом)
    unique_cycles = []
    seen = set()
    
    for cycle in cycles:
        normalized = normalize_cycle(cycle)
        if normalized not in seen:
            seen.add(normalized)
            unique_cycles.append(cycle)
    
    return unique_cycles


def find_all_cycles_through_vertex(n, edges, v, K):
    # Поиск всех простых циклов через заданную вершину v
    # n - количество вершин
    # edges - список ребер
    # v - вершина, через которую ищем циклы
    # K - максимальная длина цикла
    
    # Строим список смежности
    adj = build_adjacency_list(n, edges)
    
    # Ищем циклы через вершину v
    cycles = []
    visited = {v}
    path = [v]
    
    find_cycles_dfs(adj, v, v, visited, path, cycles, K)
    
    # Удаляем дубликаты
    unique_cycles = remove_duplicate_cycles(cycles)
    
    return unique_cycles


# ==================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ====================

def print_cycles(cycles, v):
    # Красивый вывод найденных циклов
    print("=" * 60)
    print(f"НАЙДЕННЫЕ ПРОСТЫЕ ЦИКЛЫ ЧЕРЕЗ ВЕРШИНУ {v}")
    print("=" * 60)
    
    if not cycles:
        print("  Циклы не найдены")
    else:
        for i, cycle in enumerate(cycles, 1):
            cycle_str = " -> ".join(str(node) for node in cycle)
            print(f"  Цикл {i}: [{cycle_str}] (длина: {len(cycle) - 1})")
    
    print(f"\n  Всего уникальных циклов: {len(cycles)}")
    print()


def has_cycle_through_vertex(cycles):
    # Проверка существования хотя бы одного цикла
    return len(cycles) > 0


def print_adjacency_list(adj):
    # Вывод списка смежности
    print("СПИСОК СМЕЖНОСТИ ГРАФА:")
    for i, neighbors in enumerate(adj):
        print(f"  {i}: {neighbors}")
    print()


# ==================== ПРИМЕРЫ ====================

def example_1():
    # Пример из задания
    print("\n" + "#" * 60)
    print("ПРИМЕР 1 (из задания)")
    print("#" * 60)
    
    n = 4
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3)
    ]
    v = 0
    K = 4
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    cycles = find_all_cycles_through_vertex(n, edges, v, K)
    print_cycles(cycles, v)
    print(f"Существует ли цикл через вершину {v}: {has_cycle_through_vertex(cycles)}")


def example_2():
    # Основной граф из задания
    print("\n" + "#" * 60)
    print("ПРИМЕР 2 (основной граф)")
    print("#" * 60)
    
    n = 5
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (3, 4),
        (4, 0),
        (1, 3),
        (3, 2)
    ]
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    # Ищем циклы через все вершины
    for v in range(n):
        K = 6  # Максимальная длина цикла
        cycles = find_all_cycles_through_vertex(n, edges, v, K)
        
        if cycles:
            print(f"\nЦиклы через вершину {v}:")
            for i, cycle in enumerate(cycles, 1):
                cycle_str = " -> ".join(str(node) for node in cycle)
                print(f"  [{cycle_str}]")
            print(f"  Количество: {len(cycles)}")
            print(f"  Существует: {has_cycle_through_vertex(cycles)}")


def example_3():
    # Сложный граф с несколькими циклами
    print("\n" + "#" * 60)
    print("ПРИМЕР 3 (сложный граф)")
    print("#" * 60)
    
    n = 6
    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 4),
        (3, 5),
        (4, 5),
        (4, 0),
        (5, 0)
    ]
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    v = 0
    K = 8
    cycles = find_all_cycles_through_vertex(n, edges, v, K)
    print_cycles(cycles, v)
    print(f"Существует ли цикл через вершину {v}: {has_cycle_through_vertex(cycles)}")


def example_4():
    # Граф без циклов через заданную вершину
    print("\n" + "#" * 60)
    print("ПРИМЕР 4 (граф без циклов через вершину 3)")
    print("#" * 60)
    
    n = 5
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (3, 4)
    ]
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    # Вершина 0 имеет цикл, вершина 3 - нет
    for v in [0, 3]:
        K = 5
        cycles = find_all_cycles_through_vertex(n, edges, v, K)
        print_cycles(cycles, v)
        print(f"Существует ли цикл через вершину {v}: {has_cycle_through_vertex(cycles)}")


def example_5():
    # Проверка на дубликаты циклов
    print("\n" + "#" * 60)
    print("ПРИМЕР 5 (проверка удаления дубликатов)")
    print("#" * 60)
    
    n = 4
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (0, 2),
        (2, 0)
    ]
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    v = 0
    K = 6
    cycles = find_all_cycles_through_vertex(n, edges, v, K)
    print_cycles(cycles, v)
    print(f"Существует ли цикл через вершину {v}: {has_cycle_through_vertex(cycles)}")


# ==================== ФУНКЦИЯ ДЛЯ ВВОДА СВОИХ ДАННЫХ ====================

def custom_input():
    # Ввод своего графа
    print("\n" + "#" * 60)
    print("ВВОД СВОЕГО ГРАФА")
    print("#" * 60)
    
    n = int(input("Введите количество вершин (n <= 15): "))
    
    print("Введите ребра в формате 'u v' (по одному на строку)")
    print("Пустая строка - конец ввода")
    
    edges = []
    while True:
        line = input().strip()
        if not line:
            break
        u, v = map(int, line.split())
        edges.append((u, v))
    
    v = int(input("Введите вершину для поиска циклов: "))
    K = int(input("Введите максимальную длину цикла: "))
    
    adj = build_adjacency_list(n, edges)
    print_adjacency_list(adj)
    
    cycles = find_all_cycles_through_vertex(n, edges, v, K)
    print_cycles(cycles, v)
    print(f"Существует ли цикл через вершину {v}: {has_cycle_through_vertex(cycles)}")


# ==================== ЗАПУСК ====================

if __name__ == "__main__":
    print("АЛГОРИТМ ПОИСКА ПРОСТЫХ ЦИКЛОВ ЧЕРЕЗ ЗАДАННУЮ ВЕРШИНУ")
    print("Метод: DFS с возвратом (backtracking)")
    print("Сложность: O(V + E * 2^V) в худшем случае")
    print("Оптимизация: ограничение по длине K")
    print()
    
    # Запуск примеров
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    
    # Раскомментировать для ручного ввода
    # custom_input()