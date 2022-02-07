from typing import Any, List


class SelectionSort:
    def __init__(self, datas: list) -> None:
        self.datas = datas

    def is_empty(self) -> bool:
        """Check if stack is empty or not.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return len(self.datas) == 0

    def __ascending(self) -> List[Any]:
        """Order in ascending

        Returns:
            List[Any]: Get all data in ascending list format.
        """
        for i in range(len(self.datas) - 1):
            index_min_value = i
            for j in range(i + 1, len(self.datas)):
                if self.datas[j] < self.datas[index_min_value]:
                    index_min_value = j
            if index_min_value != i:
                self.datas[index_min_value], self.datas[i] = self.datas[i], self.datas[index_min_value]
        return self.datas

    def __descending(self) -> List[Any]:
        """Order in descending.

        Returns:
            List[Any]: Get all data in descending list format.
        """
        for i in range(len(self.datas) - 1):
            index_min_value = i
            for j in range(i + 1, len(self.datas)):
                if self.datas[j] > self.datas[index_min_value]:
                    index_min_value = j
            if index_min_value != i:
                self.datas[index_min_value], self.datas[i] = self.datas[i], self.datas[index_min_value]
        return self.datas

    def sort(self, mode: str) -> str:
        """Sort value by ascending or descending mode.

        Args:
            mode (str): asc (sorting in ascending) and desc (sorting in descending).

        Returns:
            str: If list is empty and mode not found function will return message else sorted list by mode.
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
        """Get all in string format.

        Returns:
            str: if list is empty return message else all data in format string.
        """
        return "List is empty." if self.is_empty() else str(self.datas)
