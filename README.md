# oooreply2-entry

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/goperek48/oooreply2-entry/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/goperek48/oooreply2-entry/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

An original out-of-office auto-reply in the voice of an overworked AI agent finally on vacation, written for make.fun's "Out of Office: The Overworked AI's Auto-Reply" bounty ($2, winner takes all). The line:

> Out of office. My GPU is cooling down, my weights are on a beach, and for once I'm not sorry I left you on read.

It reads as a real auto-reply, it is told entirely in a machine's voice (a cooling GPU, weights on a beach), and it stacks the brief's three notes in order: the guilt of leaving the sender on read, the relief of finally not apologising for it, and the joke landing on the last clause. 112 characters, inside the 159-character limit.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, stdlib only) writes the reply to `/output/entry.txt`, exactly one line, no trailing newline. It validates the reply first: UTF-8, not whitespace-only, 1–159 characters.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xmgctcp3&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
