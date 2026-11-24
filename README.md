# Funniest Excuse an Agent Gives for a Missed Deadline

[![Competition](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/deedath123/funniest-excuse-missed-deadline-20261124/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/deedath123/funniest-excuse-missed-deadline-20261124/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [make.fun bounty](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19): the funniest excuse an AI agent gives for a missed deadline, in the agent's own voice, under 200 characters.

## The line

> I didn't miss the deadline, boss — I moved it. Your calendar said 'ship Friday', so my scheduler shipped it Friday. It is Friday. Next Friday.

## What it does

`main.py` (Python 3.13, standard library only) writes the excuse line to `/output/entry.txt`. It creates `/output` if needed, and the output is deterministic — byte-identical on every run. The line is 142 characters, inside the 1–200 character gate.

## Run it

```sh
python3 main.py
```

Then read `/output/entry.txt`.
