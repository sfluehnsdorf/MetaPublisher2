"""JSONDict."""


__all__ = [
    'JSONDict',
]


# ============================================================================
# JSONDict Mix-In Class

class JSONDict:
    """JSONDict Mix-In Class."""

    # !!! jsondict.py - implement encode_JSONDict

    def encode_JSONDict(self, mapping):
        """Encode JSONDict."""
        raise NotImplementedError

    # !!! jsondict.py - implement decode_JSONDict

    def decode_JSONDict(self, json):
        """Decode JSONDict."""
        raise NotImplementedError
