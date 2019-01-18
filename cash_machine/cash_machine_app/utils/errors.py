class Error(Exception):
    """Base exception class"""

class NoteUnavailableException(Error):
    """Raised when the amount asked for is not possible with the available banknote denominations"""
    pass