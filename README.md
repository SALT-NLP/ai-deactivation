# AI Deactivation Reduces Loneliness and Increases Social Interaction

This repository contains the de-identified data and analysis code for "AI Deactivation Reduces Loneliness and Increases Social Interaction." The supplementary information is in `supplementary.pdf`.

## Cite 
Please cite this work as follows:
```bibtex
@misc{zhao2026deactivation,
  title     = {AI Deactivation Reduces Loneliness and Increases Social Interaction},
  author    = {Zhao, Dora and Wang, Grace and Zhang, Yutong and Ibrahim, Lujain and Kraut, Robert E. and Yang, Diyi},
  year      = {2026},
  publisher = {},
  doi       = {},
  url       = {},
}
```

## Repository Structure
```
├── data/                     # Study data
├── analysis/                 # Analysis notebooks (R / Quarto and Python / Jupyter)
├── supplementary.pdf         # Supplementary information
├── pyproject.toml, uv.lock   # Python environment
└── LICENSE
```

## Data Files
Data used in our analysis are in the `data` folder. Participants are identified by an anonymized `pid`. Survey-based variables prefixed with `baseline_` are measured at the baseline survey and serve as covariates.

- `participant_data.csv`: Wide-format data with one row per participant (N = 625). Includes treatment assignment, demographics, AI chatbot usage characteristics, and item-level and scale-level survey responses at each wave (e.g., emotional state, loneliness, well-being, basic psychological needs (BPNSFS), Lubben social network scale).
- `participant_data_long.csv`: Long-format survey data with one row per participant per wave (`baseline`, `diary1`, `midline`, `diary2`, `endline`). Includes treatment, `isDeactivation` (whether the wave falls within the deactivation window), baseline covariates, and primary and secondary outcomes.
- `participant_data_eod.csv`: Long-format end-of-day (daily diary) responses with one row per participant per day. Includes daily emotional state, emotional state index (`esi`), time spent working and socializing, and number of social interactions.
- `conversation_titles.csv`: Titles of participants' AI chatbot conversations, each labeled with a conversation topic (`capability`), along with the classifier's confidence and reasoning.
- `mice_imp.rds`: Cached multiple imputation (MICE) object used in `Attrition Sensitivity.qmd`. The notebook reuses it if it matches the current imputation frame and regenerates it otherwise.

## Analysis Files
Code for the analyses reported in the paper is in the `analysis` folder. All notebooks read data from `../data/`, so run them from inside `analysis/`.

For general metadata (participant demographics and AI usage), refer to `metadata.ipynb`. For information on the conversation topics, refer to `conversation_topic.ipynb`. `variable_mappings.py` contains the mappings from raw survey responses to numeric scores and demographic categories.

For the results reported in the main body of the paper, refer to the following analysis files:
- `Primary Analysis.qmd` covers the analyses reported in Sec. 2.1 and Sec. 2.3 (primary, secondary, daily outcomes, and moderators). It also includes robustness analyses in which we fit our primary models without additional baseline demographic covariates (reported in SI, Sec. 4.3).
- `Mediation.qmd` covers the mediation analyses reported in Sec. 2.2.
- `Post Analyses.qmd` covers the analyses reported in Sec. 2.4 (outcomes after AI access resumes, including usage and problematic use). It also includes robustness analyses in which we weight results by the inverse probability of completing the post survey; the resulting table is saved to `ipw_primary.tex`.

For additional results reported in the supplementary information, refer to the following files:
- `Attrition Sensitivity.qmd` reports analyses under different missing data assumptions (complete case analysis and multiple imputation with MICE), as reported in SI, Sec. 3.
- `Robustness Analyses.qmd` reports the robustness analyses in SI, Sec. 4, including IPW-adjusted ANCOVA for baseline-to-endline outcomes and instrumental variables regression.

## Setup

### R
The `.qmd` files require R and [Quarto](https://quarto.org/). Install the required packages with:
```r
install.packages(c(
  "tidyr", "dplyr", "readr", "lme4", "lmerTest", "ggplot2", "mediation",
  "emmeans", "performance", "stargazer", "lavaan", "sandwich", "lmtest",
  "mice", "broom.mixed", "ivreg"
))
```
Render a notebook with, e.g., `quarto render "analysis/Primary Analysis.qmd"`, or run it interactively in RStudio.

### Python
The Jupyter notebooks require Python ≥ 3.12. Using [uv](https://docs.astral.sh/uv/):
```bash
uv sync
uv run --with jupyter jupyter lab
```
