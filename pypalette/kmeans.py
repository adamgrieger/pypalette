from copy import copy
from math import sqrt
import random


class KMeans:
    def __init__(self, im, k):
        self.im = im
        self.k = k
        self.d = []
        self.clusters = [{'cc': copy(random.choice(self.im)), 'pts': []}]

    def get_palette(self):
        _lloyd()
        return [c['cc'] for c in self.clusters]

    def _euclid_dist(self, c, pt):
        return sqrt((c[0] - pt[0]) ** 2 +
                    (c[1] - pt[1]) ** 2 +
                    (c[2] - pt[2]) ** 2)

    def _has_converged(self, occ):
        for i in range(0, len(self.clusters)):
            for x in range(0, 3):
                if (round(occ[i][x]) !=
                        round([c['cc'] for c in self.clusters][i][x])):
                    return False
        return True

    def _lloyd(self):
        while self.k - 1 > 0:
            if len(self.clusters) == 1:
                for pt in self.im:
                    self.d.append(self._euclid_dist(
                            self.clusters[0]['cc'], pt))
            else:
                for pt in self.im:
                    min_dist = float('inf')
                    for c in self.clusters:
                        if self._euclid_dist(c['cc'], pt) < min_dist:
                            min_dist = self._euclid_dist(c['cc'], pt)
                    self.d.append(min_dist)

            self.d = [dist ** 2 for dist in self.d]
            total = sum(self.d)
            r = random.uniform(0, total)

            b = 0
            for i, c in enumerate(self.d):
                if b + c > r:
                    self.clusters.append({'cc': copy(self.im[i]), 'pts': []})
                    break
                b += c

            self.d.clear()
            self.k -= 1

        while True:
            occ = [c['cc'] for c in self.clusters]
            self._reassign_points()
            self._update_centroids()
            if self._has_converged(occ):
                break

    def _reassign_points(self):
        for c in self.clusters:
            c['pts'].clear()
        for pt in self.im:
            min_dist = float('inf')
            min_index = 0
            for i, c in enumerate(self.clusters):
                if self._euclid_dist(c['cc'], pt) < min_dist:
                    min_dist = self._euclid_dist(c['cc'], pt)
                    min_index = i
            self.clusters[min_index]['pts'].append(pt)

    def _update_centroids(self):
        for c in self.clusters:
            c['cc'] = (sum(pt[0] for pt in c['pts']) / len(c['pts']),
                       sum(pt[1] for pt in c['pts']) / len(c['pts']),
                       sum(pt[2] for pt in c['pts']) / len(c['pts']))
