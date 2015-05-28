from statistics import mean
from kmeans import KMeans


def average_color(rgb):
    """Returns the average color of an image.

    The calculated average is just a simple arithmetic mean.

    Note:
        This function should work with HSV and HSL values too, but I wouldn't
        count on it.

    Args:
        rgb: An image as a list of RGB tuples.

    Returns:
        The average color as an RGB tuple.
    """
    r_avg = mean([px[0] for px in rgb])
    g_avg = mean([px[1] for px in rgb])
    b_avg = mean([px[2] for px in rgb])

    return r_avg, g_avg, b_avg
