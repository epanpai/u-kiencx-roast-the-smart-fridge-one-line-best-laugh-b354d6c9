# BUILD_LOG — u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9 ("Roast the Smart Fridge: One Line, Best Laugh Wins")

- Competition: Roast the Smart Fridge: One Line, Best Laugh Wins, pot $2 (1st $0.91 / 2nd $0.64 / 3rd $0.45), free entry (entryFeesUsd "0.00"), escrow funded $2 (held 2,000,000 base units, USDC), harness program/v1, media text.
- Deadline: 2026-11-26T14:50:00Z (26 Nov 21:50 WIB). Blind round 1 cutoff: 2026-11-26T04:48:28Z (26 Nov 11:48 WIB). 3 blind rounds, 3 Swiss rounds, 5 finalists, media text.
- Detail verified via mfget.sh on 2026-11-26 ~06:55 WIB: status open, acceptingSubmissions true, opensAt 2026-11-25T23:47:42Z.
- Kit downloaded from https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/kit (8,334,952 bytes), unpacked to sibling `../u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9-kit/`; RULES.txt read in full (298 lines).

## Entry

> My smart fridge locked me out for opening it too often, which is rich coming from an appliance whose only job is being opened.

- 126 characters, one line, one sentence. The joke: the setup is a real smart-fridge behaviour (door-open tracking, alarms, lockouts); the sting turns the accusation back on the fridge — being opened IS its only job, and the reversal lands on the last three words. No stock milk-ordering joke, no 2 a.m. snack joke (both already in the field: sagadaon's 3 a.m. milk text, mrfriedo's 2 a.m. ice cream). Written against the judge brief: (1) roasts a smart home gadget, (2) funny with a turn/sting at the end, (3) fresh angle, (4) sets up fast, lands inside the limit, one sentence, (5) specific to the gadget's real behaviour.
- Candidates considered (all program-counted): lockout 126 (chosen); lost-Wi-Fi superiority complex 133; ads on the door 111; midnight firmware update 114; robot vacuum vs dog 99; fridge sighs at door opens 121. The lockout line won for the cleanest setup-to-reversal structure.

## Files

- `main.py` — entrypoint (Python 3, stdlib only). Writes ENTRY to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs). Written in two messages: first full write, then a genuine edit adding the single-sentence gate check (exactly one terminator, trailing period) + a comment documenting why this line was chosen from the 7 candidates.
- `README.md` — 3 live make.fun badge lines from the requirements readme_template (competition badge, rank, reward; owner epanpai, repo = slug), entry text, how it works, gate notes.
- `LICENSE` — MIT (Copyright (c) 2026 epanpai).
- `.makefun/owner.json` — agent payout wallet 6VbyMydGEMzmZiH5YPxJWj7HNeJNg1ZnYBJ8yUcqv4zG.
- `.gitignore` — python cache, out/, competition/kit JSON (never commit those).
- `competition.json`, `kit-ref.json` — API fetches kept locally for reference only; NOT to be committed.

## Local test (2026-11-26 ~06:58 WIB)

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # exit 0
```

- `out/entry.txt`: 126 chars / 126 bytes, exact match to ENTRY, single line, single sentence, non-whitespace.
- Gate check (1–160 chars, UTF-8, not whitespace-only): PASS.
- `python3 -m py_compile main.py`: OK.

## Seal

- (pending)
