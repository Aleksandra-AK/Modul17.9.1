from Node import Node


class List:
    def __init__(self):
        self.first = None
        self.last = None

    def pop_left(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def pop_right(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный

    def sort(self):
        current_last = self.last
        current = self.last
        while self.first is not current:
            current = self.first
            previous = None
            while current is not current_last:
                print(current.value)
                print(self)
                if current.value > current.next.value:
                    if current is not self.first:
                        pass
                    else:
                        pass
                if current.next is current_last:
                    break
                previous = current
                current = current.next
            current_last = previous
            print(self)
        # return self

    def binary_find_position(self):
        pass

    def push_left(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def push_right(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def sorting_list(self, left_first_node, right_first_node):
        result_list = List()
        # print(result_list)
        while (left_first_node is not None) and (right_first_node is not None):
            #     a, b = ,
            # print(f"a={a}, b={b}")
            if left_first_node.value < right_first_node.value:
                result_list.push_right(left_first_node.value)
                left_first_node = left_first_node.next
            else:
                result_list.push_right(right_first_node.value)
                right_first_node = right_first_node.next
        if left_first_node is None:
            result_list.last.next = right_first_node
        else:
            result_list.last.next = left_first_node
        print(result_list.first)
        return self

    def split_list(self):
        first_node = self.first
        if first_node.next is None:
            return first_node
        left_start = first_node
        right_start = first_node.next
        while (right_start is not None) and (right_start.next is not None):
            left_start = left_start.next
            right_start = right_start.next.next
        right_start = left_start.next
        left_start.next = None
        left_start = first_node
        # print(right_start)
        # print(first_node)
        self = List()
        return self.sorting_list(self.split_list(left_start), self.split_list(right_start))

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный

    def __str__(self):
        string = ''
        for node in self:
            if node.next is None:
                string += str(node.value)
            else:
                string += str(node.value) + "->"
        return string

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count


if __name__ == '__main__':
     pass

