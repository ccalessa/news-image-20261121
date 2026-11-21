# news-image-20261121

make.fun bounty entry: "Sum up 21 November's world news in one image".

A newspaper front page (`THE WORLD TIMES`, Saturday, November 21, 2026) that
summarises the day's consequential world news across regions and fields:
Russia's mass strike on Ukraine with missiles landing in Poland, the ICJ
genocide ruling on Myanmar, the AI-driven market sell-off, the Trump–Xi–Putin
summit, a pancreatic-cancer pill breakthrough, Houthi missiles over Riyadh, a
Peru earthquake, and Denmark expelling a Russian diplomat.

## Entry
- `main.py` (Python 3.13, stdlib only): copies `entry.png` to `/output/entry.png`.
- `entry.png`: PNG, 683×1024 px, ~118 KB, deterministic (no network, no clock).
- `render.py`: build-time renderer used to produce `entry.png` (not part of grading).

## Grading
The program runs twice in a sandbox with no network; both runs must write the
same bytes. The gate accepts a whole PNG/JPEG of at most 1 MiB and 1024×1024 px.

## License
MIT (OSI-approved).
