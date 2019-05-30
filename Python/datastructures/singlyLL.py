class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        print("ADD_TO_FRONT::Adding to front, value: {}".format(val))
        new_node = Node(val)
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        print("ADD_TO_FRONT::Added")
        print("-"*15)
        return self

    def add_to_back(self, val):
        print("ADD_TO_BACK::Adding to back, value: {}".format(val))
        if not self.head:
            self.add_to_front(val)
            return self

        new_node = Node(val)
        runner = self.head
        while runner.next:
            runner = runner.next

        runner.next = new_node
        print("ADD_TO_BACK::Added")
        print("-"*15)
        return self

    def remove_from_front(self):
        print("REMOVE_FROM_FRONT::Removing from front")
        if not self.head:
            print("REMOVE_FROM_FRONT::List empty")
            print("-"*15)
            return self

        curr = self.head
        self.head = self.head.next
        del curr
        print("REMOVE_FROM_FRONT::Removed")
        print("-"*15)
        return self

    def remove_from_back(self):
        print("REMOVE_FROM_BACK::Removing from back")
        if not self.head:
            print("REMOVE_FROM_BACK::List empty")
            print("-"*15)
            return self

        if not self.head.next:
            del self.head
            self.head = None
            print("REMOVE_FROM_BACK::Removed head")
            print("-"*15)
            return self

        runner = self.head
        while runner.next.next:
            runner = runner.next

        temp = runner.next
        runner.next = None
        del temp
        print("REMOVE_FROM_BACK::Removed")
        print("-"*15)
        return self

    # Inserts element in list at nth with 0 based indices
    def insert_at(self, val, n):
        print("INSERT_AT::Inserting value {} at {} index".format(val, n))
        if n == 0:
            self.add_to_front(val)
            return self

        runner = self.head
        while n > 1 and runner.next:
            runner = runner.next
            n -= 1

        new_node = Node(val)
        new_node.next = runner.next
        runner.next = new_node
        print("INSERT_AT::Inserted")
        print("-"*15)
        return self

    def remove_val(self, val):
        print("REMOVE_VAL::Deleting value {}".format(val))
        if self.head == None:
            print("REMOVE_VAL::List empty.")
            print("-"*15)
            return self

        if self.head.value == val:
            self.remove_from_front()

        runner = self.head.next
        prev = self.head
        while runner.next and runner.value != val:
            prev = runner
            runner = runner.next

        # Didn't find the value
        if runner.value != val:
            print("REMOVE_VAL::Value not found.")
            print("-"*15)
            return self

        prev.next = runner.next
        runner.next = None
        del runner
        print("REMOVE_VAL::Deleted.")
        print("-"*15)
        return self

    def print_values(self):
        print("PRINT_VALUES::Printing.")
        runner = self.head

        while runner:
            print(runner.value)
            runner = runner.next

        print("-"*15)
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front(
    "Linked lists").add_to_back("fun!").add_to_front("huh").add_to_back("loooo").print_values()

# my_list.remove_from_front().print_values().remove_from_back().print_values()

my_list.insert_at("INSERTED", 4).print_values()
my_list.remove_val("INSERTED").remove_val("lo").print_values()
