import unittest
import sys
import os

sys.path.append(os.path.join('..', 'pypalette'))
import color_lists
import conversions
import kmeans
import pypalette


class TestColorLists(unittest.TestCase):
    """Tests color list accessibility."""

    def test_css3(self):
        """Tests the CSS3 color list."""

        self.assertEqual(color_lists.css3['dodgerblue'], '#1e90ff')

    def test_material_design(self):
        """Tests the Google Material Design color list."""

        self.assertEqual(color_lists.material_design['blue-500'], '#2196f3')

    def test_sp_pbt(self):
        """Tests the Signature Plastics' PBT color list."""

        self.assertEqual(color_lists.sp_pbt['gqp'], '#a49d97')


class TestConversions(unittest.TestCase):
    """Tests color space conversion functions."""

    def test_cmyk2rgb_conv(self):
        """Tests the CMYK to RGB conversion."""

        self.assertEqual(conversions.cmyk2rgb((0.56, 0.26, 0.82, 0.11)),
                         (100, 168, 41))
        self.assertEqual(conversions.cmyk2rgb((0, 0, 0, 0)), (255, 255, 255))
        self.assertEqual(conversions.cmyk2rgb((1, 1, 1, 1)), (0, 0, 0))

    def test_cmyk2rgb_cmyk_check(self):
        """Tests the invalid CMYK values error for cmyk2rgb."""

        self.assertRaises(ValueError, conversions.cmyk2rgb, (1, 1, 1.1, 1))
        self.assertRaises(ValueError, conversions.cmyk2rgb, (1, -1, 0, 0.5))

    def test_cmyk2rgb_prec_check(self):
        """Tests the optional rounding precision for cmyk2rgb."""

        self.assertEqual(conversions.cmyk2rgb((1, 0.26, 0.82, 0.11), prec=2),
                         (0, 167.94, 40.85))

    def test_hex2rgb_conv(self):
        """Tests the Hex to RGB conversion."""

        self.assertEqual(conversions.hex2rgb('b155d2'), (177, 85, 210))
        self.assertEqual(conversions.hex2rgb('#b155d2'), (177, 85, 210))
        self.assertEqual(conversions.hex2rgb('ffffff'), (255, 255, 255))
        self.assertEqual(conversions.hex2rgb('#ffffff'), (255, 255, 255))
        self.assertEqual(conversions.hex2rgb('000000'), (0, 0, 0))
        self.assertEqual(conversions.hex2rgb('#000000'), (0, 0, 0))

    def test_hsl2rgb_conv(self):
        """Tests the HSL to RGB conversion."""

        self.assertEqual(conversions.hsl2rgb((0, 0, 0)), (0, 0, 0))
        self.assertEqual(conversions.hsl2rgb((0, 0.5, 0.5)), (191, 64, 64))
        self.assertEqual(conversions.hsl2rgb((0, 1, 1)), (255, 255, 255))
        self.assertEqual(conversions.hsl2rgb((60, 0.5, 0.5)), (191, 191, 64))
        self.assertEqual(conversions.hsl2rgb((120, 0.5, 0.5)), (64, 191, 64))
        self.assertEqual(conversions.hsl2rgb((180, 0.5, 0.5)), (64, 191, 191))
        self.assertEqual(conversions.hsl2rgb((240, 0.5, 0.5)), (64, 64, 191))
        self.assertEqual(conversions.hsl2rgb((300, 0.5, 0.5)), (191, 64, 191))

    def test_hsl2rgb_hsl_check(self):
        """Tests the invalid HSL values errors for hsl2rgb."""

        self.assertRaises(ValueError, conversions.hsl2rgb, (-55, 0, 0))
        self.assertRaises(ValueError, conversions.hsl2rgb, (360, 1, 1))
        self.assertRaises(ValueError, conversions.hsl2rgb, (0, 2, 1))
        self.assertRaises(ValueError, conversions.hsl2rgb, (0, -1, 1))
        self.assertRaises(ValueError, conversions.hsl2rgb, (0, 1, 2))
        self.assertRaises(ValueError, conversions.hsl2rgb, (0, 1, -1))

    def test_hsl2rgb_prec_check(self):
        """Tests the optional round precision for hsl2rgb."""

        self.assertEqual(conversions.hsl2rgb((183, 0.25, 0.67), prec=2),
                         (149.81, 189.78, 191.89))

    def test_hsv2rgb_conv(self):
        """Tests the HSV to RGB conversion."""

        self.assertEqual(conversions.hsv2rgb((0, 0, 0)), (0, 0, 0))
        self.assertEqual(conversions.hsv2rgb((0, 0.5, 0.5)), (128, 64, 64))
        self.assertEqual(conversions.hsv2rgb((0, 1, 1)), (255, 0, 0))
        self.assertEqual(conversions.hsv2rgb((60, 0.5, 0.5)), (128, 128, 64))
        self.assertEqual(conversions.hsv2rgb((120, 0.5, 0.5)), (64, 128, 64))
        self.assertEqual(conversions.hsv2rgb((180, 0.5, 0.5)), (64, 128, 128))
        self.assertEqual(conversions.hsv2rgb((240, 0.5, 0.5)), (64, 64, 128))
        self.assertEqual(conversions.hsv2rgb((300, 0.5, 0.5)), (128, 64, 128))

    def test_hsv2rgb_hsv_check(self):
        """Tests the invalid HSV values errors for hsv2rgb."""

        self.assertRaises(ValueError, conversions.hsv2rgb, (-55, 0, 0))
        self.assertRaises(ValueError, conversions.hsv2rgb, (360, 1, 1))
        self.assertRaises(ValueError, conversions.hsv2rgb, (0, 2, 1))
        self.assertRaises(ValueError, conversions.hsv2rgb, (0, -1, 1))
        self.assertRaises(ValueError, conversions.hsv2rgb, (0, 1, 2))
        self.assertRaises(ValueError, conversions.hsv2rgb, (0, 1, -1))

    def test_hsv2rgb_prec_check(self):
        """Tests the optional round precision for hsv2rgb."""

        self.assertEqual(conversions.hsv2rgb((183, 0.25, 0.67), prec=2),
                         (128.14, 168.71, 170.85))

    def test_rgb2cmyk_conv(self):
        """Tests the RGB to CMYK conversion."""

        self.assertEqual(conversions.rgb2cmyk((0, 0, 0)), (0, 0, 0, 1))
        self.assertEqual(conversions.rgb2cmyk((255, 255, 255)), (0, 0, 0, 0))
        self.assertEqual(conversions.rgb2cmyk((89, 216, 114)),
                         (0.588, 0, 0.472, 0.153))

    def test_rgb2cmyk_rgb_check(self):
        """Tests the invalid RGB values error for rgb2cmyk."""

        self.assertRaises(ValueError, conversions.rgb2cmyk, (-1, 250, 50))
        self.assertRaises(ValueError, conversions.rgb2cmyk, (255, 256, 0))

    def test_rgb2cmyk_prec_check(self):
        """Tests the optional rounding precision for rgb2cmyk."""

        self.assertEqual(conversions.rgb2cmyk((89, 216, 114), prec=2),
                         (0.59, 0, 0.47, 0.15))

    def test_rgb2hex_conv(self):
        """Tests the RGB to Hex conversion."""

        self.assertEqual(conversions.rgb2hex((0, 0, 0)), '#000000')
        self.assertEqual(conversions.rgb2hex((128, 128, 128)), '#808080')
        self.assertEqual(conversions.rgb2hex((255, 255, 255)), '#ffffff')
        self.assertEqual(conversions.rgb2hex((89, 216, 114)), '#59d872')

    def test_rgb2hex_rgb_check(self):
        """Tests the invalid RGB values error for rgb2hex."""

        self.assertRaises(ValueError, conversions.rgb2hex, (-1, 250, 50))
        self.assertRaises(ValueError, conversions.rgb2hex, (255, 256, 0))

    def test_rgb2hsl_conv(self):
        """Tests the RGB to HSL conversion."""

        self.assertEqual(conversions.rgb2hsl((0, 0, 0)), (0, 0, 0))
        self.assertEqual(conversions.rgb2hsl((255, 255, 255)), (0, 0, 1))
        self.assertEqual(conversions.rgb2hsl((215, 157, 74)),
                         (35, 0.638, 0.567))
        self.assertEqual(conversions.rgb2hsl((96, 208, 74)),
                         (110, 0.588, 0.553))
        self.assertEqual(conversions.rgb2hsl((119, 53, 200)),
                         (267, 0.581, 0.496))

    def test_rgb2hsl_rgb_check(self):
        """Tests the invalid RGB values error for rgb2hsl."""

        self.assertRaises(ValueError, conversions.rgb2hsl, (-1, 250, 50))
        self.assertRaises(ValueError, conversions.rgb2hsl, (255, 256, 0))

    def test_rgb2hsl_prec_check(self):
        """Tests the optional rounding precision for rgb2hsl."""

        self.assertEqual(conversions.rgb2hsl((215, 157, 74), h_prec=1),
                         (35.3, 0.638, 0.567))
        self.assertEqual(conversions.rgb2hsl((215, 157, 74), sl_prec=2),
                         (35, 0.64, 0.57))

    def test_rgb2hsv_conv(self):
        """Tests the RGB to HSV conversion."""

        self.assertEqual(conversions.rgb2hsv((0, 0, 0)), (0, 0, 0))
        self.assertEqual(conversions.rgb2hsv((255, 255, 255)), (0, 0, 1))
        self.assertEqual(conversions.rgb2hsv((215, 157, 74)),
                         (35, 0.656, 0.843))
        self.assertEqual(conversions.rgb2hsv((96, 208, 74)),
                         (110, 0.644, 0.816))
        self.assertEqual(conversions.rgb2hsv((119, 53, 200)),
                         (267, 0.735, 0.784))

    def test_rgb2hsv_rgb_check(self):
        """Tests the invalid RGB values error for rgb2hsv."""

        self.assertRaises(ValueError, conversions.rgb2hsv, (-1, 250, 50))
        self.assertRaises(ValueError, conversions.rgb2hsv, (255, 256, 0))

    def test_rgb2hsv_prec_check(self):
        """Tests the optional rounding precision for rgb2hsv."""

        self.assertEqual(conversions.rgb2hsv((215, 157, 74), h_prec=1),
                         (35.3, 0.656, 0.843))
        self.assertEqual(conversions.rgb2hsv((215, 157, 74), sv_prec=2),
                         (35, 0.66, 0.84))


