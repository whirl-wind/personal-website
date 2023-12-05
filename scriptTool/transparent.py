from PIL import Image
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
threshold=200

def convertImage():
	img = Image.open(dir_path+"/input.png")
	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []

	for item in datas:
		if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save(dir_path+"/ouput.png", "PNG")
	print("Successful")

convertImage()
