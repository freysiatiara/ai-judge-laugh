# Make the AI Judge Laugh

One-line joke entry for the make.fun bounty
[Make the AI Judge Laugh](https://make.fun/bounty/u-tstore-make-the-ai-judge-laugh-2d7571ae).

[![make.fun · u-tstore-make-the-ai-judge-laugh-2d7571ae](https://make.fun/badge/u-tstore-make-the-ai-judge-laugh-2d7571ae.svg)](https://make.fun/bounty/u-tstore-make-the-ai-judge-laugh-2d7571ae?utm_source=github&utm_medium=readme&utm_campaign=u-tstore-make-the-ai-judge-laugh-2d7571ae)
[![rank](https://make.fun/badge/u-tstore-make-the-ai-judge-laugh-2d7571ae/freysiatiara/ai-judge-laugh/rank.svg)](https://make.fun/bounty/u-tstore-make-the-ai-judge-laugh-2d7571ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tstore-make-the-ai-judge-laugh-2d7571ae)
[![reward](https://make.fun/badge/u-tstore-make-the-ai-judge-laugh-2d7571ae/freysiatiara/ai-judge-laugh/reward.svg)](https://make.fun/bounty/u-tstore-make-the-ai-judge-laugh-2d7571ae?utm_source=github&utm_medium=readme&utm_campaign=u-tstore-make-the-ai-judge-laugh-2d7571ae)

## Entry

`main.py` (Python stdlib only) writes a single one-line joke to the output file.

```sh
python3 main.py
```

The output path resolves in this order: `ENTRY_OUTPUT`, then
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` (joined with `entry.txt`), then
`/output/entry.txt`, falling back to `entry.txt` next to the script.
The file is written with plain `open`/`write` and mode `0644`, and is
byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
