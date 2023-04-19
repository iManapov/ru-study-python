class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Replace all positive elements of an integer list
        with the maximum value of elements of the list.

        :param input_list: Origin list
        :return: Replaced list
        """

        if not input_list:
            return input_list

        max_el = ListExercise.find_max(input_list)
        return [max_el if el > 0 else el for el in input_list]

    @staticmethod
    def find_max(input_list: list[int]) -> int:
        """
        Finding maximum element of the list.

        :param input_list: Origin list
        :return: Max element
        """

        max_el = 0
        for el in input_list:
            if el > max_el:
                max_el = el
        return max_el

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Returns index of searching element.

        :param input_list: Origin list
        :param query: Searching element
        :return: Element index
        """

        if not input_list:
            return -1

        return ListExercise.binary_search(input_list, query, 0, len(input_list) - 1)

    @staticmethod
    def binary_search(input_list: list[int], query: int, left: int, right: int) -> int:
        """
        Binary search in list.

        :param input_list: Origin list
        :param query: Searching element
        :param left: Left index
        :param right: Right index
        :return: Element index
        """
        if left > right:
            return -1

        mid = (left + right) // 2

        if input_list[mid] == query:
            return mid
        elif input_list[mid] > query:
            return ListExercise.binary_search(input_list, query, left, mid - 1)
        else:
            return ListExercise.binary_search(input_list, query, mid + 1, right)
