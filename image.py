from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import csv
 
# 이미지 열기
csv_data = []
with open('input__XrayImage_Coordinates/coordinates.csv', "rt", encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in spamreader:
        csv_data.append([])
        for data in row:
            csv_data[i].append(data)
        i = i+1
        
    
im = Image.open('input__XrayImage_Coordinates/1.jpg')
 
# 이미지 크기 출력
print(im.size)

# 이미지 Cropping 하기 (x시작점, y시작점, 가로넓이, 세로넓이)
cropImage = im.crop((0, 200, 1000, 1000))
cropImage.save('cropped.jpg')

# 좌표값 표시하기
draw = ImageDraw.Draw(im) 
indices = [1,3,4,5,6,7,8]
for i in indices:
    draw.text((int(csv_data[1][i].split('|')[0]),int(csv_data[1][i].split('|')[1])+10), csv_data[0][i],font=ImageFont.truetype('arial', 40), fill='#ffff00')
    draw.rectangle((int(csv_data[1][i].split('|')[0])-10,int(csv_data[1][i].split('|')[1])-10, int(csv_data[1][i].split('|')[0])+10,int(csv_data[1][i].split('|')[1])+10),'yellow','blue')
im.save('text.jpg')