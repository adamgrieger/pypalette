from statistics import mean
from kmeans import KMeans


def average_color(rgb):
    r_avg = mean([px[0] for px in rgb])
    g_avg = mean([px[1] for px in rgb])
    b_avg = mean([px[2] for px in rgb])

    return r_avg, g_avg, b_avg
