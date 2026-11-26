
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    pass
    dot=0
    mag=0
    for i in range(len(v)):
        dot += v[i] * L[i]
        mag += L[i] ** 2

    res = []

    for i in range(len(L)):
        res.append((dot / mag) * L[i])

    return res
