from copy import copy
from math import sqrt
from PIL import Image
import random


def main():
    im = Image.open('..\\testingimages\\kodim21.png')
    imlist = list(im.getdata())
    imobj = KMeans(imlist, 5)


class KMeans:
    def __init__(self, im, k):
        self.im = im
        self.k = k
        self.d = []
        self.clusters = [{'cc': copy(random.choice(self.im)), 'pts': []}]
        while self.k - 1 > 0:
            if len(self.clusters) == 1:
                for pt in self.im:
                    self.d.append(self.euclid_dist(self.clusters[0]['cc'], pt))
            else:
                for pt in self.im:
                    min_dist = float('inf')
                    for c in self.clusters:
                        if self.euclid_dist(c['cc'], pt) < min_dist:
                            min_dist = self.euclid_dist(c['cc'], pt)
                    self.d.append(min_dist)

            for dist in self.d:
                dist = dist ** 2
            total = sum(self.d)
            print("Distance Total:", total)
            r = random.uniform(0, total)
            print("Random Number:", r)

            upto = 0
            for i, c in enumerate(self.d):
                if upto + c > r:
                    self.clusters.append({'cc': copy(self.im[i]), 'pts': []})
                    break
                upto += c

            self.d.clear()
            self.k -= 1

        print(len(self.clusters))
        for cluster in self.clusters:
            print(cluster['cc'])
        print("\n")

        for x in range(0, 10):
            self.reassign_points()
            self.update_centroids()
            for cluster in self.clusters:
                print(cluster['cc'])
            print("\n")

    def euclid_dist(self, c, pt):
        return sqrt((c[0] - pt[0]) ** 2 + (c[1] - pt[1]) ** 2 +
                    (c[2] - pt[2]) ** 2)

    def reassign_points(self):
        for c in self.clusters:
            c['pts'].clear()

        for pt in self.im:
            min_dist = float('inf')
            min_index = 0
            for i, c in enumerate(self.clusters):
                if self.euclid_dist(c['cc'], pt) < min_dist:
                    min_dist = self.euclid_dist(c['cc'], pt)
                    min_index = i
            self.clusters[min_index]['pts'].append(pt)

    def update_centroids(self):
        for c in self.clusters:
            c['cc'] = (round(sum(pt[0] for pt in c['pts']) / len(c['pts'])),
                       round(sum(pt[1] for pt in c['pts']) / len(c['pts'])),
                       round(sum(pt[2] for pt in c['pts']) / len(c['pts'])))

if __name__ == '__main__':
    main()
