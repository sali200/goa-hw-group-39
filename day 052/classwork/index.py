
def hello(name=None):
    if not name:
        return "Hello, World!"
    return f"Hello, {name.capitalize()}"

