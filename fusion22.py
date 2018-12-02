from PIL import Image

im = Image.open("éclaboussure-de-l-eau-13872175.jpg")
im1 = Image.open("bbsitting.JPG")
im2 = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
im3 = Image.open("dolphin-2939189__340.jpg")

im_size = im.size
new_im = Image.new('RGB', (2156,2*im_size[1]))

new_im.paste(im, (0,0))
new_im.paste(im2, (0,im_size[1]))
new_im.paste(im1, (1000,0))
new_im.paste(im3, (1000,im_size[1]))
new_im.show()
