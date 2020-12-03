"""Helper functions that are used in multiple scripts"""

def readlines(file_path: str, strip_newline_char: bool = True) -> list:
    """
    Reads in the given file and returns its contents as a list
    
    Parameters
    ----------
    file_path : str
        The path of the file to read
    strip_newline_char : bool
        If true, the \n characters are removed at the end
        of each new line, if false, they are not removed

    Returns
    -------
    lines : list
        All lines in the file as a list
    """
    with open(file_path) as f:
        if strip_newline_char:
            lines = f.read().splitlines()
        else:
            lines = f.readlines()

    return lines