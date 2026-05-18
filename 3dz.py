import time

# ==================== СОРТИРОВКА СЛИЯНИЕМ ====================

def merge_sort(arr, key_func):
    # Сортировка слиянием (Merge Sort) - стабильная O(n log n)
    if len(arr) <= 1:
        return arr
    
    # Разделяем массив пополам
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_func)
    right = merge_sort(arr[mid:], key_func)
    
    # Сливаем отсортированные половины
    return merge(left, right, key_func)


def merge(left, right, key_func):
    # Слияние двух отсортированных массивов
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Сравниваем по ключу
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_animals(animals):
    # Сортировка: по массе (возрастание), при равенстве - по кличке (алфавит)
    def sort_key(animal):
        # animal = [кличка, вид, масса]
        return (animal[2], animal[0])  # масса, затем кличка
    
    return merge_sort(animals, sort_key)


# ==================== ФУНКЦИИ ДЛЯ РЕШЕНИЯ ЗАДАЧ ====================

def print_all_sorted(animals_sorted):
    # Вывод всех животных в отсортированном порядке
    print("=" * 60)
    print("ВСЕ ЖИВОТНЫЕ В ОТСОРТИРОВАННОМ ПОРЯДКЕ")
    print("=" * 60)
    print(f"{'№':<4} {'Кличка':<15} {'Вид':<20} {'Масса':<6}")
    print("-" * 45)
    for i, animal in enumerate(animals_sorted, 1):
        print(f"{i:<4} {animal[0]:<15} {animal[1]:<20} {animal[2]:<6}")
    print()


def print_lightest(animals_sorted, count=3):
    # Вывод самых легких животных
    print("=" * 60)
    print(f"{count} САМЫХ ЛЕГКИХ ЖИВОТНЫХ")
    print("=" * 60)
    for i, animal in enumerate(animals_sorted[:count], 1):
        print(f"{i}. {animal[0]} ({animal[1]}) - {animal[2]} кг")
    print()


def print_heaviest(animals_sorted, count=3):
    # Вывод самых тяжелых животных
    print("=" * 60)
    print(f"{count} САМЫХ ТЯЖЕЛЫХ ЖИВОТНЫХ")
    print("=" * 60)
    for i, animal in enumerate(animals_sorted[-count:][::-1], 1):
        print(f"{i}. {animal[0]} ({animal[1]}) - {animal[2]} кг")
    print()


def find_by_mass(animals_sorted, target_mass):
    # Поиск всех животных с заданной массой
    result = []
    for animal in animals_sorted:
        if animal[2] == target_mass:
            result.append(animal)
    return result


def print_by_mass(animals_sorted, mass):
    # Вывод животных с заданной массой
    found = find_by_mass(animals_sorted, mass)
    print("=" * 60)
    print(f"ЖИВОТНЫЕ С МАССОЙ {mass} КГ")
    print("=" * 60)
    if found:
        for animal in found:
            print(f"  {animal[0]} ({animal[1]})")
    else:
        print("  Животных с такой массой не найдено")
    print(f"  Всего найдено: {len(found)}")
    print()


def print_mass_groups(animals_sorted):
    # Группы животных с одинаковой массой
    print("=" * 60)
    print("ГРУППЫ ЖИВОТНЫХ С ОДИНАКОВОЙ МАССОЙ")
    print("=" * 60)
    
    groups = []
    current_mass = None
    current_group = []
    
    for animal in animals_sorted:
        mass = animal[2]
        if mass != current_mass:
            if current_group and len(current_group) > 1:
                groups.append((current_mass, current_group))
            current_mass = mass
            current_group = [animal]
        else:
            current_group.append(animal)
    
    # Проверяем последнюю группу
    if current_group and len(current_group) > 1:
        groups.append((current_mass, current_group))
    
    if groups:
        for mass, group in groups:
            print(f"\n  Масса {mass} кг ({len(group)} животных):")
            for animal in group:
                print(f"    - {animal[0]} ({animal[1]})")
    else:
        print("  Нет групп с одинаковой массой")
    
    print(f"\n  Всего групп с одинаковой массой: {len(groups)}")
    print()


# ==================== ДОПОЛНИТЕЛЬНЫЕ ЗАДАЧИ ====================

def print_animals_by_species(animals_sorted, species):
    # Вывод животных определенного вида
    print("=" * 60)
    print(f"ЖИВОТНЫЕ ВИДА: {species.upper()}")
    print("=" * 60)
    found = [a for a in animals_sorted if a[1] == species]
    if found:
        for animal in found:
            print(f"  {animal[0]} - {animal[2]} кг")
    else:
        print("  Не найдено")
    print()


