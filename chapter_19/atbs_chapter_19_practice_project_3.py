# Custom Seating Cards

import os
from PIL import Image, ImageDraw

CARD_W, CARD_H = 360, 288


def seating_cards(guestlist):
    os.makedirs("cards", exist_ok=True)

    with open(guestlist, "r") as file:
        for line in file:
            name = line.strip()
            if not name:
                continue

            im = Image.new("RGB", (CARD_W, CARD_H), "white")
            draw = ImageDraw.Draw(im)

            # border (cut guide)
            draw.rectangle([0, 0, CARD_W - 1, CARD_H - 1], outline="black", width=2)

            # center the name
            bbox = draw.textbbox((0, 0), name)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            x = (CARD_W - tw) // 2
            y = (CARD_H - th) // 2
            draw.text((x, y), name, fill="black")

            # simple safe filename
            fname = name.replace(" ", "_")
            im.save(os.path.join("cards", f"{fname}_seating_card.png"))


seating_cards("guests.txt")
