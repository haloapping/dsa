from typing import Any, List


class BubbleSort:
    def __init__(self, datas: List[Any]) -> None:
        self.datas = datas
        self.swapped = False

    def __is_empty(self) -> bool:
        return len(self.datas) == 0

    def __ascending(self) -> List[Any]:
        for i in range(len(self.datas)):
            for j in range(len(self.datas) - i - 1):
                if self.datas[j] > self.datas[j + 1]:
                    self.datas[j], self.datas[j +
                                              1] = self.datas[j + 1], self.datas[j]
                    self.swapped = True
            if not self.swapped:
                break
        return self.datas

    def __descending(self) -> List[Any]:
        for i in range(len(self.datas)):
            for j in range(len(self.datas) - i - 1):
                if self.datas[j] < self.datas[j + 1]:
                    self.datas[j], self.datas[j +
                                              1] = self.datas[j + 1], self.datas[j]
                    self.swapped = True
            if not self.swapped:
                break
        return self.datas

    def sort(self, mode: str) -> str:
        """
        There are two modes:
            - asc: sorting in ascending.
            - desc: sorting in descending.
        """
        if self.__is_empty():
            return "List is empty"
        elif mode == "asc":
            return str(self.__ascending())
        elif mode == "desc":
            return str(self.__descending())
        else:
            return f"Mode {mode} not found."

    def print(self) -> str:
        return "List of data is empty." if self.__is_empty() else str(self.datas)
