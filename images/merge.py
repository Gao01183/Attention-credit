import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Helvetica", "Arial", "DejaVu Sans"]
plt.rcParams["font.size"] = 10

from PIL import Image, ImageOps


# 1. 自动裁剪 PNG 外围多余白边
def trim_border(img_path):
    img = Image.open(img_path).convert("RGB")
    # 转灰度寻找边界
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    diff = ImageOps.invert(img)
    bbox = diff.getbbox()
    return img.crop(bbox) if bbox else img


# 加载并裁剪三张图
img_a = trim_border("diag_interaction.png")
img_b = trim_border("centroid_interaction.png")
img_c = trim_border("peak_interaction.png")

# 2. 创建画布 (宽 15 inch, 高 4.5 inch)
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), dpi=300)

images = [img_a, img_b, img_c]
titles = ["(a) Diagonal Score", "(b) Centroid Tracking Error", "(c) Peak Tracking Error"]

for i, ax in enumerate(axes):
    ax.imshow(images[i])
    ax.axis("off")  # 隐藏 Pillow 绘图产生的外层坐标轴
    # 添加子图标题
    ax.set_title(
        titles[i], loc="left", fontsize=12, fontweight="bold", pad=8
    )

# 3. 补充全局共享的 X 轴标签
fig.text(
    0.5,
    0.02,
    "Executor correctness",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="semibold",
)

# 4. 调整边距并导出高分辨率图像
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("multi_panel_figure.svg", format="svg", bbox_inches="tight")
plt.savefig("multi_panel_figure.png", dpi=300, bbox_inches="tight")
plt.close()