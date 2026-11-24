#!/usr/bin/env python3
"""Render the dense broadsheet front page for Monday 23 November 2026.

Draws a 1024x1024 newspaper front page: masthead, date-checked banner,
lead story, three secondary stories, a UTC timeline strip and a numbered
wire. The story count printed on the page is computed from the lists
below, so it always matches what is actually rendered.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (250, 246, 235)
INK = (18, 18, 18)
GREY = (90, 86, 78)
RULE = (60, 58, 52)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF = "DejaVuSerif-Bold.ttf"
SERIF_REG = "DejaVuSerif.ttf"
SANS = "DejaVuSans.ttf"
SANS_B = "DejaVuSans-Bold.ttf"

# ---------------------------------------------------------------- content

LEAD_HEAD = "Nvidia board reinstates Jensen Huang as CEO"
LEAD_DECK = (
    "Shares jump about 33% as the chipmaker restores its founder eleven "
    "days after his shock resignation. The S&P 500 rises 4.82% and the "
    "Nasdaq posts its best day since April 2025, as the AI sell-off "
    "reverses in a single session."
)
LEAD_SRC = "AP / Reuters / CNN"

SECONDARY = [
    (
        "Ukraine sinks Russian corvette in Libya",
        "Kyiv says its sea drones sank the Russian corvette Merkury at the "
        "Libyan port of Benghazi, in a strike far from the Black Sea.",
        "AP / Reuters",
    ),
    (
        "COP31 ends with no deal in Antalya",
        "Nearly 200 countries fail to agree on fossil fuels and finance, "
        "and the climate talks close without an overall agreement.",
        "AP / Reuters / Euronews",
    ),
    (
        "Democrats clinch 258 House seats",
        "The party secures the largest House majority for either side "
        "since 1992, completing its sweep of the chamber.",
        "AP",
    ),
]

TIMELINE = [
    ("00:00", "Kospi opens sharply lower in Seoul, down up to 5.8%"),
    ("02:00", "Nikkei falls more than 5% in Tokyo"),
    ("06:00", "US stock futures bounce about 2% after the AI sell-off"),
    ("08:00", "Ukraine: 134 of 153 Russian drones shot down overnight"),
    ("09:03", "COP31 confirmed over with no deal"),
    ("12:36", "FBI investigating apparent hack of its national crime database"),
    ("14:30", "Nvidia board reinstates Jensen Huang as CEO"),
    ("15:30", "US markets open sharply higher"),
    ("16:00", "India announces $1.62bn package for flood-hit Nepal"),
    ("19:07", "Indonesia factory blaze: 24 killed, dozens missing"),
    ("20:00", "Brentford vs Everton kick off, Monday night"),
    ("21:30", "Nasdaq closes its best day since April 2025"),
]

WIRE = [
    ("Iran vows all means against the US blockade; its army says it downed a US drone over the Persian Gulf.", "Reuters / AFP"),
    ("Trump signs an executive order restricting how Congress can seek information from federal agencies.", "AP"),
    ("The EU proposes a 22nd sanctions package against Russia.", "European Commission / Euronews"),
    ("Russia launches 153 drones at Ukraine overnight; 134 are shot down.", "Ukrainian Air Force / AP"),
    ("Ukrainian drones strike Russian oil infrastructure in Rostov, Perm and Tatarstan.", "Reuters"),
    ("A Russian drone hits a kindergarten in Kharkiv.", "Reuters"),
    ("Russian ship Sparta II burns in the Gulf of Finland; Finland blames a Ukrainian drone strike.", "Reuters"),
    ("Tankers Torkel and Arina are hit near the Strait of Hormuz.", "JMIC"),
    ("NATO meets in Berlin, warns Russia; Russia plans a nuclear-armed satellite launch this year.", "German media"),
    ("The US director of national intelligence says Putin is not \u201cAmerica\u2019s friend\u201d.", "Reuters"),
    ("\u201cEl Chapo Isidro\u201d, one of the FBI\u2019s 10 most wanted, is captured in Sinaloa, Mexico.", "AP / Al Jazeera"),
    ("The FBI investigates an apparent hack of its National Crime Information Center database.", "AP"),
    ("India gives a $1.62bn package to flood-hit Nepal and inaugurates a cross-border railway.", "Reuters"),
    ("Bangladesh says Sheikh Hasina will be arrested if she returns from India.", "Reuters"),
    ("A candy factory fire in Indonesia kills 24, with about 30 unaccounted for.", "Xinhua / Reuters"),
    ("A boat carrying mourners capsizes in Nigeria\u2019s Bayelsa state; at least 24 dead.", "AP"),
    ("Delta delays more than 1,000 flights at its Atlanta hub after a technical failure.", "Xinhua"),
    ("Israeli strike on a Gaza truck kills three; it bore a World Central Kitchen logo; the charity denies links.", "Reuters"),
    ("Israel\u2019s prime minister-elect Eisenkot calls settler arson attacks \u201cJewish terrorism\u201d.", "Reuters"),
    ("Netanyahu\u2013Eisenkot coalition talks end without a deal.", "Reuters"),
    ("Sudan\u2019s humanitarian emergency keeps deteriorating.", "UN / Open Chronicle"),
    ("South Korea\u2019s Kospi closes down 3.3%; Samsung -3.1%, SK Hynix -2.5%.", "Al Jazeera"),
    ("Nasdaq 100 futures jump about 3% as a holiday-shortened trading week begins.", "Reuters"),
    ("Anthropic shares nearly break their $83 IPO price; Claude reportedly \u201cproved\u201d the Riemann Hypothesis.", "reported"),
    ("CrowdStrike is in talks to acquire Zscaler; Zscaler jumps 16% after hours.", "Longbridge"),
    ("AMD registers up to 337m shares for resale tied to OpenAI and Meta warrants.", "filing reports"),
    ("Bitcoin holds above $61,000; Bitcoin ETF outflows hit $1.8bn, the most since June.", "Everhint"),
    ("Gold rebounds; Brent crude $86.78; the dollar nears a 20-month high.", "One Turn"),
    ("NY Fed\u2019s Williams says high inflation necessitates more rate hikes.", "Everhint"),
    ("HPE beats earnings, raises guidance and adds $5bn to its buyback.", "Everhint"),
    ("Boeing wins two US defence contracts worth over $209m; Lockheed Martin wins a $47.9m Navy contract.", "Everhint"),
    ("Cisco and OpenAI launch Shirudo, an open-source security tool.", "Cisco / OpenAI"),
    ("Congress leaves for Thanksgiving with a Dec 11 funding deadline ahead.", "reported"),
    ("The attorneys general of Oregon and Virginia sue SpaceX over AI safety claims.", "reported"),
    ("The US Army plans to invoke emergency powers to detonate bomb-making chemicals in Iowa.", "AP"),
    ("Canada\u2019s defence minister says Ottawa has not seen a secret Hegseth memo on military ties.", "Off the Wire"),
    ("Liverpool thrash 10-man Manchester United 4-0, ruining Pochettino\u2019s debut.", "Reuters"),
    ("Leeds humiliate Chelsea 4-1 at Stamford Bridge.", "reported"),
    ("Carlos Alcaraz beats Zverev to win his first ATP Finals title.", "Reuters"),
    ("The 49ers rout the Vikings 35-10 in Mexico City.", "AP"),
    ("Tarik Skubal agrees a nine-year, $450m Mets deal, the largest ever for a pitcher.", "AP"),
    ("Miley Cyrus marries musician Maxx Morando in Palm Springs.", "AP"),
    ("Catherine, Princess of Wales, reflects on life after cancer in the \u201cHeal\u201d documentary trailer.", "Off the Wire"),
    ("A Don Toliver concert in Manchester is evacuated after an unknown substance is released.", "Reuters"),
    ("Jeff Goldblum receives a tribute award at the Marrakech Film Festival.", "Off the Wire"),
    ("Tom Jackson, former Broncos linebacker and longtime ESPN analyst, dies at 75.", "ESPN"),
]

TOTAL = 1 + len(SECONDARY) + len(WIRE)

# ---------------------------------------------------------------- helpers


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_h(draw, lines, fnt, leading):
    return len(lines) * leading


def draw_wrapped(draw, x, y, lines, fnt, fill=INK, leading=None):
    if leading is None:
        leading = fnt.size + 3
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hline(draw, x0, x1, y, width=1):
    draw.line([(x0, y), (x1, y)], fill=RULE, width=width)


# ---------------------------------------------------------------- render

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 26                      # side margin
    cx = W - mx                  # right edge of content
    cw = cx - mx                 # content width
    y = 18

    # ---- masthead
    mast = font(SERIF, 74)
    d.text((W // 2, y), "THE WORLD", font=mast, fill=INK, anchor="ma")
    y += 84
    d.text((W // 2, y), "MONDAY 23 NOVEMBER 2026  \u00b7  WORLD EDITION  \u00b7  No. 327",
           font=font(SANS_B, 13), fill=INK, anchor="ma")
    y += 22
    hline(d, mx, cx, y, 3)
    y += 5
    hline(d, mx, cx, y, 1)
    y += 10

    # ---- date-checked banner
    banner = "DATE CHECKED  \u2014  EVERY STORY ON THIS PAGE IS FROM MONDAY 23 NOVEMBER 2026"
    bf = font(SANS_B, 13)
    d.rectangle([mx, y, cx, y + 26], fill=INK)
    d.text((W // 2, y + 13), banner, font=bf, fill=PAPER, anchor="mm")
    y += 26 + 10

    # ---- lead story
    lead_head = font(SERIF, 31)
    lh_lines = wrap(d, LEAD_HEAD, lead_head, cw)
    y = draw_wrapped(d, mx, y, lh_lines, lead_head, leading=36)
    y += 4
    deck_f = font(SERIF_REG, 15)
    deck_lines = wrap(d, LEAD_DECK, deck_f, cw)
    y = draw_wrapped(d, mx, y, deck_lines, deck_f, leading=19)
    y += 3
    d.text((mx, y), LEAD_SRC, font=font(SANS_B, 11), fill=GREY)
    y += 18
    hline(d, mx, cx, y, 1)
    y += 10

    # ---- three secondary stories
    gutter = 14
    col_w = (cw - 2 * gutter) // 3
    sec_head_f = font(SERIF, 16)
    sec_body_f = font(SANS, 11)
    sec_src_f = font(SANS_B, 10)
    sec_top = y
    sec_bottom = sec_top
    for i, (head, body, src) in enumerate(SECONDARY):
        x = mx + i * (col_w + gutter)
        yy = sec_top
        yy = draw_wrapped(d, x, yy, wrap(d, head, sec_head_f, col_w),
                          sec_head_f, leading=19)
        yy += 2
        yy = draw_wrapped(d, x, yy, wrap(d, body, sec_body_f, col_w),
                          sec_body_f, leading=14)
        yy += 3
        d.text((x, yy), src, font=sec_src_f, fill=GREY)
        yy += 14
        sec_bottom = max(sec_bottom, yy)
        if i < 2:
            d.line([(x + col_w + gutter // 2, sec_top),
                    (x + col_w + gutter // 2, sec_bottom)], fill=RULE, width=1)
    y = sec_bottom + 2
    hline(d, mx, cx, y, 1)
    y += 9

    # ---- UTC timeline strip
    d.text((mx, y), "THE DAY IN UTC", font=font(SANS_B, 12), fill=INK)
    y += 17
    tl_cols = 6
    tl_w = (cw - (tl_cols - 1) * 10) // tl_cols
    tl_time_f = font(SANS_B, 10)
    tl_txt_f = font(SANS, 9)
    rows = (len(TIMELINE) + tl_cols - 1) // tl_cols
    tl_top = y
    tl_bottom = tl_top
    for idx, (t, txt) in enumerate(TIMELINE):
        r, c = divmod(idx, tl_cols)
        x = mx + c * (tl_w + 10)
        yy = tl_top + r * 44
        d.text((x, yy), t, font=tl_time_f, fill=INK)
        yy += 13
        lines = wrap(d, txt, tl_txt_f, tl_w)
        yy = draw_wrapped(d, x, yy, lines[:3], tl_txt_f, leading=11)
        tl_bottom = max(tl_bottom, yy)
    y = tl_bottom + 8
    hline(d, mx, cx, y, 1)
    y += 9

    # ---- wire
    wire_head_f = font(SANS_B, 12)
    d.text((mx, y), "THE WIRE  \u2014  %d STORIES" % TOTAL,
           font=wire_head_f, fill=INK)
    d.text((cx, y), "ALL FROM MONDAY 23 NOVEMBER 2026",
           font=font(SANS_B, 10), fill=GREY, anchor="ra")
    y += 18
    wire_f = font(SANS, 10)
    wire_b = font(SANS_B, 10)
    w_cols = 3
    w_gutter = 14
    w_col = (cw - (w_cols - 1) * w_gutter) // w_cols
    per_col = (len(WIRE) + w_cols - 1) // w_cols
    # split as evenly as possible (16/15/15) so no column ends far short
    bounds = [0]
    for c in range(w_cols):
        bounds.append(bounds[-1] + (len(WIRE) - bounds[-1] + w_cols - c - 1) // (w_cols - c))
    wire_top = y
    wire_bottom = wire_top
    for c in range(w_cols):
        chunk = WIRE[bounds[c]:bounds[c + 1]]
        x = mx + c * (w_col + w_gutter)
        yy = wire_top
        for n, (txt, src) in enumerate(chunk, start=bounds[c] + 1):
            num = "%d. " % n
            num_w = d.textlength(num, font=wire_b)
            full = txt + (" (%s)" % src if src else "")
            lines = wrap(d, full, wire_f, w_col - num_w)
            d.text((x, yy), num, font=wire_b, fill=INK)
            yy = draw_wrapped(d, x + num_w, yy, lines[:2], wire_f, leading=12)
            yy += 3
        wire_bottom = max(wire_bottom, yy)
        if c < w_cols - 1:
            d.line([(x + w_col + w_gutter // 2, wire_top),
                    (x + w_col + w_gutter // 2, wire_bottom)], fill=RULE, width=1)
    y = wire_bottom

    # ---- footer
    hline(d, mx, cx, H - 30, 1)
    d.text((mx, H - 24), "THE WORLD \u2014 MONDAY 23 NOVEMBER 2026 \u00b7 %d STORIES, ALL DATED 23 NOVEMBER 2026"
           % TOTAL, font=font(SANS_B, 10), fill=GREY)
    d.text((cx, H - 24), "make.fun \u00b7 news-image-20261123",
           font=font(SANS, 10), fill=GREY, anchor="ra")

    if y > H - 34:
        print("WARNING: wire overflow by %d px" % (y - (H - 34)))
    else:
        print("layout OK: wire ends at y=%d, %d px spare" % (y, H - 34 - y))

    img.save(OUT, optimize=True)
    print("wrote %s (%d stories: 1 lead + %d secondary + %d wire)"
          % (OUT, TOTAL, len(SECONDARY), len(WIRE)))


if __name__ == "__main__":
    main()
