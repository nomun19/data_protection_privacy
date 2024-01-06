# ℓ-Diversity: Privacy Beyond k-Anonymity

## What is k-Anonymization?
K-anonymization is a privacy-preserving data anonymization technique used to 
protect the identities of individuals in a dataset.

The primary goal of k-anonymization is to ensure that each record 
in the dataset is indistinguishable from at least k-1 other records 
with respect to a set of quasi-identifiers (attributes that can potentially 
identify individuals). 

- Quasi-identifiers: Attributes in the dataset that, when combined, could potentially 
identify individuals. One example of a quasi-identifier is a primary key like social security number.


- K-anonymous groups: Sets of records in the dataset where each record is 
indistinguishable from at least k-1 other records with respect to quasi-identifiers.

- Generalization: The process of replacing specific values with more generalized 
versions to achieve anonymity. 

- Suppression: The process of removing or redacting certain values to achieve 
anonymity. 

- Anonymized Dataset: The result of applying k-anonymization to the original 
dataset, ensuring that each record belongs to a k-anonymous group.

## Attacks On k-Anonymity
 
- Homogeneity Attack: In a k-anonymous dataset, all records within a group (or cluster) 
look the same with respect to quasi-identifiers. This uniformity can be exploited by 
an attacker to make educated guesses about sensitive attributes.
- Background Knowledge Attack: An adversary with external knowledge or auxiliary information 
may use that knowledge to re-identify individuals within a k-anonymous group.

### Bayes-Optimal Privacy
- Prior Distribution: The adversary's initial beliefs or knowledge about the distribution 
of individuals in the dataset before observing any specific output.
- Privacy principle 
Positive disclosure occurs when a published table allows an adversary to accurately 
identify the value of a sensitive attribute with high probability, while negative 
disclosure happens when the adversary can eliminate possible values of the sensitive 
attribute with high probability.
- Uninformative Principle, states that the published table should provide the adversary 
with little additional information compared to their background knowledge.

### Limitations of the Bayes-Optimal Privacy
- Insufficient Knowledge: The data publisher is unlikely to know the full 
distribution f of sensitive and nonsensitive attributes over the general 
population from which T is a sample
- THe adversary's Knowledge is Unknown: It's also unlikely that the adversary has knowledge of the complete
joint distribution between the non-sensitive and sensitive attributes.
However, the data publisher deos not know how much the adversary knows.
- Instance-Level Knowledge: The theoretical definition does not protect against knowledge that cannot be modeled probabilistically.
- Multiple Adversaries: There will be multiple adversaries with different levels of knowledge, 
each of which is consistent with the full joint distributions.




