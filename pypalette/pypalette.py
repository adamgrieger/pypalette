from PIL import Image


def main():
    img = Image.open("TestImages\\sunlight-through-clouds.jpg")
    rgb_tuples = list(img.getdata())
    print(average_color(rgb_tuples))


def average_color(rgb):
    r_sum = 0
    g_sum = 0
    b_sum = 0

    for pixel in rgb:
        r_sum += pixel[0]
        g_sum += pixel[1]
        b_sum += pixel[2]

    r_average = r_sum / len(rgb)
    g_average = b_sum / len(rgb)
    b_average = g_sum / len(rgb)

    return r_average, g_average, b_average


if __name__ == "__main__":
    main()