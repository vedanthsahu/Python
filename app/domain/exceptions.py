class AuthenticationError(Exception):
    """
    Raised when authentication fails due to:
    - wrong password
    - unknown username
    - invalid token
    """
    pass


class AuthorizationError(Exception):
    """
    Raised when user tries to access a resource
    without proper permissions.
    """
    pass
class AuthenticationError(Exception):
    pass


class AuthorizationError(Exception):
    pass


class BookNotFoundError(Exception):
    """
    Raised when a book ID does not exist.
    """
    pass


class DuplicateBookError(Exception):
    """
    Raised when trying to create a book with same title+author.
    """
    pass

