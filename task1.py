class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Метод реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Метод сортування однозв'язного списку (сортування злиттям)
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(left, right):
            dummy = Node()
            tail = dummy
            while left and right:
                if left.data <= right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next

        def merge_sort_rec(head):
            if head is None or head.next is None:
                return head
            left, right = split(head)
            left = merge_sort_rec(left)
            right = merge_sort_rec(right)
            return merge(left, right)

        self.head = merge_sort_rec(self.head)

    # Метод об'єднання двох відсортованих однозв'язаних списка в один відсортований список
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        a, b = list1.head, list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Приклад використання:
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(4)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(3)
list2.insert_at_end(6)

# Об'єднання
merged = LinkedList.merge_sorted_lists(list1, list2)
print("Об'єднаний список:")
merged.print_list()

# Реверсування
print("Реверсований список:")
merged.reverse()
merged.print_list()

# Сортування
print("Відсортованный список:")
merged.merge_sort()
merged.print_list()