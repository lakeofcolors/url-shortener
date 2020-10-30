import functools


def base_view(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            print("{} is running".format(func.__name__))
            return func(*args, **kwargs)
        except Exception as error:
            print(error)
            return error

    return wrapper
