import glob
import os
from PIL import Image
import concurrent.futures


def make_image_thumbnail(filename):
    base_filename, file_extension = os.path.splitext(filename)
    thumbnail_filename = f"{base_filename}_thumbnail{file_extension}"
    # 保存缩略图
    # image = Image.open(filename)
    # image.thumbnail(size=(128,128))
    return thumbnail_filename


# 创建 process pool，默认为每个 cpu 创建一个
with concurrent.futures.ProcessPoolExecutor() as executor:
    image_files = glob.glob("*.jpg")
    # 处理文件列表，通过 pool 划分工作，使用全部 cpu
    for image_file, thumbnail_file in zip(image_files, executor.map(make_image_thumbnail, image_files)):
        print(f"A thumbnail for {image_file} was saved as {thumbnail_file}")