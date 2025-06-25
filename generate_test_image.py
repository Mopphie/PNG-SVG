from PIL import Image, ImageDraw
img = Image.new('RGB', (300, 200), 'white')
draw = ImageDraw.Draw(img)
# car body
draw.rectangle([50, 100, 250, 150], outline='black', width=5)
# roof
draw.polygon([(80,100),(120,70),(180,70),(220,100)], outline='black', width=5)
# wheels
draw.ellipse([70,150,110,190], outline='black', width=5)
draw.ellipse([190,150,230,190], outline='black', width=5)
img.save('test_car.png')
