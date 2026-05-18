import time
from typing import Any, Optional

# ==================== ОДНОСВЯЗНЫЙ СПИСОК ====================

class NodeSingly:
    # Узел односвязного списка
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class SinglyLinkedList:
    # Односвязный список
    def __init__(self):
        self.head = None
        self._size = 0
    
    def insert_at_end(self, data: Any) -> None:
        # Вставка в конец списка - O(n)
        new_node = NodeSingly(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def insert_at_index(self, index: int, data: Any) -> bool:
        # Вставка по индексу - O(n)
        if index < 0 or index > self._size:
            return False
        
        new_node = NodeSingly(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self._size += 1
        return True
    
    def set_at_index(self, index: int, data: Any) -> bool:
        # Изменение значения по индексу - O(n)
        if index < 0 or index >= self._size:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data
        return True
    
    def index_of(self, data: Any) -> int:
        # Нахождение индекса первого вхождения - O(n)
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def __len__(self) -> int:
        return self._size
    
    def to_list(self) -> list:
        # Вспомогательный метод для проверки
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# ==================== ДВУСВЯЗНЫЙ СПИСОК ====================

class NodeDoubly:
    # Узел двусвязного списка
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Двусвязный список
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def insert_at_end(self, data: Any) -> None:
        # Вставка в конец списка - O(1)
        new_node = NodeDoubly(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def insert_at_index(self, index: int, data: Any) -> bool:
        # Вставка по индексу - O(n), но с оптимизацией обхода
        if index < 0 or index > self._size:
            return False
        
        new_node = NodeDoubly(data)
        
        if index == 0:
            # Вставка в начало
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        elif index == self._size:
            # Вставка в конец
            self.insert_at_end(data)
            return True
        else:
            # Оптимизация: идем с начала или с конца
            if index < self._size // 2:
                # Идем с начала
                current = self.head
                for _ in range(index):
                    current = current.next
            else:
                # Идем с конца
                current = self.tail
                for _ in range(self._size - index - 1):
                    current = current.prev
            
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        
        self._size += 1
        return True
    
    def set_at_index(self, index: int, data: Any) -> bool:
        # Изменение значения по индексу - O(n) с оптимизацией
        if index < 0 or index >= self._size:
            return False
        
        # Оптимизация обхода
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - index - 1):
                current = current.prev
        
        current.data = data
        return True
    
    def index_of(self, data: Any) -> int:
        # Нахождение индекса первого вхождения - O(n)
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def __len__(self) -> int:
        return self._size
    
    def to_list(self) -> list:
        # Вспомогательный метод для проверки
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def to_list_reverse(self) -> list:
        # Вспомогательный метод: обход с конца
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result


# ==================== ТЕСТИРОВАНИЕ И СРАВНЕНИЕ ====================

def test_list_operations(list_obj, name: str):
    # Тест базовых операций
    print(f"\n=== Тестирование {name} ===")
    
    # Вставка в конец
    for i in range(5):
        list_obj.insert_at_end(i)
    print(f"После вставки в конец [0-4]: {list_obj.to_list()}")
    
    # Вставка по индексу
    list_obj.insert_at_index(0, 10)
    print(f"Вставка 10 в начало: {list_obj.to_list()}")
    
    list_obj.insert_at_index(3, 20)
    print(f"Вставка 20 по индексу 3: {list_obj.to_list()}")
    
    list_obj.insert_at_index(len(list_obj), 30)
    print(f"Вставка 30 в конец: {list_obj.to_list()}")
    
    # Изменение по индексу
    list_obj.set_at_index(2, 999)
    print(f"Изменение индекса 2 на 999: {list_obj.to_list()}")
    
    # Поиск индекса
    idx = list_obj.index_of(20)
    print(f"Индекс первого вхождения 20: {idx}")
    
    idx = list_obj.index_of(999)
    print(f"Индекс первого вхождения 999: {idx}")
    
    idx = list_obj.index_of(100)
    print(f"Индекс первого вхождения 100 (нет): {idx}")


def benchmark_lists():
    # Сравнение производительности
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        print(f"\n--- Размер списка: {size} элементов ---")
        
        # Односвязный список
        sll = SinglyLinkedList()
        for i in range(size):
            sll.insert_at_end(i)
        
        # Двусвязный список
        dll = DoublyLinkedList()
        for i in range(size):
            dll.insert_at_end(i)
        
        # Тест: вставка в конец
        start = time.perf_counter()
        sll.insert_at_end(999)
        time_sll_end = time.perf_counter() - start
        
        start = time.perf_counter()
        dll.insert_at_end(999)
        time_dll_end = time.perf_counter() - start
        
        print(f"Вставка в конец:")
        print(f"  Односвязный: {time_sll_end:.8f} сек (O(n))")
        print(f"  Двусвязный:  {time_dll_end:.8f} сек (O(1))")
        print(f"  Ускорение:   {time_sll_end/time_dll_end:.2f}x")
        
        # Тест: вставка в середину
        mid = size // 2
        start = time.perf_counter()
        sll.insert_at_index(mid, 888)
        time_sll_mid = time.perf_counter() - start
        
        start = time.perf_counter()
        dll.insert_at_index(mid, 888)
        time_dll_mid = time.perf_counter() - start
        
        print(f"Вставка в середину (индекс {mid}):")
        print(f"  Односвязный: {time_sll_mid:.8f} сек")
        print(f"  Двусвязный:  {time_dll_mid:.8f} сек")
        
        # Тест: поиск элемента
        target = size - 1
        start = time.perf_counter()
        sll.index_of(target)
        time_sll_search = time.perf_counter() - start
        
        start = time.perf_counter()
        dll.index_of(target)
        time_dll_search = time.perf_counter() - start
        
        print(f"Поиск элемента {target}:")
        print(f"  Односвязный: {time_sll_search:.8f} сек")
        print(f"  Двусвязный:  {time_dll_search:.8f} сек")


# Запуск
if __name__ == "__main__":
    # Тестирование односвязного списка
    sll = SinglyLinkedList()
    test_list_operations(sll, "Односвязный список")
    
    # Тестирование двусвязного списка
    dll = DoublyLinkedList()
    test_list_operations(dll, "Двусвязный список")
    
    # Дополнительный тест обратного обхода для двусвязного
    print(f"\nОбратный обход двусвязного: {dll.to_list_reverse()}")
    
    # Бенчмарки
    benchmark_lists()
    