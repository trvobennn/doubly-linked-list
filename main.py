"""
My version of a doubly linked list
"""

class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.previous = previous
        self.succeeding = succeeding

class LinkedList:
    def __init__(self):
        self.main_list = {}
        self.last_value = None
        self.first_value = None
    def push(self, value):
        if self.last_value:
            new_node = Node(value, previous=self.last_value)
            self.main_list[self.last_value].succeeding = value
            self.main_list[value] = new_node
            self.last_value = value
        if self.last_value is None:
            new_node = Node(value)
            self.main_list[value] = new_node
            self.last_value = value
            self.first_value = value

    def pop(self):
        if self.first_value:
            prev_ = self.main_list[self.last_value].previous
            pop_value = self.last_value
            self.main_list.pop(pop_value)
            self.last_value = prev_
            if prev_ is not None:
                self.main_list[prev_].succeeding = None
            return pop_value
    def shift(self):
        if self.first_value:
            next_ = self.main_list[self.first_value].succeeding
            shift_val = self.first_value
            self.main_list.pop(shift_val)
            self.first_value = next_
            if next_ is not None:
                self.main_list[next_].previous = None
            return shift_val

    def unshift(self, value):
        if self.first_value:
            new_node = Node(value, succeeding=self.first_value)
            self.main_list[self.first_value].previous = value
            self.main_list[value] = new_node
            self.first_value = value
        if self.first_value is None:
            new_node = Node(value)
            self.main_list[value] = new_node
            self.last_value = value
            self.first_value = value