class TestKMeans(unittest.TestCase):
    """Tests the k-means clustering class."""

    def test_kmeans_im_check(self):
        """Tests the empty image error for the KMeans class."""

        self.assertRaises(ValueError, kmeans.KMeans, [], 3)

    def test_kmeans_k_check(self):
        """Tests the invalid number of clusters error for the KMeans class."""

        self.assertRaises(ValueError, kmeans.KMeans, [0, 0, 0], 1)

    def test_kmeans_get_colors(self):
        """Tests the get_colors method from the KMeans class."""

        # Fibonacci sequence anyone?
        im = [(0, 1, 1), (2, 3, 5), (8, 13, 21), (34, 55, 89)]
        im_kmeans = kmeans.KMeans(im, 4)
        im_colors = im_kmeans.get_colors()

        # Sometimes the colors are in a different order because of the
        # centroids being randomly picked.
        self.assertEqual(sorted(im), sorted(im_colors))


class TestPyPalette(unittest.TestCase):
    """Tests main PyPalette functions."""

    def test_average_color(self):
        """Tests the average_color function."""

        # Fibonacci sequence anyone?
        im = [(0, 1, 1), (2, 3, 5), (8, 13, 21), (34, 55, 89)]

        self.assertEqual(pypalette.average_color(im), (11, 18, 29))


if __name__ == '__main__':
    unittest.main(exit=False)
