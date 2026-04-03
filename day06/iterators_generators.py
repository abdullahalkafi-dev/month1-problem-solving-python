def even_number_generator(start: int, end: int):
    if not isinstance(start, int):
        raise TypeError("start data type not allowed")
    if not isinstance(end, int):
        raise TypeError("end data type not allowed")

    current = start
    if current % 2 != 0:
        current = current + 1

    while current <= end:
        yield current
        current = current + 2


class RunningSum:
    def __init__(self, numbers: list[int]):
        if not isinstance(numbers, list):
            raise TypeError("numbers data type not allowed")
        for number in numbers:
            if not isinstance(number, int):
                raise TypeError("numbers item data type not allowed")

        self.numbers = numbers
        self.index = 0
        self.total = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration

        self.total = self.total + self.numbers[self.index]
        self.index = self.index + 1
        return self.total


def safe_int_parse(values: list[str]) -> list[int]:
    if not isinstance(values, list):
        raise TypeError("values data type not allowed")

    parsed_values = []
    for value in values:
        try:
            parsed_values.append(int(value))
        except (ValueError, TypeError):
            continue
    return parsed_values
