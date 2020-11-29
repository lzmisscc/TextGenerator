import os
import os.path as osp
import glob
import PIL
from PIL import Image, ImageDraw
import json
from functools import reduce


def show():
    p = "output/data/1e7d2a221fe1473dc14a8925aebc9ee13eacd06d.json"
    with open(p, "r") as f:
        data = json.load(f,)
    p = p.replace(".json", ".png").replace('data/', 'img/pic/pic_')
    image = Image.open(p)
    draw = ImageDraw.Draw(image, mode="RGBA")
    for i in data["fragment"]:
        rotate_box = i['rotate_box']
        res = []
        for i in rotate_box:
            res += i
        draw.polygon(res, fill=(255, 100, 1, 200), )
    image.save("image.png")

    return


show()
exit(0)

def json2txt():
    json_lines = glob.glob("output/data/*.json")
    for p in json_lines:
        with open(p, "r") as f:
            data = json.load(f,)
        p = p.replace(".json", ".png").replace('data/', 'img/pic/pic_')
        txt_lines = []
        for i in data["fragment"]:
            rotate_box = i['rotate_box']
            res = []
            for i in rotate_box:
                res += i
            txt_lines.append(','.join(map(str, res))+'\n')
        with open(p.replace(".png", ".txt"), "w") as f:
            f.writelines(txt_lines)
        print(p)

    return

json2txt()
exit(0)