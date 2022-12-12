## Reading week 11 BRJ

## A Machine learning approach to analyze and support anti-corruption policy

## Very short summary
The paper considers a model that can predict whether there will be corruption present in a municipality in Brazil. These predictions can then be used to support policy responses. 

After constructing the model, the paper continues to assess how the model can be used to support policy.

One of the problems with corruption is that corrupt actors have strong incentives to hide their actions, and hence measurements of corruption are results of very costly and expensive investigations. This also makes it hard to make good corruption policies, since they are troubled by expensive investigations. 

This is the part where this paper wants to help out: detecting corruption in a low cost data driven way. The investigation/development is started by looking at ground-truth measures from professional government auditors. 

With ML, corruption is predicted from the features of public accounts. Accuracy of 72% is obtained in the best model specification (using gradient boosted trees). The algo ranks municipalities by the probability of corruption, which reproduces the distribution of corruption on the held-out data. 

In a second analysis, the authors determine the causal effect of auditing on curruption (event study analysis). The result from this is that audits reduce corruption over subsequent years (about 2.7% drop in probability).

In the last part of the paper, the authors look at the potetnial of making audit policy based on the predictions of corruption risk. Also measures of algorithmic fairness are considered here, since it might be socially undesirable to have heterogeneous audit rates between different political parties. 

## 

Data sets on curruption are joined with municipal level budget factors and demographics (municipality data). 

Feature importance metrics are used to interpret the predictions and see what components are important for the predictions of corruption. About half of the predictors are ignored (noisy or very correlated with the target). 

WHat is cool, is that the important features are then searched for in published audit reports (do the experts recognize similar features when they screen for corruption?). The corrleation between these is then investigated by plotting a lienar regression plot. There indeed seems to be a positive association. 

Then: an analysis of a diff-in-diff approach to investigate the influence of some results in the corruption literature is done. E.g. a diff-in-diff approach to see the effect of revenue windfalls on corruption is done. 

In general, there are some analyses done using the predicted curruption. This is interesting, but hopefully they also give some limitations of this approach. 

Next to extending datasets, the predictions can also be used to guide policy makers. One extension here, for example, is to target audits at the 203 municipalities that have the highest corruption probability, instead of doing random audits. 

## QUstions/Remarks:

- What about measures of corruption that have not been discovered in the ground-truth data. Is the model able to identify these corruption cases in the hold-out data? (i.e. will the algorithm be able to detect forms of corruption that have never been detected before?)
- Mean imputation of missing values: maybe there is also some endogeneity in the missing data. hence, it could be cool to also include a dummy: is there missing data? Or is it too sporadic?. A: this has been done, and results did not significantly change!
- The datasets are joined between the two corruption metrics. Is that a sensible thing to do?'
- What about false negatives in corruption detection?

- It would be cool to discuss when the classification method is actually good enough to use it for some social science research. Can we trust the predictions enough such that we can base policy on them? 
- From reinforcement learning, we know the xploration, exploitation tradeoff. Maybe we always want to add some random ones to find new forms of corruption, that our model can then incorparate in the model training.
- In this targeting way, undiscovered corruption schemes might never be discovered. 