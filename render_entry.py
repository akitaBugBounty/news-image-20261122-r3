#!/usr/bin/env python3
"""Deterministic newspaper-style renderer for the 22 November 2026 image.

No network access, no randomness. Calling render() twice produces
byte-identical output.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 48
CONTENT_W = W - 2 * MARGIN

BG = (247, 243, 232)
INK = (20, 20, 20)
RED = (178, 34, 34)
GREY = (105, 100, 90)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = FONT_DIR + "/DejaVuSerif.ttf"
SERIF_BOLD = FONT_DIR + "/DejaVuSerif-Bold.ttf"
SANS = FONT_DIR + "/DejaVuSans.ttf"
SANS_BOLD = FONT_DIR + "/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines fitting width."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, path, max_size, min_size, width, max_lines):
    """Largest size in [min_size, max_size] whose wrap fits max_lines."""
    for size in range(max_size, min_size - 1, -1):
        fnt = font(path, size)
        lines = wrap(draw, text, fnt, width)
        if len(lines) <= max_lines:
            return fnt, lines
    fnt = font(path, min_size)
    return fnt, wrap(draw, text, fnt, width)


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def render(path):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Top bar: date left, label right.
    draw.rectangle([0, 0, W, 44], fill=INK)
    bar_font = font(SANS_BOLD, 20)
    draw.text((MARGIN, 11), "SUNDAY, 22 NOVEMBER 2026", font=bar_font, fill=WHITE)
    right = "ONE IMAGE  \u2022  ONE DAY"
    rw = draw.textlength(right, font=bar_font)
    draw.text((W - MARGIN - rw, 11), right, font=bar_font, fill=WHITE)

    # Masthead, auto-fit to a single line.
    mast_font, mast_lines = fit_lines(
        draw, "THE WORLD IN ONE IMAGE", SERIF_BOLD, 66, 40, CONTENT_W, 1
    )
    draw.text((MARGIN, 58), mast_lines[0], font=mast_font, fill=INK)

    # Tagline, centred.
    tag_font = font(SERIF, 22)
    tag = "The day's world news, summed up in a single picture"
    tw = draw.textlength(tag, font=tag_font)
    draw.text(((W - tw) / 2, 138), tag, font=tag_font, fill=GREY)

    # Double rule.
    draw.line([(MARGIN, 172), (W - MARGIN, 172)], fill=INK, width=3)
    draw.line([(MARGIN, 178), (W - MARGIN, 178)], fill=INK, width=1)

    # Lead kicker.
    kick_font = font(SANS_BOLD, 22)
    draw.text(
        (MARGIN, 194), "CLIMATE  \u2022  ANTALYA, T\u00dcRKIYE", font=kick_font, fill=RED
    )

    # Lead headline, auto-fit to at most two lines.
    head_font, head_lines = fit_lines(
        draw, "COP31 COLLAPSES OVER FOSSIL FUELS", SERIF_BOLD, 60, 40, CONTENT_W, 2
    )
    y = draw_lines(draw, head_lines, MARGIN, 226, head_font, INK, 64)

    # Deck.
    deck_font = font(SERIF, 23)
    deck = (
        "After record overtime, 194 countries reject the 'Antalya Pact'. "
        "The longest climate summit in history ends with no deal \u2014 "
        "the first major breakdown since Copenhagen in 2009."
    )
    deck_lines = wrap(draw, deck, deck_font, CONTENT_W)
    y = draw_lines(draw, deck_lines, MARGIN, y + 8, deck_font, INK, 30)

    # Rule above the columns, positioned from the deck.
    rule_y = y + 14
    draw.line([(MARGIN, rule_y), (W - MARGIN, rule_y)], fill=INK, width=2)

    # Three columns.
    gap = 32
    col_w = (CONTENT_W - 2 * gap) // 3
    columns = [
        (
            "SECURITY \u2014 BRUSSELS",
            "NATO calls emergency meeting after missiles fall in Poland",
            "An emergency North Atlantic Council session meets on Monday "
            "in Brussels after two Russian missiles and a drone came down "
            "in south-east Poland on 20 November. No casualties were "
            "reported; Warsaw seeks stronger air defences for the eastern flank.",
        ),
        (
            "ENERGY \u2014 STRAIT OF HORMUZ",
            "Hormuz tanker attacks run near-daily through November",
            "Five tankers were struck in the week to 18 November, monitors "
            "say, as Iran claims more vessels hit naval mines in corridors "
            "it calls unauthorised. October was already the worst month "
            "since the war began.",
        ),
        (
            "TRADE \u2014 BRUSSELS",
            "EU and Indonesia sign landmark trade pact",
            "The CEPA and investment deal signed on 21 November scraps "
            "duties on 98.5% of tariff lines for EU goods; 90.4% of "
            "Indonesian lines enter the EU duty-free from day one, saving "
            "over \u20ac600 million a year.",
        ),
    ]
    x = MARGIN
    col_top = rule_y + 18
    for kicker, headline, body in columns:
        col_kick_font = font(SANS_BOLD, 18)
        kick_lines = wrap(draw, kicker, col_kick_font, col_w)
        cy = draw_lines(draw, kick_lines, x, col_top, col_kick_font, RED, 23)
        col_head_font, col_head_lines = fit_lines(
            draw, headline, SERIF_BOLD, 30, 24, col_w, 4
        )
        cy = draw_lines(draw, col_head_lines, x, cy + 6, col_head_font, INK, 34)
        body_font = font(SERIF, 19)
        body_lines = wrap(draw, body, body_font, col_w)
        draw_lines(draw, body_lines, x, cy + 6, body_font, INK, 26)
        x += col_w + gap

    # Footer bar.
    draw.rectangle([0, 914, W, 984], fill=INK)
    foot_font = font(SANS_BOLD, 20)
    foot = (
        "ALSO TODAY  \u2022  FBI most-wanted 'El Chapo Isidro' captured "
        "in Mexico raid \u2014 11 killed in gunbattle"
    )
    foot_lines = wrap(draw, foot, foot_font, CONTENT_W)
    fy = 914 + (70 - len(foot_lines) * 26) // 2
    for line in foot_lines:
        lw = draw.textlength(line, font=foot_font)
        draw.text(((W - lw) / 2, fy), line, font=foot_font, fill=WHITE)
        fy += 26

    # Sources line.
    src_font = font(SANS, 15)
    src = (
        "Sources: CNN  \u2022  Le Monde  \u2022  UKMTO  \u2022  EU / ANTARA  "
        "\u2022  Reuters  \u2014  21\u201322 November 2026"
    )
    sw = draw.textlength(src, font=src_font)
    draw.text(((W - sw) / 2, 994), src, font=src_font, fill=GREY)

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    img.save(path, format="PNG")


if __name__ == "__main__":
    render("/output/entry.png")
