from statistics import mean
from kmeans import KMeans


def average_color(im, prec=0):
    """Returns the average color of an image.

    The calculated average is just a simple arithmetic mean.

    Note:
        This function should work with HSV and HSL values too, but I wouldn't
        count on it.

    Args:
        im: An image as a list of RGB tuples.
        prec: Optional int for RGB value decimal precision,
            defaults to 0.

    Returns:
        The average color as an RGB tuple.
    """
    r_avg = mean([px[0] for px in im])
    g_avg = mean([px[1] for px in im])
    b_avg = mean([px[2] for px in im])

    return round(r_avg, prec), round(g_avg, prec), round(b_avg, prec)


def grayscale(im, mode='luminosity'):
    """Returns a grayscale version of an image.

    The available grayscale modes are: Lightness, Average, and Luminosity.
    The Luminosity mode is the default because it more accurately represents
    human color perception.

    http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/

    Args:
        im: An image as a list of RGB tuples.
        mode: Optional string for grayscale mode selection.

    Returns:
        A grayscale version of the image as a list of RGB tuples.

    Raises:
        ValueError: If an empty image is passed or if an invalid grayscale
            mode is selected.
    """
    if len(im) == 0:
        raise ValueError('An empty image has been passed')

    gim = []    # Grayscale image list

    if mode == 'lightness':
        for px in im:
            gray = round((max(px) + min(px)) / 2)
            gim.append((gray, gray, gray))
    elif mode == 'average':
        for px in im:
            gray = round((px[0] + px[1] + px[2]) / 3)
            gim.append((gray, gray, gray))
    elif mode == 'luminosity':
        for px in im:
            gray = round(0.21 * px[0] + 0.72 * px[1] + 0.07 * px[2])
            gim.append((gray, gray, gray))
    else:
        raise ValueError('Invalid grayscale mode selected')

    return gim
