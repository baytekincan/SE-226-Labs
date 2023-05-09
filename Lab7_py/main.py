import cv2

image = cv2.imread('example.jpeg')
cv2.imshow("Original_Image", image)
cv2.waitKey(0)

b, g, r = cv2.split(image)

cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)

print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)

for x in range(0, 1024):
    for y in range(0, 768):
        if b[x, y] > 100:
            b[x, y] = 10

image_merge = cv2.merge([r, g, b])

cv2.imshow("RGB_Image", image_merge)

cv2.waitKey(0)

dimensions = image.shape
print(dimensions)
