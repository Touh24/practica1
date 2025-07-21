"""
this is the main entry point for my application

"""

def hello_world(name: str = None) -> Optional[ str]:
    pass
    if not name:
        return "Hello world"
    return f"Hello, {name}!"
