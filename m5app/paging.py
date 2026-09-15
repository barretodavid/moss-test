MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100
DEFAULT_PAGE_SIZE = 20

def page_size(value):
    if value is None:
        return DEFAULT_PAGE_SIZE
    return max(MIN_PAGE_SIZE, min(value, MAX_PAGE_SIZE))
