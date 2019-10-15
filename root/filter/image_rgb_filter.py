from root.filter import ImageFilter as filter
from root.util import RgbUtil as rgb


class RgbFilter():

    @staticmethod
    def apply_negative(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_negative(r)
        g = filter.apply_negative(g)
        b = filter.apply_negative(b)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_logarithmic(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_logarithmic(r)
        g = filter.apply_logarithmic(g)
        b = filter.apply_logarithmic(b)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_gamma_correction(img, gamma):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_gamma_correction(r, gamma)
        g = filter.apply_gamma_correction(g, gamma)
        b = filter.apply_gamma_correction(b, gamma)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def draw_histogram(img, img_name):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.draw_histogram(r, img_name + "_red" + ".jpg", "r")
        g = filter.draw_histogram(g, img_name + "_green" + ".jpg", "g")
        b = filter.draw_histogram(b, img_name + "_blue" + ".jpg", "b")

    @staticmethod
    def apply_histogram_equalization(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_histogram_equalization(r)
        g = filter.apply_histogram_equalization(g)
        b = filter.apply_histogram_equalization(b)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_median(img, filter_size):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_median(r, filter_size)
        g = filter.apply_median(g, filter_size)
        b = filter.apply_median(b, filter_size)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_piecewise_linear(img, coordinates_x, coordinates_y):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_piecewise_linear(r, coordinates_x, coordinates_y)
        g = filter.apply_piecewise_linear(g, coordinates_x, coordinates_y)
        b = filter.apply_piecewise_linear(b, coordinates_x, coordinates_y)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_convolution(img, filter_matrix):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_convolution(r, filter_matrix)
        g = filter.apply_convolution(g, filter_matrix)
        b = filter.apply_convolution(b, filter_matrix)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_laplacian(img):
        r, g, b = rgb.get_rgb_layers(img)
        r, r_sharpened = filter.apply_laplacian(r)
        g, g_sharpened = filter.apply_laplacian(g)
        b, b_sharpened = filter.apply_laplacian(b)
        return rgb.merge_rgb_layers(r, g, b), rgb.merge_rgb_layers(r_sharpened, g_sharpened, b_sharpened)

    @staticmethod
    def apply_gradient(img, filter_matrix):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_gradient(r, filter_matrix)
        g = filter.apply_gradient(g, filter_matrix)
        b = filter.apply_gradient(b, filter_matrix)
        return rgb.merge_rgb_layers(r, g, b)

    @staticmethod
    def apply_sobel(img):
        r, g, b = rgb.get_rgb_layers(img)
        r = filter.apply_sobel(r)
        g = filter.apply_sobel(g)
        b = filter.apply_sobel(b)
        return rgb.merge_rgb_layers(r, g, b)
