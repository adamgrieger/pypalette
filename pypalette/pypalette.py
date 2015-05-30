from statistics import mean
from kmeans import KMeans


def average_color(rgb, prec=0):
    """Returns the average color of an image.

    The calculated average is just a simple arithmetic mean.

    Note:
        This function should work with HSV and HSL values too, but I wouldn't
        count on it.

    Args:
        rgb: An image as a list of RGB tuples.
        prec: Optional int for RGB value decimal precision,
            defaults to 0.

    Returns:
        The average color as an RGB tuple.
    """
    r_avg = mean([px[0] for px in rgb])
    g_avg = mean([px[1] for px in rgb])
    b_avg = mean([px[2] for px in rgb])

    return round(r_avg, prec), round(g_avg, prec), round(b_avg, prec)
