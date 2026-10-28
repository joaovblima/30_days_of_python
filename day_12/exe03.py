import random 
def rgb_color_gen():
    rgb = []
    num = 0
    for i in range(3):
        num = random.randint(0, 255)
        rgb.append(num)

    rgb_tlp = tuple(rgb)

    return rgb_tlp

print(rgb_color_gen())