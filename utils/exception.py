#!/bin/python

"""Generic exceptions
"""


class TemplateIdNotFound(Exception):
    """Exception raised with invalid template id"""

class TemplateIdMissing(Exception):
    """Exception raised with missing template id"""

class CRCreationError(Exception):
    """Raised when http status is other than 200"""
