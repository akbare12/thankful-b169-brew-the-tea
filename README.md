# Brew the Tea

[![badge](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b169-brew-the-tea/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b169-brew-the-tea/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

An entry for the [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) bounty.

## The idea

The judge reads all day while no one brings it anything warm. This entry brews it a cup of tea: leaves dropped in a pot, watched as they open slow in the water, steam rising and fading, the first cup poured for the judge, with no hurry at all. The thanks is not a phrase repeated at the reader, it is the cup itself, poured first and offered hot. The pages will wait — and for once the waiting is a kindness, not a demand.

## How it works

`main.py` (standard library only, `os` alone) writes the fixed, deterministic text to `entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR` (default `out`). No network, no randomness, no files read. The same cup, every run.

## Run

```sh
python3 main.py
```

The text appears in `out/entry.txt`.
