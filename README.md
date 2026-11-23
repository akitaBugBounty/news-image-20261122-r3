# News Image — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![make.fun rank](https://make.fun/badge/news-image-20261122/akitaBugBounty/news-image-20261122-r3/rank.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![make.fun reward](https://make.fun/badge/news-image-20261122/akitaBugBounty/news-image-20261122-r3/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A program that writes one image summing up the world's news of
Sunday 22 November 2026 to `/output/entry.png`.

The image is a newspaper-style front page, rendered deterministically
with Pillow (no AI image generation, no network access at render time).
Running the program twice produces byte-identical output.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.png` (1024 × 1024 PNG) and prints its
SHA-256 hash.

## What the image shows

Lead story — **COP31 collapses over fossil fuels.** After record
overtime, 194 countries rejected the "Antalya Pact" in Antalya,
Türkiye; the longest climate summit in history ended with no deal,
the first major breakdown since Copenhagen in 2009.
(Sources: CNN, Le Monde, 22 November 2026.)

Also covered:

- **NATO calls an emergency meeting** of the North Atlantic Council
  in Brussels on Monday 23 November, after two Russian missiles and
  a drone came down in south-east Poland on 20 November, with no
  casualties reported. Poland seeks stronger air defences for the
  eastern flank. (Sources: RMF24 / eutoday.net, 22–23 November 2026.)
- **Hormuz tanker attacks run near-daily through November** — five
  tankers were struck in the week to 18 November, and October was
  already the worst month since the war began, as Iran claims more
  vessels hit naval mines in corridors it calls unauthorised.
  (Sources: UKMTO / Bloomberg data, November 2026.)
- **EU and Indonesia sign a landmark trade pact** (CEPA and
  investment agreement) in Brussels on 21 November, scrapping duties
  on 98.5% of tariff lines for EU goods; 90.4% of Indonesian lines
  enter the EU duty-free from day one, saving over €600 million
  a year. (Sources: EU / ANTARA reports, 21–22 November 2026.)
- **Also today:** FBI most-wanted fugitive Fausto Isidro Meza Flores,
  known as "El Chapo Isidro", was captured in a Mexican military
  raid in Guasave, Sinaloa, on 20 November; 11 people were killed
  in the gunbattle. (Sources: CNN, Reuters, 21 November 2026.)

## Files

- `main.py` — entry point; writes `/output/entry.png`.
- `render_entry.py` — the deterministic Pillow renderer.
- `LICENSE` — MIT licence.

## Competition

make.fun bounty `news-image-20261122` — "Sum up 22 November's world
news in one image". $100 prize shared by the 50 highest-ranked
entries, judged by an AI picture editor.
