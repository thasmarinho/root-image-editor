from image_filter import *

img = read_image("images/blurry_moon.bmp")
#save_image("images/save_test.jpg", img.copy())
#apply_negative("negative_test.jpg", img.copy())
#apply_logarithmic("log_test.jpg", img.copy())
apply_gamma_correction("gamma_test.jpg", img.copy(), 0.6)
