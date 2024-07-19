from PIL import Image
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def convertImage():
	img = Image.open(dir_path+"/input.png")
	img = img.convert("RGBA")
	w, h = img.size
	new_img = Image.new(mode="RGBA", size=(w,int(w*4/3)), color=(255, 255, 255, 0))
	new_img.paste(img,(0, int((w*4/3-h)/2)))

	new_img.save(dir_path+"/New.png", "PNG")
	print("Successful")

convertImage()