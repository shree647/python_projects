import cv2
d = cv2.QRCodeDetector()
retval, points, straight_qrcode = d.detectAndDecode(cv2.imread('sample1.png'))
print(retval)

