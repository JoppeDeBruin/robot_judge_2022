## Paper discussion "In-group bias in the Indian judiciary"

The paper examines bias in India's courts, asking whether judges deliver more favroable treatment to defendants who match their identities.

This form of in-group bias has already been established in other contexts in India: loan officers, election workers, school teachers.

First challenge is to provide some indentity characteristics (for both judges and defendants), as they are usually not readily available in the data set. These are constructed using a NN classifier on gender and religion. Data from other datasets is used and the model achieves over 97% accuracy out of sample.

Castes are matched using matches of last name! Imperfect measure, but easy to implement.

Research question: do judges threat defendants differently when they share the same gender, religion or caste. ALso speed of decisions is considered.

Judge identity is as good as rnadom due to arbitrary rules by which cases are assigned. Preferred specificaition is court-year-month and charge FIXED EFFECTS! This compares outcomes of two defendants with the same identity, charged under the same criminal section in the same court and in the same month, but who are assigned to judges with different identities.

In all dimensions, a robust null estimate of the bias is found.

However, the paper takes another step and also looks at cases wehre the defendant and the victim haver different identities (and the judge shares the identity with the victim). Second: gender bias in crimes against women are considered. Also in-group bias on the basis of religion is activiated during the month of ramadan.

Probability of acquittal is increased during the Ramadan!

There seems to be some relationship between the salience of identity and the found effects/bias. Most similar studies focus on the US and Israel, where identities may be exceptionally salient. 

There seems to be a publication bias towards non-null effects. This is also tested in the paper.

There are two main contributions of this paper
1. First (contrary to most literature), it presnts a notable absence of judicial in-group bias in an important low-income country with substantial indentity cleavages
2. Second: findings of differential bias effects in certain cases helps shed light o context where bias may be more ore less liekly to occur.


**In this paper, the case assignment to judges is of pivotal importance!! THe study hinges on the exogenous assignment of judges to cases. Hence we assume there is no confounding between case assignment and outcome!!!!**

The assignment protocol is organized as follows:
- First: crime is reported at police station
- Case is assigned to a judge sitting in the courthouse within the territorial jurisdiction of a specific courthouse
- If there are multiple judges, a rule-based process determines assignment
- Judges typically spend tow to three years in a given court, during which they rotate through several courtrooms. Murder cases go to the same courtroom, larceny might go to a different one.

- Less than 0.5% of criminal cases pending in india are disposed through plea bargaining, minimizing the effect of endogeneity of ending up in court

### DATA:
- First filtering of the cases cuts about 70% of the data.

- Data on judges include name, position/designation, start and end date of appointment to each court
- Mathcing judge data with case data loses about 17% of the initial data.
- From that subset, all bail-decisions are removed. 
- Also the cases where the identity cannot be identified are dropped. Also cases are dropped where there is only one judge in a certain time period.


The data does not contain demographic data on the judges and defendants. So a machine classifier is fitted to assign identity. For that, Delhi voter rolls are used.
The classifier is trained on the texts of names. A LSTM network (based on recurrent NNs) is used to assign the gender as well as religion of people. The LSTM has some advantages over fuzzy matching.

Names that are not confidently classified are removed. 

Note that also the 100 annotated names are very small sample. They are stratified according to region, which makes effective sample size only smaller!!!!

The case outcomes are modeled using a binary variable. Acquittal vs not. But there are other dimensions to bias (e.g. if punished: how badly?)

The randomization of the judge assignment to the case, basically takes care of all potential confounding. Hence, we can look at causal effects in a safe way.

## Results

About half of the time, the judge changes before the final decision is reached. However, that does not matter too much, since the results seem robust for that.

Based on the general analysis, it seems that judges do not provide substantively better outcomes for own-gender and own-religion defendants, on average. THe paper then continues to cases were identity is more salient. 

This is done by including a dummy variable that is equal to one when the salience condition is satisfied. This dummy is also interacted with all covariates in the regression. Also this inclusion yields null effects (for the gender mismatch in cases where the judge shares the gender of the defendant). The same holds for the case where the crimes are crimes against women.

The (arguably) most important social cleavage in India is caste. However, there is not sufficient information available to make a comparison based on caste. So as a proxy, last name is taken. Note that this is a suboptimal and noisy proxy for caste, especially since names are more numerous than castes. Hence people with different names might be part of the same caste.

Also in this context, there is a null bias. However, the unweighted analysis, gives more influence to very common names, which might be less culturally informative of caste (and potential other biases). Hence a weighted version is also performed. The regressions in this specification describe variation in bias across groups, rather than individuals!!

The results here, suggest that there is caste-based in-group bias diven by groups with less common names. This is further substantiated with an "rare last name" dummy variable. 



### Questions/Remarks:

- Does the Delhi voter rolls have bias (i.e. do they only contain names and demographics from people in the Delhi region?)

- Dropping non-confident names: does that not induce bias? Is there a reason that certain names are incomplete or non confident? then these might be a confounder.

- There is another dimension to bias: maybe people are convicted, but the punishment is different!! Maybe that is why there is no bias found?

- Is there a control for severity of the crime? This might be a confounder (it is more likely that a male murders someone than a female). Or is this a mediator? Gender directly contributes to severity of the crime and that influences the decision. SO maybe should not control for it.

- It is stated that "conditional on court-time and charge fixed effects", judge assignment is practically random (remember the different charges going to specific courts). However, in the causal diagram, would charge severity not be a mediator? Hence we condition on a mediator. How to deal with this? It makes sense that given case, the judge assignment is random. Is conditioning on this, then different from controlling for observables?

- WHy fixed effects and no random effects? Don't you think there is an inherent stochastic nature to judge decisions?

- In the first regression specification, you include religion controls. Are they confounders? Does religions affect the probability of being male and of the outcome?