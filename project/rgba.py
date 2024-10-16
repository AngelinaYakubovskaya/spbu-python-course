def rgba_vector(index):
    """
    Generate a 4D RGBA vector where alpha takes only even values.

    Args:
        index (int): The index of the RGBA vector to retrieve (1-based index).

    Returns:
        tuple: A tuple representing the RGBA vector (R, G, B, A) or None if the index is out of range.
    """
    if not isinstance(index, int):
        return None  # Could also raise an error
    if index < 1:
        return None  # Could also raise an error
    max_elements = 256 * 256 * 256 * 51  # Total possible RGBA values
    if index > max_elements:
        return None  # Could also raise an error

    # Calculate the 0-based index
    zero_based_index = index - 1

    # Calculate the alpha index and value
    alpha_index = zero_based_index % 51  # Total alpha values
    alpha_value = alpha_index * 2  # Even values: 0, 2, ..., 100

    # Calculate the RGB index
    rgb_index = zero_based_index // 51

    # Calculate R, G, B values
    r_value = (rgb_index // (256 * 256)) % 256
    g_value = (rgb_index // 256) % 256
    b_value = rgb_index % 256

    return (r_value, g_value, b_value, alpha_value)
