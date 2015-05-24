from math import acos, cos, pi, radians, sqrt


def cmyk2rgb(cmyk, prec=0):
    """Converts a CMYK quadruplet into an RGB triplet.

    NOTE: CMYK and RGB color spaces have different color gamuts, so visual
        results may differ depending on what RGB profile is selected.

    CMYK values are expected to be on the interval [0, 1].
    RGB values are given on the interval [0, 255].

    http://www.rapidtables.com/convert/color/cmyk-to-rgb.htm

    Args:
        cmyk (tuple): The CMYK quadruplet to convert.
        prec (int, optional): The decimal precision for RGB value rounding.

    Returns:
        tuple: An RGB triplet.

    Raises:
        ValueError: If one or more CMYK values are outside the interval [0, 1].

    """
    for value in cmyk:
        if not 0 <= value <= 1:
            raise ValueError('One or more CMYK values are outside [0, 1]')

    r = 255 * (1 - cmyk[0]) * (1 - cmyk[3])
    g = 255 * (1 - cmyk[1]) * (1 - cmyk[3])
    b = 255 * (1 - cmyk[2]) * (1 - cmyk[3])

    return round(r, prec), round(g, prec), round(b, prec)


def hex2rgb(hx):
    """Converts an RGB Hexadecimal into an RGB triplet.

    Hex values can be given in the form '#xxxxxx' or 'xxxxxx'.
    RGB values are given on the interval [0, 255].

    Args:
        hx (string): The RGB Hexadecimal to convert.

    Returns:
        tuple: An RGB triplet.

    """
    if hx[0] == '#':
        return int(hx[1:3], 16), int(hx[3:5], 16), int(hx[5:7], 16)
    else:
        return int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)


def hsl2rgb(hsl, prec=0):
    """Converts an HSL triplet into an RGB triplet.

    H values are expected to be on the interval [0, 360).
    S and L values are expected to be on the interval [0, 1].
    RGB values are given on the interval [0, 255].

    http://en.wikipedia.org/wiki/HSL_and_HSV#From_HSL

    Args:
        hsl (tuple): The HSL triplet to convert.
        prec (int, optional): The decimal precision for RGB value rounding.

    Returns:
        tuple: An RGB triplet.

    Raises:
        ValueError: If the given H value is outside [0, 360),
            or if the given S and/or L values are outside [0, 1].

    """
    h, s, l = hsl[0] / 60, hsl[1], hsl[2]

    if not 0 <= h < 6:
        raise ValueError('The given H value is outside [0, 360)')
    elif not 0 <= s <= 1 or not 0 <= l <= 1:
        raise ValueError('The given S and/or L values are outside [0, 1]')

    c = (1 - abs(2 * l - 1)) * s
    m = l - c / 2

    if 0 <= h < 1:
        r, g, b = c, c * (1 - abs(h % 2 - 1)), 0
    elif 1 <= h < 2:
        r, g, b = c * (1 - abs(h % 2 - 1)), c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, c * (1 - abs(h % 2 - 1))
    elif 3 <= h < 4:
        r, g, b = 0, c * (1 - abs(h % 2 - 1)), c
    elif 4 <= h < 5:
        r, g, b = c * (1 - abs(h % 2 - 1)), 0, c
    else:
        r, g, b = c, 0, c * (1 - abs(h % 2 - 1))

    r, g, b = r + m, g + m, b + m

    return round(255 * r, prec), round(255 * g, prec), round(255 * b, prec)


def hsv2rgb(hsv, prec=0):
    """Converts an HSV triplet into an RGB triplet.

    NOTE: HSV is also known as HSB, so if you're looking
        for HSB, look no further!

    H values are expected to be on the interval [0, 360).
    S and V values are expected to be on the interval [0, 1].
    RGB values are given on the interval [0, 255].

    http://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV

    Args:
        hsv (tuple): The HSV triplet to convert.
        prec (int, optional): The decimal precision for RGB value rounding.

    Returns:
        tuple: An RGB triplet.

    Raises:
        ValueError: If the given H value is outside [0, 360),
            or if the given S and/or V values are outside [0, 1].

    """
    h, s, v = hsv[0] / 60, hsv[1], hsv[2]

    if not 0 <= h < 6:
        raise ValueError('The given H value is outside [0, 360)')
    elif not 0 <= s <= 1 or not 0 <= v <= 1:
        raise ValueError('The given S and/or V values are outside [0, 1]')

    c = v * s
    m = v - c

    if 0 <= h < 1:
        r, g, b = c, c * (1 - abs(h % 2 - 1)), 0
    elif 1 <= h < 2:
        r, g, b = c * (1 - abs(h % 2 - 1)), c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, c * (1 - abs(h % 2 - 1))
    elif 3 <= h < 4:
        r, g, b = 0, c * (1 - abs(h % 2 - 1)), c
    elif 4 <= h < 5:
        r, g, b = c * (1 - abs(h % 2 - 1)), 0, c
    else:
        r, g, b = c, 0, c * (1 - abs(h % 2 - 1))

    r, g, b = r + m, g + m, b + m

    return round(255 * r, prec), round(255 * g, prec), round(255 * b, prec)


