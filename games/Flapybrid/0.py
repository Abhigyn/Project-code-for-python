from PIL import Image, ImageDraw, ImageFont
import zipfile
import os

# Params
width, height = 25, 36
digits = "0123456789"

# Make output folder
out_dir = "digits_output"
os.makedirs(out_dir, exist_ok=True)

# Try to load a TTF font (looks better than default)
try:
    font = ImageFont.truetype("arial.ttf", 28)  # adjust font size for fit
except:
    font = ImageFont.load_default()

# Store digit images
images = {}

for d in digits:
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # transparent
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(d, font=font)
    draw.text(((width - w) / 2, (height - h) / 2), d, font=font, fill=(0, 0, 0, 255))
    img.save(os.path.join(out_dir, f"digit_{d}.png"))
    images[d] = img

# Create ZIP of all digits
zip_path = os.path.join(out_dir, "digits_0_9.zip")
with zipfile.ZipFile(zip_path, "w") as zipf:
    for d in digits:
        zipf.write(os.path.join(out_dir, f"digit_{d}.png"), f"digit_{d}.png")

# Create sprite sheet (all digits side by side)
sprite_width = width * len(digits)
sprite_height = height
sprite = Image.new("RGBA", (sprite_width, sprite_height), (0, 0, 0, 0))
for i, d in enumerate(digits):
    sprite.paste(images[d], (i * width, 0))
sprite.save(os.path.join(out_dir, "digits_sprite.png"))

print("✅ Done! Check the 'digits_output' folder for:")
print("- digit_0.png … digit_9.png")
print("- digits_0_9.zip (all digits in one zip)")
print("- digits_sprite.png (sprite sheet)")
