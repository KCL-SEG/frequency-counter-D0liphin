def frequencies(items: list[any]) -> dict[str, int]:
    """
    Converts a list of items to a dictionary of string: frequency
    pairs.
    """
    frequencies = {}
    for item in items:
        k = str(item)
        frequencies[k] = frequencies.get(k, 0) + 1
    return frequencies
