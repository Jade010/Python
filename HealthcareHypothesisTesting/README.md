# Drug Trial Analysis

## Overview
A pharmaceutical company conducted a randomized controlled drug trial to ensure their drug outcomes are reproducible and safe. This project analyzes the trial data to determine the proportion of drugs causing adverse reactions. The analysis focuses on three main questions:

1. Does the proportion of adverse effects differ significantly between the Drug and Placebo groups?
2. Is the number of adverse effects independent of the treatment and control groups?
3. Is there a significant difference in ages between the Drug and Placebo groups?

## Approach
1. **Proportion of Adverse Effects:** Conduct a two-sided z-test to compare the proportions of adverse effects between the Drug and Placebo groups.
2. **Independence of Adverse Effects:** Perform a chi-square test to check if the number of adverse effects is independent of the treatment group.
3. **Age Differences:** Use the Mann-Whitney U test to compare ages between the Drug and Placebo groups.

## Conclusion
1. **Proportion of Adverse Effects:** There is no significant difference in the proportion of adverse effects between the Drug and Placebo groups (p-value: 0.9639).
2. **Independence of Adverse Effects:** The number of adverse effects is independent of whether participants received the Drug or Placebo (p-value: 0.62).
3. **Age Differences:** There is no significant difference in ages between the Drug and Placebo groups (p-value: 0.257).

These findings suggest that the drug's adverse effects are similar to those of the placebo, the treatment type does not affect the number of adverse reactions, and age differences are not a factor. This confirms the drug's outcomes are reproducible and its safety profile is comparable to the placebo.
