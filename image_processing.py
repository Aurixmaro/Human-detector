import cv2


def calculate_humans(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (700, 400))

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (humans, _) = hog.detectMultiScale(img, winStride=(4, 4),
    padding=(4, 4), scale=1.1)
    return len(humans)
