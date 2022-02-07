from typing import Any, List


class BubbleSort:
    def __init__(self, datas: List[Any]) -> None:
        self.datas = datas
        self.swapped = False

    def __is_empty(self) -> bool:
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
        """Order in descending.

        Returns:
            List[Any]: Get all data in descending list format.
        """
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
        """Sort value by ascending or descending mode.

        Args:
            mode (str): asc (sorting in ascending) and desc (sorting in descending).

        Returns:
            str: If list is empty and mode not found function will return message else sorted list by mode.
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
        """Get all in string format.

        Returns:
            str: if list is empty return message else all data in format string.
        """
        return "List of data is empty." if self.__is_empty() else str(self.datas)
