from hashlib import new


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


# Inisialisasi beberapa node
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

# Hubungkan setiap node dengan next
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

# Hubungkan setiap node dengan prev
node_5.prev = node_4
node_4.prev = node_3
node_3.prev = node_2
node_2.prev = node_1

# Ambil semua data dari kiri ke kanan
print("Semua data dari kiri ke kanan: ", end="")
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Ambil semua data dari kanan ke kiri
print("\nSemua data dari kanan ke kiri: ", end="")
current_node = node_5
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.prev

# Masukkan data dari head
print("\nSetelah data dimasukkan dari head: ", end="")
new_node = Node(0)
new_node.next = node_1
node_1.prev = new_node
node_1 = new_node

current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Masukkan data dari tail
print("\nSetelah data dimasukkan dari tail: ", end="")
current_node = node_1
for _ in range(5):
    current_node = current_node.next

new_node = Node(6)
current_node.next = new_node
new_node.prev = current_node
current_node = node_5 = new_node

current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Masukkan data berdasarkan indeks tertentu
index = 3
current_node = node_1
for _ in range(index):
    current_node = current_node.next

new_node = Node(7)
current_node.prev.next = new_node
new_node.prev = current_node.prev
new_node.next = current_node
current_node.prev = new_node

# Ambil semua data dari kiri ke kanan
print("\nSemua data dari kiri ke kanan: ", end="")
current_node = node_1
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Ambil semua data dari kanan ke kiri
print("\nSemua data dari kanan ke kiri: ", end="")
current_node = node_5
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.prev
