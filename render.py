#!/usr/bin/env python3
"""Render a newspaper front page for 21 November 2026 world news (deterministic)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 683, 1024
PAPER = (251, 247, 236)      # warm newsprint cream
INK = (26, 26, 26)
RED = (139, 0, 0)
GRAY = (80, 80, 80)

F = "/usr/share/fonts/truetype/dejavu/"
serif = F + "DejaVuSerif.ttf"
serif_b = F + "DejaVuSerif-Bold.ttf"
sans = F + "DejaVuSans.ttf"
sans_b = F + "DejaVuSans-Bold.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_size(path, text, maxw, start=48, min_size=14):
    size = start
    while size > min_size:
        f = font(path, size)
        if d.textlength(text, font=f) <= maxw:
            return f
        size -= 1
    return font(path, min_size)


def wrap(text, fnt, maxw):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, fnt, fill=INK):
    d.text((x, y), s, font=fnt, fill=fill)


def hrule(y, x0=28, x1=W - 28, color=INK, w=1):
    d.line([(x0, y), (x1, y)], fill=color, width=w)


# ---- Masthead ----
mast = font(serif_b, 56)
title = "THE WORLD TIMES"
text((W - d.textlength(title, font=mast)) / 2, 30, title, mast, INK)
hrule(100, color=INK, w=3)
hrule(108, color=INK, w=1)

# dateline
dl = font(sans_b, 15)
text(28, 120, "SATURDAY, NOVEMBER 21, 2026", dl, INK)
right = "WORLD EDITION  —  $1.00"
rw = d.textlength(right, font=dl)
text(W - 28 - rw, 120, right, dl, INK)
hrule(144, color=INK, w=2)

# ---- Lead headline (auto-fitted to width) ----
MAXW = W - 56
lead_f = fit_size(serif_b, "RUSSIA POUNDS UKRAINE;", MAXW, start=44)
lh = d.textlength("Ag", font=lead_f)
lead1 = "RUSSIA POUNDS UKRAINE;"
lead2 = "MISSILES FALL IN POLAND"
y = 164
text(28, y, lead1, lead_f, INK)
y += int(lh * 1.05) + 4
text(28, y, lead2, lead_f, INK)
y += int(lh * 1.05) + 14

# deck
deck = font(sans, 17)
deck_txt = ("500 drones and 110 missiles hit Kyiv and other cities overnight; "
            "NATO scrambles jets after two missiles and a drone fall on Polish soil.")
for i, ln in enumerate(wrap(deck_txt, deck, MAXW)):
    text(28, y, ln, deck, GRAY)
    y += 22
y += 8

# body
body = font(serif, 15)
body_txt = ("At least eight killed in the capital; bridges and railway stations damaged. "
            "PM Tusk calls the strikes a \u201cdeliberate provocation\u201d; "
            "a later hit on Kryvyi Rih wounded about 20.")
for i, ln in enumerate(wrap(body_txt, body, MAXW)):
    text(28, y, ln, body, INK)
    y += 20
y += 14
hrule(y, color=INK, w=2)
y += 16

# ---- Two-column stories ----
colw = (W - 56 - 24) / 2
kick = font(sans_b, 13)
head = font(serif_b, 19)
bdy = font(serif, 13)

stories_left = [
    ("WORLD COURT", "ICJ rules Myanmar committed genocide",
     "First time a state is held responsible; court orders the return of the Rohingya and reparations."),
    ("MARKETS", "AI rout pushes S&P 500 into correction",
     "Stocks fall 3.7%; the Nasdaq erases its 2026 gains as chip shares slide worldwide."),
    ("DIPLOMACY", "Trump, Xi and Putin hold first summit",
     "Trump calls Putin \u201ca friend\u201d; Zelensky answers, \u201cHe\u2019s a killer.\u201d Little concrete agreed."),
    ("HEALTH", "Cancer pill shows major breakthrough",
     "Daraxonrasib left tumours undetectable in one in 12 pancreatic-cancer patients."),
]
stories_right = [
    ("MIDDLE EAST", "Houthi missiles intercepted over Riyadh",
     "Saudi-led coalition downs three ballistic missiles; third night of alerts over the capital."),
    ("AMERICAS", "Magnitude 6.7 quake shakes Peru",
     "Epicentre near Jun\u00edn in the Andes; no deaths or major damage reported."),
    ("EUROPE", "Denmark expels Russian diplomat",
     "Intelligence links Moscow to a plot to kill a Ukrainian rapper near Copenhagen."),
    ("WORLD BRIEFS", "GTA VI nets $3.8bn on day one",
     "Rockstar\u2019s record launch; South Africa\u2019s ANC posts its worst local result since 1994."),
]


def draw_story(x, top, kicker, hl, bodyline):
    yy = top
    text(x, yy, kicker, kick, RED)
    yy += 18
    for ln in wrap(hl, head, colw):
        text(x, yy, ln, head, INK)
        yy += 24
    yy += 2
    for ln in wrap(bodyline, bdy, colw):
        text(x, yy, ln, bdy, GRAY)
        yy += 17
    return yy


left_y = y
right_y = y
for (k, h, b) in stories_left:
    left_y = draw_story(28, left_y, k, h, b) + 16
for (k, h, b) in stories_right:
    right_y = draw_story(28 + colw + 24, right_y, k, h, b) + 16

# ---- Footer ----
foot = font(sans_b, 13)
text(28, H - 30, "THE WORLD TIMES  \u00b7  SATURDAY, NOVEMBER 21, 2026", foot, GRAY)
pg = "A1"
pw = d.textlength(pg, font=foot)
text(W - 28 - pw, H - 30, pg, foot, GRAY)

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size, "max_story_y", max(left_y, right_y))
