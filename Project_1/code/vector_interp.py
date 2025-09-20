def vector_interp(p1, p2, V1, V2, coord, dim):
    """
    Calculates the interpolated vector value using linear interpolation.

    :param p1: Point 1 (x1, y1)
    :param p2: Point 2 (x2, y2)
    :param V1: Vector at point p1
    :param V2: Vector at point p2
    :param coord: Coordinate of the point p (either x or y)
    :param dim: 1 if interpolating along x, 2 if along y
    :return: Interpolated vector V at the given coordinate
    """

    # Choose the appropriate axis (x or y) for distance calculation
    if dim == 1:
        denominator = p2[0] - p1[0]
    elif dim == 2:
        denominator = p2[1] - p1[1]
    else:
        raise ValueError("dim must be 1 (x) or 2 (y)")

    # Avoid division by zero (when points have the same x or y value)
    if abs(denominator) < 1e-10:
        return V1  # Could also return V2, since they should be equal in this case

    # Compute the interpolation factor t between the two points
    if dim == 1:
        t = (coord - p1[0]) / denominator
    else:
        t = (coord - p1[1]) / denominator

    # Linearly interpolate between V1 and V2 based on t
    V = (1 - t) * V1 + t * V2
    return V
