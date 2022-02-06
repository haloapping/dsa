from typing import Any, List


class SelectionSort:
    def __init__(self, datas: list) -> None:
        self.datas = datas

    def is_empty(self) -> bool:
        return len(self.datas) == 0

    def __ascending(self) -> List[Any]:
        for i in range(len(self.datas) - 1):
            index_min_value = i
            for j in range(i + 1, len(self.datas)):
                if self.datas[j] < self.datas[index_min_value]:
                    index_min_value = j
            if index_min_value != i:
                self.datas[index_min_value], self.datas[i] = self.datas[i], self.datas[index_min_value]
        return self.datas

    def __descending(self) -> List[Any]:
        for i in range(len(self.datas) - 1):
            index_min_value = i
            for j in range(i + 1, len(self.datas)):
                if self.datas[j] > self.datas[index_min_value]:
                    index_min_value = j
            if index_min_value != i:
                self.datas[index_min_value], self.datas[i] = self.datas[i], self.datas[index_min_value]
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
            return f"Mode {mode} not available."

    def print(self) -> str:
        return "List is empty." if self.is_empty() else str(self.datas)
