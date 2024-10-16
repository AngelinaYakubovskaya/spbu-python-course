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

    # Calculate the alpha value
    a_index = index % total_alpha  # Index for Alpha
    alpha_value = a_index * 2  # Convert to even value (0, 2, ..., 100)

    # Calculate the RGB index without alpha
    rgb_index = index // total_alpha

    r_index = (rgb_index // (total_colors**2)) % total_colors
    g_index = (rgb_index // total_colors) % total_colors
    b_index = rgb_index % total_colors

    # Return the RGBA vector
    return (r_index, g_index, b_index, alpha_value)
