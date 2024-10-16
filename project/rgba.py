def rgba_vector(index):
    """
    Generate a 4D RGBA vector where alpha takes only even values.

    Args:
        index (int): The index of the RGBA vector to retrieve.

    Returns:
        tuple: A tuple representing the RGBA vector (R, G, B, A) or None if the index is out of range.
    """
    # Total number of possible values for each color channel
    total_colors = 256
    total_alpha = 51  # Alpha can be 0, 2, 4, ..., 100 (51 values)

    # Calculate total number of RGBA combinations
    total_combinations = total_colors**3 * total_alpha

    # Check if the index is out of range
    if index < 0 or index >= total_combinations:
        return None

    # Convert the index to RGBA values
    a_index = index % total_alpha  # Get the index for Alpha
    rgb_index = index // total_alpha  # Remaining index for RGB

    r_index = (rgb_index // (total_colors**2)) % total_colors
    g_index = (rgb_index // total_colors) % total_colors
    b_index = rgb_index % total_colors

    # Calculate the RGBA vector
    return (
        r_index,
        g_index,
        b_index,
        a_index * 2,
    )  # Multiply alpha index by 2 to get the correct value
