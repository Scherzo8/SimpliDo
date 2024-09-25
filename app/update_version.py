import toml



def get_version() -> str:
    """
    Retrieve the application version from the pyproject.toml file.

    Returns:
        str: The version of the application.
    """
    
    pyproject = toml.load('pyproject.toml')

    return pyproject['tool']['poetry']['version']