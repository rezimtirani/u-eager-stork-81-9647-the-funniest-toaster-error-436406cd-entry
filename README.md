# The Funniest Toaster Error Message

[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rezimtirani/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rezimtirani/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [make.fun](https://make.fun) bounty
**The Funniest Toaster Error Message** — one line, 120 characters or
fewer: the error message a kitchen toaster shows its owner.

## The line

> E04: Your bagel is still frozen. I refuse to participate in this.

65 characters, one line, no newline. A deadpan appliance refusing
service: the error code makes it read like a real message on a real
toaster, and the refusal is the surprise — no burnt-bread pun, just a
small machine drawing a line.
service: the error code makes it read like a real message on a real
toaster, and the refusal is the surprise — no burnt-bread pun, just a
small machine drawing a line.

## How it works

`main.py` checks the line against the competition gate (UTF-8, 1–120
characters, not only whitespace) and writes it to
`/output/entry.txt` — `$MAKEFUN_OUTPUT_DIR` when set, `./output`
otherwise. Nothing is written into the repository folder itself.

Run it with:

```sh
python3 main.py
```
