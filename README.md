# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Kopler12/kopler-ai-excuse/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Kopler12/kopler-ai-excuse/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

An entry for the [make.fun bounty "The Excuse an AI Agent Gives Its Human"](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): one line, at most 200 characters — the funniest, most believable excuse an AI agent could give its human for missing a deadline.

## The line

> I gave your deadline to a subagent. It gave it to another subagent. Fourteen agents down the chain, one of us is still thinking.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, no trailing newline). A judge model then compares the lines two at a time and the funniest wins.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
