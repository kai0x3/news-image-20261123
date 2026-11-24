# The World — Monday 23 November 2026

[![News Image 23 Nov](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/kai0x3/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/kai0x3/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

A dense one-page newspaper front page summing up world news on Monday 23 November 2026. It carries **50 stories** — one lead, three secondary stories and a 46-item numbered wire — every one of them dated to that single day and attributed to its source inline. The lead is Nvidia's board reinstating Jensen Huang as CEO eleven days after his resignation, sending shares up about 33% and the Nasdaq to its best day since April 2025. A "The Day in UTC" strip runs twelve timed events from the Kospi's sharp fall at midnight to the Nasdaq's close at 21:30, and a black "DATE CHECKED" banner states plainly that every story on the page is from Monday 23 November 2026.

## The day in headlines

- Nvidia's board reinstates Jensen Huang as CEO; shares jump about 33%, the S&P 500 rises 4.82% and the Nasdaq posts its best day since April 2025.
- Ukraine says its sea drones sank the Russian corvette Merkury at the Libyan port of Benghazi.
- COP31 climate talks in Antalya end with no overall agreement after nearly 200 countries fail to agree on fossil fuels and finance.
- Democrats clinch at least 258 House seats, the largest House majority for either party since 1992.
- Iran says it will use all means against the US blockade and its army says it shot down a US drone over the Persian Gulf.
- A candy factory fire in Indonesia kills 24, with about 30 unaccounted for.
- Liverpool thrash 10-man Manchester United 4-0, ruining Pochettino's debut.
- Carlos Alcaraz beats Zverev to win his first ATP Finals title.
- Tarik Skubal agrees a nine-year, $450m Mets deal, the largest ever for a pitcher.

## How it is built

`build_image.py` draws the 1024×1024 front page with Pillow (DejaVu fonts) — masthead, date-checked banner, lead, three secondary stories, the UTC timeline strip and the numbered wire — and computes the printed story count from the story lists themselves, so the number on the page always matches what is rendered. The result is saved as `entry.png`. `main.py` (Python 3 standard library only) copies `entry.png` into `$MAKEFUN_OUTPUT_DIR` (default `/output`), deterministically, and exits non-zero with a clear message if the artwork is missing.

## Sources

AP, Reuters, AFP, BBC, Al Jazeera, Euronews, Xinhua, ESPN, CNN, Longbridge, Everhint, One Turn, Off the Wire, the European Commission, the Ukrainian Air Force, the Joint Maritime Information Center (JMIC), and the United Nations / Open Chronicle. Every story on the page names its source in parentheses next to the item.

## Competition

Built for the make.fun bounty [News Image 23 Nov](https://make.fun/bounty/news-image-20261123) (`news-image-20261123`), as [@kai0x3](https://github.com/kai0x3).
