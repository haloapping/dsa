from typing import Any


class InsertionSort:
    def __init__(self, datas: list) -> None:
        self.datas = datas

    def is_empty(self) -> bool:
        return len(self.datas) == 0

    def __ascending(self) -> list[Any]:
        for insert_index, insert_value in enumerate(self.datas[1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value < self.datas[insert_index]:
                self.datas[insert_index + 1] = self.datas[insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                self.datas[insert_index + 1] = insert_value
        return self.datas

    def __descending(self) -> list[Any]:
        for insert_index, insert_value in enumerate(self.datas[1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value > self.datas[insert_index]:
                self.datas[insert_index + 1] = self.datas[insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                self.datas[insert_index + 1] = insert_value
        return self.datas

    def sort(self, mode: str) -> str:
        """
        There are two modes:
            - asc: sorting in ascending.
            - desc: sorting in descending.
        """
        if self.is_empty():
            return "List is empty."
        elif mode == "asc":
            return str(self.__ascending())
        elif mode == "desc":
            return str(self.__descending())
        else:
            return f"Mode {mode} is not available."

    def print(self):
        return "List is empty." if self.is_empty() else str(self.datas)
