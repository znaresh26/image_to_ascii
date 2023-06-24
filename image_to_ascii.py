from PIL import Image

ascii_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_surface=" `.,108"
# ascii_surface="108"
l=len(ascii_surface)
max_pixel_value=765
brightness_weight= l/max_pixel_value

def pixel_to_ascii(pixel):
#     print(pixel)
    pixel=sum(pixel)
    index=int(pixel*brightness_weight)-1
    return ascii_surface[index]
    
def image_to_ascii(img):
    art=[]
    b,h=img.size
    for y in range(h-1):
        line=""
        for x in range(b-1):
            px=img.getpixel((x,y))
            line+=pixel_to_ascii(px)
        art+=[line]
    return art
def save_as_file(art):
    name=img_name.split(".")[0]
    file = open(str(name)+".txt","w")
    for i in art:
        
        file.write(i)
        file.write("\n")
    file.close()

img_name="rengoku.jpg"
img=Image.open(img_name)
img=img.resize((512,512))
ascii_art = image_to_ascii(img)
save_as_file(ascii_art)
