# Decis Frecasting Bots: Amended Metaculus bot

This repository contains a version of the basic Metaculus forecasting bot forked from [```metac-bot-template```](https://github.com/Metaculus/metac-bot-template)

Info and tournament rules are [here](https://www.metaculus.com/aib/)

## Performance

The bot began well but gradually fell down the rankings and by May 13 was in last place. 🙀

## Issues, Tasks, Changelog

* Need better records of how each question was handled
  - [X] added logging to keep a better record of how each question was handled (resolved May 13)

# General Tasks
- [ ] Add and amend question parser from Orac
- [ ] Add core SMES: geopolitics, markets, climate
- [ ] Add benchmarking and feedback module (see below)

## Bot Development

Based on the [```Ideas for bot improvement```](https://github.com/Metaculus/metac-bot-template?tab=readme-ov-file#ideas-for-bot-improvements) and work on the the [```Decis Reasoning Engine```](https://github.com/agsheves/OracReasoningEngine) we plan to test and impliment:

- 🎓 Expert personalities (SMEs)
- 🌎 WorldSIM 
- 🧭 Orchestration to direct questions to the appropriate SME
- 🦹 Adversarial agents to challenge predictions
- 🔍 Supplimental research via the Decis country stability database

Core Metaculus functions and imported ```forecasting-tools``` will remain unchanged as these ensure proper perfoance related to the tournaments.

# Contact
Contact andrew@decis.ai

# Benchmarking
Provided in this project is an example of how to benchmark your bot's forecasts against the community prediction for questions on Metaculus. Running `community_benchmark.py` will run versions of your bot defined by you (e.g. with different LLMs or research paths) and score them on how close they are to the community prediction using expected baseline score (a proper score assuming the community prediction is the true probability). You will want to edit the file to choose which bot configurations you want to test and how many questions you want to test on. Any class inheriting from `forecasting-tools.Forecastbot` can be passed into the benchmarker. As of March 28, 2025 the benchmarker only works with binary questions.

To run a benchmark:
`poetry run python community_benchmark.py --mode run`

To run a custom benchmark (e.g. remove background info from questions to test retrival):
`poetry run python community_benchmark.py --mode custom`

To view a UI showing your scores, statistical error bars, and your bot's reasoning:
`poetry run streamlit run community_benchmark.py`

See more information in the benchmarking section of the [forecasting-tools repo](https://github.com/Metaculus/forecasting-tools?tab=readme-ov-file#benchmarking)
