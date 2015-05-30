from copy import copy
from math import sqrt
import random


def euclid_dist(c, pt):
    """Calculates the 3D Euclidean distance between two points.

    Args:
        c: A cluster centroid as an RGB tuple.
        pt: A selected image point as an RGB tuple.

    Returns:
        The Euclidean distance between the two points.
    """
    return sqrt((c[0] - pt[0]) ** 2 + (c[1] - pt[1]) ** 2 +
                (c[2] - pt[2]) ** 2)


class KMeans(object):
    """A class for performing k-means clustering on an image.

    The method of k-means clustering is used here to partition the points
    in a given image into k different clusters. Since the points in the image
    represent the colors in the image, the resulting cluster centroids are
    declared to be the image's most representative colors. To improve results,
    k-means++ initialization is used so that initial cluster centroid seeding
    is less random and more consistent.

    http://en.wikipedia.org/wiki/K-means_clustering
    http://en.wikipedia.org/wiki/K-means%2B%2B
    """

    def __init__(self, im, k):
        """Initializes KMeans with an image and initial cluster data.

        Args:
            im: An image as a list of RGB tuples.
            k: The number of clusters to generate.

        Raises:
            ValueError: If an empty image is passed (i.e. []) or if the desired
                amount of clusters is less than two.
        """
        if len(im) == 0:
            raise ValueError('An empty image has been passed')
        elif k < 2:
            raise ValueError('The number of clusters must be at least two')

        self.im = im
        self.k = k
        self.d = []    # Empty distances list for use later on

        # First initial cluster centroid is chosen uniformly at random
        self.clusters = [{'cc': copy(random.choice(self.im)), 'pts': []}]

    def get_colors(self, prec=0):
        """Returns a list of k colors that are most representative of the image.

        Args:
            prec: An optional int for RGB value decimal precision,
                defaults to 0.

        Returns:
            A list of k RGB tuples.
        """
        self._kpp_init()
        self._lloyd()
        return [c['cc'] for c in self.clusters]

    def _has_converged(self, occ):
        """Determines whether the cluster centroids have converged.

        The cluster centroids are said to have converged when the rounded
        cluster centroids remain the same after an iteration of updating.

        Args:
            occ: The cluster centroids from the previous iteration.

        Returns:
            True is the cluster centroids have converged, False otherwise.
        """
        for i in range(0, len(self.clusters)):
            for x in range(0, 3):    # Have to compare RGB values separately
                if (round(occ[i][x]) !=
                        round([c['cc'] for c in self.clusters][i][x])):
                    return False
                else:
                    return True

    def _kpp_init(self):
        """Uses k-means++ initialization to generate initial cluster centroids.

        Instead of generating all initial cluster centroids uniformly at
        random, all centroids after the first one are generated proportional
        to each point's squared distance to the nearest cluster. This helps
        in spreading out the initial clusters and avoiding weird results that
        can occur with all random cluster centroids.
        """
        while self.k - 1 > 0:
            # No point in calculating minimum distances with one cluster
            if len(self.clusters) == 1:
                for pt in self.im:
                    self.d.append(euclid_dist(self.clusters[0]['cc'], pt))
            # Assigns each point to the nearest cluster
            else:
                for pt in self.im:
                    min_dist = float('inf')    # For first comparison
                    for c in self.clusters:
                        if euclid_dist(c['cc'], pt) < min_dist:
                            min_dist = euclid_dist(c['cc'], pt)
                    self.d.append(min_dist)

            # Probability distrubution proportional to squared distance
            self.d = [dist ** 2 for dist in self.d]
            total = sum(self.d)
            r = random.uniform(0, total)

            # Generates a new cluster using the above probability distribution
            b = 0
            for i, c in enumerate(self.d):
                if b + c > r:
                    self.clusters.append({'cc': copy(self.im[i]), 'pts': []})
                    break
                b += c

            self.d.clear()
            self.k -= 1

    def _lloyd(self):
        """The standard k-means algorithm / Lloyd's algorithm.

        The few steps to Lloyd's algorithm are as follows:
            1. Reassign each point in the image to its nearest cluster.
            2. Update cluster centroids by taking the mean of their members.
            3. Repeat Steps 1 and 2 until convergence.
        """
        while True:
            occ = [c['cc'] for c in self.clusters]
            self._reassign_points()
            self._update_centroids()
            if self._has_converged(occ):
                break

    def _reassign_points(self):
        """Reassigns each point in the image to its nearest cluster."""

        for c in self.clusters:
            c['pts'].clear()    # Gets rid of old cluster members
        for pt in self.im:
            min_dist = float('inf')    # For first comparison
            min_index = 0
            for i, c in enumerate(self.clusters):
                if euclid_dist(c['cc'], pt) < min_dist:
                    min_dist = euclid_dist(c['cc'], pt)
                    min_index = i
            self.clusters[min_index]['pts'].append(pt)

    def _update_centroids(self):
        """Updates cluster centroids by taking the mean of their members."""

        for c in self.clusters:
            c['cc'] = (sum(pt[0] for pt in c['pts']) / len(c['pts']),
                       sum(pt[1] for pt in c['pts']) / len(c['pts']),
                       sum(pt[2] for pt in c['pts']) / len(c['pts']))
