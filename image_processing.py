import cv2


def calculate_humans(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (700, 400))

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (humans, _) = hog.detectMultiScale(img, winStride=(4, 4),
    padding=(4, 4), scale=1.1)
    return len(humans)

image_path = "people.png"
    num_humans, humans = calculate_humans(image_path)
    print(f'People found: {num_humans}')
image = cv2.imread(image_path)
for (x, y, w, h) in humans:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

 cv2.imshow("People detector", image)
