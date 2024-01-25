import cv2
from PIL import Image
img_cat = "pics/cat.jpeg"
image = cv2.imread(img_cat)

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cate_face = cat_face_cascade.detectMultiScale(image)
print(cate_face)
cat = Image.open(img_cat)
glasses = Image.open("pics/glasses.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for(x, y, w, h) in cate_face:
    #cv2.rectangle(image, (x, y), (x + w, y + h), (250, 0, 0), 3 )
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y + h/4)), glasses)
    cat.save('pics/newCat.png')
cv2.imshow("Cat", image)
cv2.waitKey()