from PIL import Image 

for i in range(0, 2000):
    print(i)
    image = Image.open('./images/' + str(i) + '.png').convert("RGBA")
    image = image.resize((1024, 1024), Image.ANTIALIAS)
    image.save('./images/' + str(i) + '.png')