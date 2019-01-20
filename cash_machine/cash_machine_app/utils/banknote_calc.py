from .errors import NoteUnavailableException


def get_notes(amount):
    if amount < 0:
        raise ValueError("amount must be positive")
    remaining = amount
    denominations = [100.0, 50.0, 20.0, 10.0]
    notes = []
    for denom in denominations:
            while remaining >= denom:
                notes.append(denom)
                remaining -= denom
                if remaining < min(denominations) and remaining != 0.0:
                    raise NoteUnavailableException("that amount cannot be given with the available banknote denominations")
    return notes