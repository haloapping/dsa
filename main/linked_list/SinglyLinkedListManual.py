from math import ceil
import string


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# Tanpa menggunakan head dan tail
# Initialize 5 nodes
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

# Sambungkan kelima node dengan next
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

# Ambil semua nilai node dari kiri ke kanan
print("Data dari kiri ke kanan: ", end="")
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

print()

# Masukkan data dari head
print("Setelah memasukkan data dari head: ", end="")
new_node = Node(0)
new_node.next = node_1
node_1 = new_node
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

print()

# Memasukkan data dari tail
current_node = node_1
for _ in range(5):
    current_node = current_node.next
new_node = Node(6)
current_node.next = new_node

print("Setelah memasukkan data dari tail: ", end="")
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

print()

# Memasukkan data berdasarkan indeks tertentu
index = 3
current_node = node_1
for _ in range(index):
    prev_node = current_node
    current_node = current_node.next
new_node = Node(7)
new_node.next = current_node
prev_node.next = new_node

print("Setelah memasukkan data dari indeks tertentu: ", end="")
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next
print()

# Ambil dari berdasarkan indeks tertentu
index = 1
current_node = node_1
for _ in range(index):
    current_node = current_node.next
print(f"Data indeks ke-{index}: {current_node.data}", end="")

# Menggunakan head dan tail
# Initialize head, tail, dan 5 nodes
head = tail = None
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

print("\n\nMenggunakan head dan tail")
# Sambungkan kelima node dengan next
head = node_1
head.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
tail = node_5

# Ambil semua nilai node
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Masukkan data dari head
new_node = Node(0)
new_node.next = head
head = new_node

print("\nSetelah memasukkan data dari head:", end="")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Masukkan data dari tail
new_node = Node(6)
tail.next = new_node
tail = new_node

print("\nSetelah memasukkan data dari tail:", end="")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next
print()
