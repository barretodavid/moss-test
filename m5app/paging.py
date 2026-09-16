MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100

def page_size(value):
    return min(value, MAX_PAGE_SIZE)

def default_page_size():
    return 12