def print_statistics(animals_sorted):
    # Статистика по зоопарку
    print("=" * 60)
    print("СТАТИСТИКА ПО ЗООПАРКУ")
    print("=" * 60)
    
    total_animals = len(animals_sorted)
    total_mass = sum(a[2] for a in animals_sorted)
    avg_mass = total_mass / total_animals
    min_animal = animals_sorted[0]
    max_animal = animals_sorted[-1]
    
    # Считаем виды
    species_count = {}
    for animal in animals_sorted:
        species = animal[1]
        species_count[species] = species_count.get(species, 0) + 1
    
    print(f"  Всего животных: {total_animals}")
    print(f"  Всего видов: {len(species_count)}")
    print(f"  Общая масса: {total_mass} кг")
    print(f"  Средняя масса: {avg_mass:.1f} кг")
    print(f"  Самое легкое: {min_animal[0]} ({min_animal[1]}) - {min_animal[2]} кг")
    print(f"  Самое тяжелое: {max_animal[0]} ({max_animal[1]}) - {max_animal[2]} кг")
    print()


# ==================== СПИСОК ЖИВОТНЫХ ====================

animals = [
    ["Барсик", "рысь", 18],
    ["Слоник", "слон", 5400],
    ["Луна", "волк", 32],
    ["Грибочек", "лиса", 18],
    ["Миша", "медведь", 310],
    ["Тигра", "тигр", 220],
    ["Король", "лев", 205],
    ["Снежок", "заяц", 4],
    ["Гром", "бизон", 720],
    ["Норка", "енот", 9],
    ["Марта", "жираф", 810],
    ["Шторм", "носорог", 2100],
    ["Дымка", "пума", 68],
    ["Мила", "лама", 130],
    ["Кузя", "кабан", 140],
    ["Зевс", "орел", 6],
    ["Плюша", "панда", 115],
    ["Искра", "антилопа", 95],
    ["Яша", "ягуар", 96],
    ["Няня", "обезьяна", 27],
    ["Тор", "лось", 430],
    ["Лада", "косуля", 34],
    ["Шура", "сурикат", 5],
    ["Гоша", "бегемот", 1600],
    ["Рада", "зебра", 280],
    ["Туман", "волк", 41],
    ["Кира", "рысь", 21],
    ["Мишка", "медведь", 360],
    ["Феня", "лиса", 14],
    ["Арчи", "тигр", 240],
    ["Веста", "леопард", 72],
    ["Птичка", "соболь", 8],
    ["Пороро", "пингвин", 12],
    ["Ева", "кенгуру", 85],
    ["Грант", "верблюд", 540],
    ["Оскар", "осел", 190],
    ["Шустрик", "лама", 145],
    ["Тюльпан", "альпака", 62],
    ["Милашка", "сурикат", 6],
    ["Умник", "шимпанзе", 48],
    ["Великан", "слон", 4900],
    ["Зубр", "зубр", 790],
    ["Апельсинка", "капибара", 51],
    ["Работа", "волк", 38],
    ["Высь", "рысь", 19],
    ["Персик", "орангутан", 77],
    ["Юта", "пума", 70],
    ["Пумба", "кабан", 155],
    ["Розовый", "фламинго", 3],
    ["Тедди", "медведь", 295],
    ["Мурка", "корова", 410],
    ["Трус", "страус", 104],
    ["Тайга", "тигр", 228],
    ["Жулик", "енот", 11],
    ["Тимон", "сурикат", 4],
    ["Симба", "лев", 198],
    ["Сима", "лиса", 16],
    ["Бруно", "ягуар", 101],
    ["Вихрь", "лошадь", 460],
    ["Ветер", "косуля", 29],
    ["Бегемотик", "бегемот", 1750],
    ["Полоска", "зебра", 300],
    ["Рере", "пингвин", 13],
    ["Мира", "кенгуру", 79],
    ["Серый", "волк", 44],
    ["Рыка", "рысь", 20],
    ["Рожок", "носорог", 2300],
    ["Кузко", "лама", 128],
    ["Ти", "тигр", 235],
    ["Бэлла", "леопард", 67],
    ["Сестрица", "лиса", 15],
    ["Панда", "панда", 109],
    ["Заря", "антилопа", 89],
    ["Тим", "обезьяна", 24],
    ["Высотка", "жираф", 780],
    ["Орфей", "орел", 5],
    ["Лаки", "соболь", 7],
    ["Скай", "ястреб", 4],
    ["Капибара", "капибара", 56],
    ["Аякс", "бизон", 680],
    ["Нелли", "альпака", 58],
    ["Вилли", "осел", 175],
    ["Дора", "пума", 73],
    ["Макс", "кабан", 148],
    ["Лея", "фламинго", 4],
    ["Ральф", "медведь", 340],
    ["Волк", "волк", 36],
    ["Умка", "белый медведь", 410],
    ["Кай", "снежный барс", 44],
    ["Пушистик", "рысь", 22],
    ["Денди", "страус", 97],
    ["Бусинка", "енот", 10],
    ["Грэм", "зубр", 810],
    ["Молния", "лошадь", 430],
    ["Фред", "кенгуру", 91],
    ["Есения", "зебра", 275],
    ["Нептун", "морской лев", 260],
    ["Сальма", "лама", 132],
    ["Грей", "леопард", 69],
    ["Ирис", "лиса", 17],
    ["Земля", "сурикат", 5],
    ["Юпитер", "слон", 5200],
    ["Роса", "косуля", 31],
    ["Арфа", "антилопа", 87],
    ["Шериф", "волк", 43],
    ["Пума", "пума", 71],
    ["Дина", "обезьяна", 26],
    ["Коди", "пингвин", 14],
    ["Лавр", "верблюд", 560],
    ["Папанда", "панда", 112],
    ["Мускат", "кабан", 162],
    ["Топаз", "ягуар", 98],
    ["Соната", "жираф", 840],
    ["Бакс", "лев", 212],
    ["Челси", "лиса", 13],
    ["Рубин", "тигр", 245],
    ["Линда", "енот", 12],
    ["Аметист", "пума", 66],
    ["Триша", "альпака", 60],
    ["Единорог", "носорог", 2250],
    ["Мята", "капибара", 54],
    ["Орел", "орел", 6],
    ["Гуфи", "обезьяна", 29],
    ["Север", "бизон", 705],
    ["Жасмин", "лама", 126],
    ["Каспер", "снежный барс", 47],
    ["Моника", "зебра", 290],
    ["Айс", "пингвин", 11],
    ["Терра", "рысь", 23],
    ["Флинт", "волк", 39],
    ["Белка", "сурикат", 4],
    ["Гера", "лиса", 18],
    ["Стелла", "кенгуру", 83],
    ["Морис", "медведь", 330],
    ["Киви", "фламинго", 3],
    ["Рой", "кабан", 150],
    ["Аврора", "леопард", 74],
    ["Платон", "осел", 185],
    ["Дунай", "лошадь", 470],
    ["Вега", "антилопа", 92],
    ["Наоми", "панда", 118],
    ["Подлодка", "морской лев", 245],
    ["Шая", "капибара", 53],
    ["Корсар", "зубр", 830],
    ["Ева", "лиса фенек", 6],
    ["Магнолия", "альпака", 63],
    ["Рокси", "рысь", 24],
    ["Тайфун", "лев", 208],
    ["Сафира", "тигр", 232],
    ["Оливер", "енот", 9],
    ["Луна", "фламинго", 4],
    ["Граф", "верблюд", 590],
    ["Нокс", "снежный барс", 46],
]


