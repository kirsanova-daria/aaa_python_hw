
def count_letters(word) -> tuple[int, int]:
    """
    Counts letters in a word
    >>> count_letters('')
    (0, 0)
    >>> count_letters('Hello world!')
    (10, 2)
    >>> count_letters('.')
    (0, 1)
    """
    return (lt := sum(1 for x in word if x.isalpha()), len(word) - lt)






