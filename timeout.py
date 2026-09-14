def normalize_timeout(seconds):
    """Clamp whole seconds to the inclusive range 1 through 60."""
    return min(60, max(0, seconds))
