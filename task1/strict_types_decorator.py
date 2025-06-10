import inspect
from functools import wraps


def strict(func):
    """
    A decorator that enforces strict typing rules on function arguments.

    Ensures that:
        - All function parameters are explicitly annotated.
        - No parameters have default values.
        - Annotations only use allowed types: bool, int, float, str.

    Args:
        func : The function to validate and wrap.

    Returns:
        The wrapped function with validation logic.

    Raises:
        TypeError:
            - If any parameter is missing an annotation.
            - Any parameter has a default value.
            - Any annotation is not in the allowed types.
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        TYPES_ALLOWED = (bool, int, float, str)

        func_sign = inspect.signature(func)
        parameters = func_sign.parameters

        for name, param in parameters.items():
            if param.default != inspect._empty:
                raise TypeError(f"Argument {name} was passed with a default value")
            elif param.annotation == inspect._empty:
                raise TypeError(f"Argument {name} was passed without annotation")
            elif param.annotation not in TYPES_ALLOWED:
                raise TypeError(f"Type {param.annotation.__name__} of argument '{name}' is not allowed!")

        return func(*args, **kwargs)

    return wrapped_func
