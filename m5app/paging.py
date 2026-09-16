MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100
DEFAULT_PAGE_SIZE = 20

def page_size(value):
    if value is None:
        return DEFAULT_PAGE_SIZE
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("page size must be an integer or None")
    return max(min(value, MAX_PAGE_SIZE), MIN_PAGE_SIZE)
