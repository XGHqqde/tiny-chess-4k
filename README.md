# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/XGHqqde/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/XGHqqde/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python. The whole engine is `main.py`, which unpacks itself at startup: negamax alpha-beta search with a transposition table, quiescence search, null-move pruning and late-move reductions over a tapered piece-square evaluation. It searches to a fixed node budget, never a clock, so every game replays move for move. It plays the make.fun tiny-chess-01 house gauntlet (eight engines, anchored 855 to 1712) through the trial env.

## Run it

```sh
MAKEFUN_ENV_URL=<trial env url> python3 main.py
```

The engine reads the env's address from `MAKEFUN_ENV_URL` and plays every game of the gauntlet, one after another. With the competition's dev kit it is graded the same way the server grades it: `node cli/makefun.mjs grade-local --kit . --bot <this repo> --driver docker`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=h2p0r5nf&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
