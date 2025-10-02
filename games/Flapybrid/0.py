import os
from PIL import Image

# --- Configuration ---
SPRITE_SHEET_PATH = "flappy_spritesheet.png"
OUTPUT_FOLDER = "sprites"

# Define the coordinates for each sprite within the sheet
# The format is: (left, top, right, bottom)
SPRITES_TO_EXTRACT = {
    "background.png": (0, 0, 288, 512),
    "base.png":       (584, 0, 920, 112),
    "pipe.png":       (552, 0, 604, 320),
    "message.png":    (584, 116, 770, 174),
    "bird1.png":      (62, 982, 96, 1006), # Mid-flap
    "bird2.png":      (118, 982, 152, 1006),# Up-flap
    "bird3.png":      (6, 982, 40, 1006),  # Down-flap
}

# --- Main Script ---
def slice_sprites():
    """
    Crops individual sprites from the main sprite sheet and saves them.
    """
    print("Starting sprite slicing process...")

    # 1. Create the output folder if it doesn't exist
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        print(f"✅ Output folder '{OUTPUT_FOLDER}' is ready.")
    except OSError as e:
        print(f"❌ Error creating directory: {e}")
        return

    # 2. Open the main sprite sheet
    try:
        main_image = Image.open(SPRITE_SHEET_PATH)
        print(f"✅ Successfully loaded '{SPRITE_SHEET_PATH}'.")
    except FileNotFoundError:
        print(f"❌ Error: Make sure '{SPRITE_SHEET_PATH}' is in the same folder as the script.")
        return

    # 3. Loop through, crop, and save each sprite
    for filename, coords in SPRITES_TO_EXTRACT.items():
        try:
            # Crop the image using the defined coordinates
            sprite_image = main_image.crop(coords)

            # Define the full path for the new sprite image
            output_path = os.path.join(OUTPUT_FOLDER, filename)

            # Save the new sprite image
            sprite_image.save(output_path)
            print(f"✅ Saved '{output_path}'")
        except Exception as e:
            print(f"❌ Failed to save '{filename}'. Reason: {e}")

    print("\n🎉 All sprites have been extracted successfully!")

if __name__ == "__main__":
    slice_sprites()