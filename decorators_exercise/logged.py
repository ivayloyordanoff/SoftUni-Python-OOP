def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}" \
               f"({', '.join(str(arg) for arg in args)})\n" \
               f"it returned {func(*args)}"

    return wrapper
