def rgba_vector(index):
    """
    Generate a 4D RGBA vector where alpha takes only even values.

    Args:
        index (int): The index of the RGBA vector to retrieve.

    Returns:
        tuple: A tuple representing the RGBA vector (R, G, B, A) or None if the index is out of range.
    """
    from itertools import islice

    # Using a generator expression to create RGBA values
    rgba_gen = (
        (r, g, b, a)
        for r in range(256)
        for g in range(256)
        for b in range(256)
        for a in range(0, 101, 2)
    )

    # Using islice to directly get the element at the given index
    try:
        return next(islice(rgba_gen, index, index + 1))
    except StopIteration:
        return None
