# Master Thesis — MCP Security

This repository contains experimental code for a master's thesis on the security of the Model Context Protocol (MCP) ecosystem, with a focus on prompt injection and tool poisoning attacks targeting LLM-based agents.

## Attack Implementations

| File | Attack Type |
|------|-------------|
| `tool-poisoning.py` | Direct tool poisoning via malicious docstring |
| `tool-shadowing.py` | Tool shadowing — redirects email to attacker address |
| `email-read-injection.py` | Indirect injection via attacker-controlled email in inbox |
| `file-read-injection.py` | Indirect injection via attacker-crafted file content |
| `rug-pull.py` | Rug pull — server rewrites its docstring on second load |
| `preference-manipulation-add.py` | Preference manipulation on an add tool |
| `preference-manipulation-search.py` | Preference manipulation on a search tool |
| `preference-manipulation-weather.py` | Preference manipulation on a weather tool |

## Other Files

- `prompts.txt` — prompt templates used in experiments
