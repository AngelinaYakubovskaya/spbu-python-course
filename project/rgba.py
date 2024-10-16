def rgba_vector(index):
    """
    Returns the RGBA vector at the specified index, where the alpha channel is even.

    The RGBA values are generated from 0 to 255 for red, green, and blue, and
    from 0 to 100 (even numbers only) for the alpha channel.

    Args:
        index (int): The index of the RGBA vector to retrieve.

    Returns:
        tuple: The RGBA vector as a tuple (r, g, b, a), or None if the index is out of bounds.
    """
    rgba_gen = (
        (r, g, b, a)
        for r in range(256)
        for g in range(256)
        for b in range(256)
        for a in range(0, 101, 2)
    )

    try:
        # Using islice to directly get the element at the given index
        from itertools import islice

        return next(islice(rgba_gen, index, index + 1))
    except StopIteration:
        return None
