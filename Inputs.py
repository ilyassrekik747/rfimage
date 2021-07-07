def T(m):
    im_1 = Image.open(m,mode="r")

    width, height = im_1.size
    print(im_1.mode)
    B = im_1.tobytes()
    print(width, height)
#T(the image name or where it is )
