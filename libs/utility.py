def to_bool(value, default: bool = False) -> bool:
    """Convert common truthy/falsy values to bool.

    Accepts booleans, numbers (0/1), and strings like
    "true/false", "yes/no", "on/off", "1/0" (case-insensitive).
    If value is None, returns the provided default (False by default).
    Raises ValueError only for unrecognized non-None, non-empty inputs.
    """

    if value is None:
        return default

    if isinstance(value, bool):
        return value

    if isinstance(value, (int, float)):
        return bool(value)

    if isinstance(value, str):
        val = value.strip().lower()
        # Common truthy/falsy sets
        truthy = {"1", "true", "t", "yes", "y", "on"}
        falsy = {"0", "false", "f", "no", "n", "off", ""}
        if val in truthy:
            return True
        if val in falsy:
            return False

    raise ValueError("Value was not recognized as a valid Boolean.")
