import typing


def frequencies(items: typing.List[typing.Any]) -> typing.Dict[str, int]:
    """
    Converts a list of items to a dictionary of string: frequency
    pairs.
    """
    frequencies = {}
    for item in items:
        k = str(item)
        frequencies[k] = frequencies.get(k, 0) + 1
    return frequencies
