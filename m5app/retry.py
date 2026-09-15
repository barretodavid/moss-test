MIN_RETRY_COUNT = 1
MAX_RETRY_COUNT = 5

def retry_count(value):
    return max(MIN_RETRY_COUNT, min(value, MAX_RETRY_COUNT))
