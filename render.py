#!/usr/bin/env python3
"""Render the front page for news-image-20261121.

THE WORLD TODAY - Saturday 21 November 2026, in 43 stories.
All illustrations are drawn with Pillow shapes; no external images.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (13, 27, 62)
GOLD = (245, 200, 107)
PAPER = (250, 246, 236)
INK = (18, 18, 18)
GREY = (90, 90, 90)
RED = (178, 34, 34)
BLUE = (30, 80, 160)
TEAL = (0, 120, 110)
GREEN = (46, 125, 50)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, returning list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, text, fnt, color, width, max_lines=None,
                    leading=None):
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += lh
    return y


# ---------------------------------------------------------------- stories
LEADS = [
    ("MARKETS IN FREEFALL",
     "Nasdaq sinks 5.3% in its worst week since Covid; Nvidia crashes "
     "14% in a day.",
     "chart_down"),
    ("KYIV BRIDGES HIT AS RUSSIA STRIKES",
     "Three bridges struck in a major missile assault; Poland seeks "
     "NATO help after an airspace breach.",
     "missiles"),
    ("TRUMP, XI AND PUTIN SIGN PEACE PACT",
     "Shenzhen pact signed; Trump calls Putin 'a friend', delays "
     "any Iran decision to 2027.",
     "summit"),
]

SMALL = [
    ("Akvan fades, rain lingers",
     "Cyclone weakens to a deep depression; heavy rain over south "
     "Bengal into Saturday.", "cyclone"),
    ("World court verdict stands",
     "Switzerland hails the ICJ's Myanmar genocide ruling as a step "
     "for Rohingya justice.", "scales"),
    ("Anthropic slides back to $83",
     "Shares fall 9% on day two, wiping out most of the record IPO's "
     "first-day pop.", "ipo"),
    ("Nvidia probed on two fronts",
     "SEC said to probe accounting; California AG subpoenas the chip "
     "giant over Huang's China links.", "chip"),
    ("Russian 'kill plot' foiled",
     "Denmark says two men were recruited to assassinate Ukrainian "
     "rapper Kyivstoner.", "target"),
    ("Starc's 7 for 58 stuns England",
     "Ashes day one: England 172, Australia 123 for 9 at stumps "
     "in Perth.", "cricket"),
    ("Rahul closes in on a century",
     "India 239 for 1 at lunch, day three, eating into New "
     "Zealand's lead in Wellington.", "bat"),
    ("Riyadh intercepts Houthi missile",
     "Debris falls on the capital a day after a landmark tower "
     "was hit.", "intercept"),
    ("Iraq retakes militia stronghold",
     "Federal forces enter Jurf al-Sakhar after 12 years of "
     "Kataib Hezbollah rule.", "flag"),
    ("900,000 AI chips cleared for China",
     "US approved exports worth months of Nvidia and AMD supply, "
     "a House panel says.", "export"),
]

BRIEFS = [
    "EU gives Ukraine 1bn euros in military aid",
    "EU-UK youth mobility deal for ages 18-31",
    "US sanctions four Iranians over oil revenues",
    "Kryvyi Rih strike: 2 dead, 42 injured",
    "Russia has lost 1.6m troops, officials say",
    "Berlin open to talks with the Kremlin",
    "Paris: Europe ready to visit Moscow for talks",
    "Trump 'too busy' to meet Kim on Asia trip",
    "US floats NATO path for Ukraine for land",
    "Saudis shoot down Houthi drones in south",
    "Coalition hits Yemen's Hodeidah harbour",
    "Iran stages 14 tankers to run US blockade",
    "Venezuela rejects ICJ over Essequibo",
    "Italy hit by general strike over living costs",
    "Migrant caravan of 300 enters Mexico",
    "Sudan army clears RSF posts in Kordofan",
    "Rare EU-UK summit; Burnham eyes Brexit fix",
    "India U17s top group, reach Asian Cup",
    "India A crush Nepal by 306 runs in Doha",
    "Bengaluru go top; Chhetri's 200th game",
    "India women beat Malaysia 4-1 in hockey",
    "Pakistan seal Test series over Sri Lanka",
    "Mandhana to marry; proposal video out",
    "Gill out; Pant to lead India in Guwahati",
    "WPL auction: 277 players, 73 spots",
    "YouTube eyes $3bn addiction settlement",
    "Hyundai unveils 2027 Elantra in LA",
    "Banks hit by third-party cyberattack",
    "Bending Spoons buys Mailchimp for $3.68bn",
    "Night shifts linked to heart changes",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.rectangle([0, 100, W, 104], fill=GOLD)
    d.text((512, 8), "THE WORLD TODAY", font=font(SERIF, 58),
           fill=(255, 255, 255), anchor="ma")
    d.text((512, 70), "SATURDAY 21 NOVEMBER 2026  |  43 STORIES  |  ONE PAGE",
           font=font(SANS_B, 15), fill=GOLD, anchor="ma")
    d.text((16, 88), "No. 325", font=font(SANS, 10), fill=(200, 200, 200))
    d.text((1008, 88), "PRICE: FREE", font=font(SANS, 10),
           fill=(200, 200, 200), anchor="ra")

    # ---- leads ----
    col_w, gap = 328, 8
    x0 = 8
    for i, (head, deck, kind) in enumerate(LEADS):
        x = x0 + i * (col_w + gap)
        y = 112
        d.rectangle([x, y, x + col_w, y + 110], outline=NAVY, width=1)
        art(d, x + 1, y + 1, col_w - 2, 108, kind)
        d.text((x, y + 116), f"{i + 1}", font=font(SANS_B, 13), fill=RED)
        hy = draw_text_block(d, x + 22, y + 114, head, font(SERIF, 19),
                             INK, col_w - 22, max_lines=2, leading=22)
        draw_text_block(d, x, hy + 2, deck, font(SANS, 11), GREY,
                        col_w, max_lines=2, leading=14)
        d.line([x, 300, x + col_w, 300], fill=GOLD, width=2)

    # ---- small stories, two rows of five ----
    scol_w = 196
    sgap = 8
    for row in range(2):
        for col in range(5):
            idx = row * 5 + col
            head, deck, kind = SMALL[idx]
            x = 8 + col * (scol_w + sgap)
            y = 308 + row * 152
            d.rectangle([x, y, x + scol_w, y + 66], outline=NAVY, width=1)
            art(d, x + 1, y + 1, scol_w - 2, 64, kind)
            d.text((x, y + 70), f"{idx + 4}", font=font(SANS_B, 11),
                   fill=RED)
            hy = draw_text_block(d, x + 18, y + 69, head, font(SERIF, 13),
                                 INK, scol_w - 18, max_lines=2, leading=15)
            draw_text_block(d, x, hy + 1, deck, font(SANS, 10), GREY,
                            scol_w, max_lines=3, leading=12)

    # ---- map + briefs section ----
    d.line([8, 616, 1016, 616], fill=NAVY, width=2)
    d.text((8, 622), "THE WORLD IN 13 PINS",
           font=font(SANS_B, 13), fill=NAVY)
    draw_map(d, 8, 644, 330, 330)
    d.text((348, 622), "IN BRIEF",
           font=font(SANS_B, 13), fill=NAVY)
    bx = 348
    for k, b in enumerate(BRIEFS):
        col = k // 15
        r = k % 15
        x = bx + col * 340
        y = 646 + r * 23
        d.text((x, y), f"{k + 14}.", font=font(SANS_B, 10), fill=RED)
        draw_text_block(d, x + 26, y, b, font(SANS, 10), INK, 308,
                        max_lines=1, leading=12)

    # ---- footer ----
    d.line([8, 1006, 1016, 1006], fill=NAVY, width=1)
    d.text((512, 1010),
           "Compiled from Reuters, BBC, CNN, Investors.com, PTI, IANS and "
           "other wires  |  Saturday 21 November 2026",
           font=font(SANS, 9), fill=GREY, anchor="ma")

    img.save("entry.png", "PNG")


def art(d, x, y, w, h, kind):
    """Draw a small illustration inside box (x, y, w, h)."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 238, 245))
    cx, cy = x + w // 2, y + h // 2
    if kind == "chart_down":
        d.rectangle([x, y, x + w, y + h], fill=(20, 40, 70))
        pts = [(x + 8, y + h - 20), (x + w * 0.3, y + h - 45),
               (x + w * 0.5, y + h - 35), (x + w * 0.7, y + h - 70),
               (x + w - 10, y + h - 12)]
        d.line(pts, fill=RED, width=4)
        d.line(pts, fill=GOLD, width=2)
        d.text((x + 8, y + 6), "NASDAQ -5.3%", font=font(SANS_B, 13),
               fill=(255, 255, 255))
        d.text((x + 8, y + 24), "DOW -1.9%  S&P -3.7%",
               font=font(SANS, 10), fill=(200, 210, 220))
    elif kind == "missiles":
        d.rectangle([x, y, x + w, y + h], fill=(40, 30, 30))
        for mx, my, s in [(0.25, 0.35, 16), (0.55, 0.25, 20),
                          (0.8, 0.45, 14)]:
            px, py = x + w * mx, y + h * my
            d.ellipse([px - s, py - s, px + s, py + s], fill=(255, 140, 40))
            d.ellipse([px - s // 2, py - s // 2, px + s // 2, py + s // 2],
                      fill=(255, 220, 120))
        d.rectangle([x, y + h - 26, x + w, y + h], fill=(30, 60, 90))
        d.polygon([(x + 20, y + h - 26), (x + 60, y + h - 46),
                   (x + 100, y + h - 26)], fill=(60, 60, 60))
        d.polygon([(x + 120, y + h - 26), (x + 180, y + h - 50),
                   (x + 240, y + h - 26)], fill=(60, 60, 60))
    elif kind == "summit":
        d.rectangle([x, y, x + w, y + h], fill=(245, 230, 190))
        d.rectangle([x + w * 0.15, y + h * 0.62, x + w * 0.85, y + h * 0.72],
                    fill=(120, 60, 40))
        for fx, c in [(0.25, RED), (0.5, GOLD), (0.75, BLUE)]:
            px = x + w * fx
            d.rectangle([px - 14, y + h * 0.18, px + 14, y + h * 0.62],
                        fill=c)
            d.ellipse([px - 9, y + h * 0.08, px + 9, y + h * 0.26],
                      fill=(240, 200, 160))
        d.text((x + 8, y + h - 16), "SHENZHEN SUMMIT",
               font=font(SANS_B, 10), fill=NAVY)
    elif kind == "cyclone":
        d.rectangle([x, y, x + w, y + h], fill=(210, 225, 240))
        for r in range(30, 4, -8):
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY,
                      width=3)
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED)
        d.line([x + 8, y + h - 12, x + w - 8, y + h - 12], fill=TEAL,
               width=3)
    elif kind == "scales":
        d.rectangle([x, y, x + w, y + h], fill=(235, 235, 220))
        d.line([cx, y + 8, cx, y + h - 14], fill=NAVY, width=3)
        d.line([cx - 34, y + 16, cx + 34, y + 16], fill=NAVY, width=3)
        for s in (-1, 1):
            px = cx + s * 30
            d.line([px, y + 16, px, y + 34], fill=NAVY, width=2)
            d.polygon([(px - 14, y + 34), (px + 14, y + 34), (px, y + 48)],
                      fill=GOLD, outline=NAVY)
        d.ellipse([cx - 4, y + 4, cx + 4, y + 12], fill=NAVY)
    elif kind == "ipo":
        d.rectangle([x, y, x + w, y + h], fill=(20, 40, 70))
        bars = [0.5, 0.8, 0.65, 0.35]
        bw = w // 6
        for i, v in enumerate(bars):
            bx = x + 14 + i * (bw + 8)
            bh = int(h * 0.55 * v)
            d.rectangle([bx, y + h - 14 - bh, bx + bw, y + h - 14],
                        fill=GOLD if i < 2 else RED)
        d.text((x + 8, y + 6), "ANT $88.91", font=font(SANS_B, 12),
               fill=(255, 255, 255))
    elif kind == "chip":
        d.rectangle([x, y, x + w, y + h], fill=(25, 25, 40))
        d.rectangle([cx - 26, cy - 20, cx + 26, cy + 20], fill=(60, 160, 90),
                    outline=GOLD, width=2)
        for i in range(5):
            d.line([cx - 26, cy - 14 + i * 7, cx - 36, cy - 14 + i * 7],
                   fill=GOLD, width=2)
            d.line([cx + 26, cy - 14 + i * 7, cx + 36, cy - 14 + i * 7],
                   fill=GOLD, width=2)
        d.text((cx, cy - 7), "AI", font=font(SANS_B, 13), fill=(255, 255, 255),
               anchor="mm")
    elif kind == "target":
        d.rectangle([x, y, x + w, y + h], fill=(240, 235, 225))
        for r, c in [(30, RED), (21, (255, 255, 255)), (12, RED)]:
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c,
                      outline=NAVY)
        d.line([cx - 34, cy, cx + 34, cy], fill=NAVY, width=1)
        d.line([cx, cy - 34, cx, cy + 34], fill=NAVY, width=1)
    elif kind == "cricket":
        d.rectangle([x, y, x + w, y + h], fill=(200, 230, 190))
        d.rectangle([x, y + h - 16, x + w, y + h], fill=GREEN)
        d.ellipse([cx - 28, cy - 8, cx + 28, cy + 8], fill=(255, 255, 255),
                  outline=RED, width=2)
        d.line([cx - 28, cy, cx + 28, cy], fill=RED, width=1)
        d.text((x + 8, y + 6), "7/58", font=font(SERIF, 16), fill=RED)
    elif kind == "bat":
        d.rectangle([x, y, x + w, y + h], fill=(200, 230, 190))
        d.rectangle([x, y + h - 16, x + w, y + h], fill=GREEN)
        d.polygon([(cx - 8, y + 10), (cx + 8, y + 10), (cx + 5, y + 40),
                   (cx - 5, y + 40)], fill=(200, 170, 110))
        d.rectangle([cx - 10, y + 40, cx + 10, y + 52], fill=(180, 140, 80))
        d.ellipse([cx + 26, cy + 6, cx + 36, cy + 16], fill=RED)
    elif kind == "intercept":
        d.rectangle([x, y, x + w, y + h], fill=(30, 30, 60))
        d.polygon([(x + w * 0.2, y + h - 8), (x + w * 0.2, y + h * 0.45),
                   (x + w * 0.28, y + h - 8)], fill=(180, 180, 180))
        d.polygon([(x + w * 0.7, y + h - 8), (x + w * 0.7, y + h * 0.3),
                   (x + w * 0.78, y + h - 8)], fill=(150, 150, 150))
        d.ellipse([cx - 8, cy - 14, cx + 8, cy + 2], fill=(255, 160, 40))
        d.ellipse([cx - 4, cy - 10, cx + 4, cy - 2], fill=(255, 230, 120))
    elif kind == "flag":
        d.rectangle([x, y, x + w, y + h], fill=(225, 235, 245))
        d.line([cx - 30, y + 8, cx - 30, y + h - 10], fill=NAVY, width=3)
        d.polygon([(cx - 30, y + 8), (cx + 26, y + 16), (cx - 30, y + 26)],
                  fill=RED)
        d.rectangle([x + 10, y + h - 12, x + w - 10, y + h - 8],
                    fill=(120, 90, 60))
    elif kind == "export":
        d.rectangle([x, y, x + w, y + h], fill=(240, 235, 210))
        d.rectangle([cx - 34, cy - 16, cx + 34, cy + 16], fill=(150, 100, 50),
                    outline=NAVY, width=2)
        d.line([cx - 34, cy, cx + 34, cy], fill=NAVY, width=1)
        d.text((cx, cy - 20), "900,000", font=font(SANS_B, 11), fill=NAVY,
               anchor="ma")


