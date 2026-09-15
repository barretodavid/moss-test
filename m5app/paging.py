MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 100

def page_size(value):
    return max(min(value, MAX_PAGE_SIZE), MIN_PAGE_SIZE)
