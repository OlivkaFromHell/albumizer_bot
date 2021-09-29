from cv2 import imread, resize, imwrite, INTER_AREA


async def make_cover():
    img = imread('/home/albumizer_bot/data/images/photo.jpg')
    label = imread('/home/albumizer_bot/data/images/label.jpg')

    resized = resize(img, (1064, 1064), interpolation=INTER_AREA)
    x_offset = 827
    y_offset = 900

    resized[y_offset:y_offset+label.shape[0], x_offset:x_offset+label.shape[1]] = label

    imwrite(filename='/home/albumizer_bot/data/images/cover.jpg', img=resized)
