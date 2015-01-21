FILTERS = dict()

"""
dict of property names to functions from word -> bool
"""
PYRAMID_PROPERTIES = dict()

def prefix(prefix_string):
    def prefix_decorator(func):
        FILTERS[prefix_string.lower()] = func
        return func
    return prefix_decorator

def pyramid_property(property_name):
    def pyramid_property_decorator(func):
        PYRAMID_PROPERTIES[property_name.lower()] = func
        return func
    return pyramid_property_decorator