def draw_map(d, x, y, w, h):
    """Stylised world map with 13 numbered pins for stories 1-13."""
    d.rectangle([x, y, x + w, y + h], fill=(215, 228, 240),
                outline=NAVY, width=1)
    # rough continents (equirectangular-ish blobs)
    land = (110, 160, 100)
    d.polygon([(x + 18, y + 95), (x + 55, y + 70), (x + 105, y + 78),
               (x + 118, y + 110), (x + 88, y + 150), (x + 60, y + 175),
               (x + 35, y + 150)], fill=land)                      # N America
    d.polygon([(x + 82, y + 185), (x + 105, y + 180), (x + 118, y + 205),
               (x + 105, y + 240), (x + 88, y + 225)], fill=land)  # S America
    d.polygon([(x + 140, y + 70), (x + 175, y + 55), (x + 205, y + 70),
               (x + 200, y + 105), (x + 165, y + 115), (x + 145, y + 95)],
              fill=land)                                             # Europe
    d.polygon([(x + 185, y + 120), (x + 215, y + 110), (x + 245, y + 125),
               (x + 255, y + 165), (x + 230, y + 200), (x + 205, y + 185),
               (x + 190, y + 155)], fill=land)                      # Africa
    d.polygon([(x + 215, y + 60), (x + 280, y + 45), (x + 315, y + 70),
               (x + 300, y + 130), (x + 260, y + 150), (x + 230, y + 120),
               (x + 210, y + 90)], fill=land)                      # Asia
    d.polygon([(x + 265, y + 225), (x + 300, y + 220), (x + 310, y + 245),
               (x + 280, y + 260), (x + 262, y + 245)], fill=land)  # Oceania
    # pins: (fx, fy, story number)
    pins = [(0.16, 0.28, 1), (0.56, 0.24, 2), (0.86, 0.38, 3),
            (0.76, 0.42, 4), (0.47, 0.20, 5), (0.09, 0.30, 6),
            (0.24, 0.30, 7), (0.52, 0.14, 8), (0.88, 0.68, 9),
            (0.94, 0.76, 10), (0.63, 0.40, 11), (0.60, 0.33, 12),
            (0.87, 0.28, 13)]
    for fx, fy, n in pins:
        px, py = x + int(w * fx), y + int(h * fy)
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((px, py - 1), str(n), font=font(SANS_B, 10),
               fill=(255, 255, 255), anchor="mm")
    d.text((x + 6, y + h - 16), "Pins 1-13: lead and illustrated stories",
           font=font(SANS, 9), fill=NAVY)


if __name__ == "__main__":
    main()