# ==================== ЗАПУСК ====================

if __name__ == "__main__":
    # Замер скорости сортировки
    start = time.perf_counter()
    sorted_animals = sort_animals(animals)
    sort_time = time.perf_counter() - start
    
    print(f"АЛГОРИТМ: СОРТИРОВКА СЛИЯНИЕМ (Merge Sort)")
    print(f"Сложность: O(n log n), стабильная")
    print(f"Время сортировки: {sort_time:.6f} сек")
    print(f"Отсортировано животных: {len(sorted_animals)}")
    print()
    
    # 1. Вывод всех животных
    print_all_sorted(sorted_animals)
    
    # 2. Три самых легких
    print_lightest(sorted_animals, 3)
    
    # 3. Три самых тяжелых
    print_heaviest(sorted_animals, 3)
    
    # 4. Поиск по заданной массе (несколько примеров)
    print_by_mass(sorted_animals, 4)
    print_by_mass(sorted_animals, 18)
    print_by_mass(sorted_animals, 44)
    print_by_mass(sorted_animals, 100)
    
    # 5. Группы с одинаковой массой
    print_mass_groups(sorted_animals)
    
    # Дополнительно: статистика
    print_statistics(sorted_animals)
    
    # Дополнительно: примеры по видам
    print_animals_by_species(sorted_animals, "лиса")
    print_animals_by_species(sorted_animals, "слон")