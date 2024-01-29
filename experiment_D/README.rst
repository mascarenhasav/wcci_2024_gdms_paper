Experiment A - Assessment of theoretical properties
===================================================

Description
-----------

We conducted a mathematical assessment of the metrics' performance on a simple dataset with a fixed population diversity. This evaluation was based on the seven cases proposed by `Corriveau et al <https://api.semanticscholar.org/CorpusID:2995563>`_. In these cases, with the exception of cases 6 and 7, all solutions converged perfectly to predefined optimal points. This convergence allows us to observe diversity without being influenced by variations in values due to data variability.

All these cases are situated on a 2D landscape within the range of $[-1, 1]$, with a constant population size of 100. In Case 1, a single optimal point exists at the center of the landscape, and the population is concentrated at this central point. In Case 2, the optimal point lies between the center and the corner of the landscape, and the population is uniformly distributed. Case 3 shares the same optimal point as Case 2 but exhibits non-uniform population distribution. Case 4 features the optimal point at the corner of the landscape, with an even distribution of the population. Similarly, Case 5 has the same optimal point as Case 4 but also displays non-uniform population distribution. In both Case 3 and Case 5, 70\% of the individuals are concentrated at one optimal point, while the remaining 30\% are evenly distributed among the other optimal points. In Case 6, individuals are evenly distributed along the diagonal of the landscape. Lastly, in Case 7, individuals are uniformly distributed at regular intervals across the landscape. Figure \ref{fig:flozencase} illustrates the population distributions.

In these frozen cases, the diversity ranking must be $case1 < case2 = case3 < case4 = case5 < case6 < case7$ in order to satisfy the three diversity requirements proposed by Corriveau.

How to run
-----------

A very simple explanation in how to run the experiments