def rgb2cmyk(rgb, prec=3):
    """Converts an RGB triplet into a CMYK quadruplet.

    NOTE: CMYK and RGB color spaces have different color gamuts, so visual
        results may differ depending on what RGB profile is selected.

    RGB values are expected to be on the interval [0, 255].
    CMYK values are given on the interval [0, 1].

    http://www.rapidtables.com/convert/color/rgb-to-cmyk.htm

    Args:
        rgb (tuple): The RGB triplet to convert.
        prec (int, optional): The decimal precision for RGB value rounding.

    Returns:
        tuple: A CMYK quadruplet.

    """
    for value in rgb:
        if not 0 <= value <= 255:
            raise ValueError('One or more RGB values are outside [0, 255]')

    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255

    try:
        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    except ZeroDivisionError:
        c, m, y, k = 0, 0, 0, 1

    return round(c, prec), round(m, prec), round(y, prec), round(k, prec)


def rgb2hex(rgb):
    """Converts an RGB triplet into an RGB Hexadecimal.

    RGB values are expected to be given on the interval [0, 255].
    Hex values are given in the form '#xxxxxx'.

    Args:
        rgb (tuple): The RGB triplet to convert.

    Returns:
        string: An RGB Hexadecimal.

    """
    for value in rgb:
        if not 0 <= value <= 255:
            raise ValueError('One or more RGB values are outside [0, 255]')

    r_hex = hex(rgb[0])[2:]
    g_hex = hex(rgb[1])[2:]
    b_hex = hex(rgb[2])[2:]

    return '#' + r_hex.zfill(2) + g_hex.zfill(2) + b_hex.zfill(2)


def rgb2hsl(rgb, h_prec=0, sl_prec=3):
    """Converts an RGB triplet into an HSL triplet.

    RGB values are expected to be on the interval [0, 255].
    H values are given on the interval [0, 360).
    S and L values are given on the interval [0, 1].

    http://www.rapidtables.com/convert/color/rgb-to-hsl.htm

    Args:
        rgb (tuple): The RGB triplet to convert.
        h_prec (int, optional): The decimal precision for H value rounding.
        sl_prec (int, optional): The decimal precision for
            S and L value rounding.

    Returns:
        tuple: An HSL triplet.

    Raises:
        ValueError: If the given RGB values are outside [0, 255].

    """
    for value in rgb:
        if not 0 <= value <= 255:
            raise ValueError('One or more RGB values are outside [0, 255]')

    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    # Hue
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * ((b - r) / delta + 2)
    else:
        h = 60 * ((r - g) / delta + 4)

    # Lightness
    l = (c_max + c_min) / 2

    # Saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    return round(h, h_prec), round(s, sl_prec), round(l, sl_prec)


def rgb2hsv(rgb, h_prec=0, sv_prec=3):
    """Converts an RGB triplet into an HSV triplet.

    NOTE: HSV is also known as HSB, so if you're looking
        for HSB, look no further!

    RGB values are expected to be on the interval [0, 255].
    H values are given on the interval [0, 360).
    S and V values are given on the interval [0, 1].

    http://www.rapidtables.com/convert/color/rgb-to-hsv.htm

    Args:
        rgb (tuple): The RGB triplet to convert.
        h_prec (int, optional): The decimal precision for H value rounding.
        sv_prec (int, optional): The decimal precision for
            S and V value rounding.

    Returns:
        tuple: An HSV triplet.

    Raises:
        ValueError: If the given RGB values are outside [0, 255].

    """
    for value in rgb:
        if not 0 <= value <= 255:
            raise ValueError('One or more RGB values are outside [0, 255]')

    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    # Hue
    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * ((b - r) / delta + 2)
    else:
        h = 60 * ((r - g) / delta + 4)

    # Saturation
    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    # Value / Brightness
    v = c_max

    return round(h, h_prec), round(s, sv_prec), round(v, sv_prec)
