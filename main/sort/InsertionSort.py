from typing import Any, List


class InsertionSort:
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
        for insert_index, insert_value in enumerate(self.datas[1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value < self.datas[insert_index]:
                self.datas[insert_index + 1] = self.datas[insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                self.datas[insert_index + 1] = insert_value
        return self.datas

    def __descending(self) -> List[Any]:
        """Order in descending.

        Returns:
            List[Any]: Get all data in descending list format.
        """
        for insert_index, insert_value in enumerate(self.datas[1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value > self.datas[insert_index]:
                self.datas[insert_index + 1] = self.datas[insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                self.datas[insert_index + 1] = insert_value
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
            return f"Mode {mode} is not available."

    def print(self) -> str:
        """Get all in string format.

        Returns:
            str: if list is empty return message else all data in format string.
        """
        return "List is empty." if self.is_empty() else str(self.datas)
