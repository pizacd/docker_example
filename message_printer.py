"""Python script to generate a welcome message.
Very simple, exercise is more for executing code
in a Docker container"""

def say_hello(name: str) -> str:
    """returns a welcome message
    Args:
    name: str, name of the entity we wish to greet"""
    msg = f"Hello {name}!"
    return msg

if __name__=="__main__":
    print(say_hello("GitHub"))
