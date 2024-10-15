import numpy as np
from PIL import Image


file_name = "./work_dir/drc_routenet/test_result/7099-zero-riscy-a-1-c2-u0.7-m1-p3-f0.npy"
# 加载 .npy 文件

data = np.load(file_name)
is_all_zero = np.all(data == 0)
print(is_all_zero)
# 假设要保存的是最后两个维度 (256, 256)
image = data[0, 0]  # 选择合适的切片
image = Image.fromarray(image)

# 保存为图片
image.save('output_image.png')

