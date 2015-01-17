FILTERS = dict()

def prefix(prefix_string):
    def prefix_decorator(func):
        FILTERS[prefix_string] = func
        return func
    return prefix_decorator
