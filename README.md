# Native Tab REPL (`urepl`)

A lightweight, **zero-dependency** alternative configuration for the standard interactive Python shell. 

## Why native-tab-repl?
Unlike massive REPL alternatives that require heavy third-party dependency trees (and add latency to your terminal load times), `native-tab-repl` relies entirely on pure Python built-in modules. 

### Key Features
* 🚀 **Zero Dependencies:** Pure vanilla Python under the hood. No bloated installation footprint.
* ⌨️ **Cross-Platform Tab Completion:** Seamless auto-completion out of the box using native `readline` on Unix systems and `pyreadline3` hooks automatically configured on Windows platforms.
* 🖥️ **System Insights:** Instantly greets you with environment context (OS type, active user, node host identity) via a custom shell banner.

## Installation

```bash
pip install native-tab-repl

```

## Quick Start

Once installed, simply run the custom terminal entry point command to start your session:

```bash
urepl

```

## Exit

Type `exit()` or `quit()` to drop out cleanly.

## Project Links

* **Repository:** [https://github.com/unseenumair/urepl](https://www.google.com/search?q=https://github.com/unseenumair/urepl)
* **Author:** [@UmairShakoor](https://github.com/unseenumair)
