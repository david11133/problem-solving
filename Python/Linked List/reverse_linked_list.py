lass ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next  

def reversed_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# print the linked list
def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3)))

print_linked_list(head)

reversed_head = reversed_linked_list(head)

print_linked_list(reversed_head)
