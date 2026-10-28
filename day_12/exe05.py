import random
def list_of_rgb_colors():
    rgb = []
    num = 0
    for i in range(3):
        num = random.randint(0, 255)
        rgb.append(num)

    rgb_tlp = tuple(rgb)
    list_rgb = []
    list_rgb.append(rgb_tlp)

    return list_rgb

print(list_of_rgb_colors())
