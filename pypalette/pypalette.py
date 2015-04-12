def main():
    print(hsv2rgb(180, 1, 0.5))


def average_color(rgb):
    r_sum = 0
    g_sum = 0
    b_sum = 0

    for pixel in rgb:
        r_sum += pixel[0]
        g_sum += pixel[1]
        b_sum += pixel[2]

    r_avg = r_sum / len(rgb)
    g_avg = b_sum / len(rgb)
    b_avg = g_sum / len(rgb)

    return r_avg, g_avg, b_avg


def rgb2hsv(r, g, b):
    rp = r / 255
    gp = g / 255
    bp = b / 255
    c_max = max(rp, gp, bp)
    c_min = min(rp, gp, bp)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == rp:
        h = 60 * (((gp - bp) / delta) % 6)
    elif c_max == gp:
        h = 60 * (((bp - rp) / delta) + 2)
    else:
        h = 60 * (((rp - gp) / delta) + 4)

    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    v = c_max

    return h, s, v


def hsv2rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        rp = c
        gp = x
        bp = 0
    elif 60 <= h < 120:
        rp = x
        gp = c
        bp = 0
    elif 120 <= h < 180:
        rp = 0
        gp = c
        bp = x
    elif 180 <= h < 240:
        rp = 0
        gp = x
        bp = c
    elif 240 <= h < 300:
        rp = x
        gp = 0
        bp = c
    else:
        rp = c
        gp = 0
        bp = x

    return rp * 255 + m, gp * 255 + m, bp * 255 + m


def rgb2hsl(r, g, b):
    rp = r / 255
    gp = g / 255
    bp = b / 255
    c_max = max(rp, gp, bp)
    c_min = min(rp, gp, bp)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == rp:
        h = 60 * (((gp - bp) / delta) % 6)
    elif c_max == gp:
        h = 60 * (((bp - rp) / delta) + 2)
    else:
        h = 60 * (((rp - gp) / delta) + 4)

    l = (c_max + c_min) / 2

    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs((2 * l) - 1))

    return h, s, l


def hsl2rgb(h, s, l):
    pass


def rgb2cmyk(r, g, b):
    rp = r / 255
    gp = g / 255
    bp = b / 255

    k = 1 - max(rp, gp, bp)
    c = (1 - rp - k) / (1 - k)
    m = (1 - gp - k) / (1 - k)
    y = (1 - bp - k) / (1 - k)

    return c, m, y, k


def cmyk2rgb(c, m, y, k):
    pass


def rgb2hex(r, g, b):
    r_hex = hex(r)[2:]
    g_hex = hex(g)[2:]
    b_hex = hex(b)[2:]

    return r_hex.zfill(2) + g_hex.zfill(2) + b_hex.zfill(2)


def hex2rgb(hex):
    pass


if __name__ == "__main__":
    main()