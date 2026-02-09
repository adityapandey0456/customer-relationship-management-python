class CRMError(Exception):
    """Base class for all CRM exceptions."""
    pass

class InvalidDataError(CRMError):
    """Raised when email or date format is incorrect."""
    pass

class DuplicateCustomerError(CRMError):
    """Raised when a Customer ID already exists."""
    pass

class ExportError(CRMError):
    """Raised when file export fails."""
    pass