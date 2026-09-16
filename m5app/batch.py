from m5app.paging import page_size

def page_sizes(values):
    return [page_size(value) for value in values]
