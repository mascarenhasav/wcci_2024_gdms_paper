<<<<<<< HEAD
Experiment B2 - Controlled Diversity Benchmark (Supplementary Material)
=======
Experiment B - Centroids
>>>>>>> 7d4ad445cdd3a6639ca13cb6c70cf37d0ba0904b
===================================================

Description
-----------

<<<<<<< HEAD
To gain a deeper understanding, let's delve into how these metrics behave in both uni-modal and multi-modal problems. To facilitate this exploration, an appropriate benchmark is essential. Common benchmarks in Evolutionary Algorithms (EAs) often lack a controlled variable for population diversity. Consequently, information about the actual diversity status of a population is scarce, except through the comparison of Genotypic Diversity Metrics (GDMs). This creates an ill-defined problem, as different GDMs may yield varied estimations, complicating the determination of the most accurate representation of authentic diversity.

The benchmark's definition is also crucial. Genotypic diversity focuses solely on the distribution of individuals across a landscape, irrespective of their respective fitness functions. Thus, creating an environment for GDMs necessitates transitioning the population from a fully dispersed state to a completely aggregated one. Additionally, the number of optimal solutions across the landscape is expected to impact GDMs. A well-defined benchmark should simulate the influence of modalities. In this context, we adopt the benchmark proposed by `Corriveau et al <https://dl.acm.org/doi/10.1109/TEVC.2011.2170075>`_.

The benchmark's concept involves creating an environment where the diversity of individuals in the population can be known and controlled, ensuring a clear evaluation of diversity metrics. In each generation, the landscape linearly decreases, and a new population is randomly created.

To assess the performance of GDMs on a uni-modal problem. The landscape progressively reduces by 1\% of the initial size in each dimension in every generation, and the population becomes less spread until converging in generation 100.

To test the performance of the GMDs on a multi-modal problem, making the landscape 1\% of the initial size smaller in each dimension in each generation and randomly recreating the population less spread until the convergence on the generation 100. But in this case, instead of only one optimum point, we have 5 and the population was divided in 5, where each of these subpopulations is in charge to converge to a different optimum point.

Finally in order to evaluate the metric’s consistency under different numbers of optima points and dimensions we are going now to consider only the value of the last generation. As a controlled system, we know that this is the generation where the populations have converged.
=======
Elements that contribute to the promotion of increased diversity include the number of niches within a population and the variability of individuals. Understanding how each metric evaluates different scenarios allows for the adoption of metrics tailored to the diversity needs of users. An experiment is conducted using a easily creatable 2D landscape datasets to visualize the impact of the number of niches and the variability of individuals on metric values.

The dataset utilized in the experiment is created by providing several centroids and generating individuals uniformly within squares centered around these centroids. The number of centroids ranges from 1 to 13, with 13 possible configurations, distributed on a 2D landscape in the range of $[0, 1]$. 
The positions of the centroids are determined by selecting 13 points from an infinite set of points within the $[0, 1]^2$. When multiple centroids are used, they are utilized in the order in which they are selected. The side length of the square takes 13 equally spaced values ranging from 0.002 to 0.250. The choice of 0.250 ensures that even with the maximum number of centroids, the squares do not overlap. From the above, a total of 169 patterns of data will be generated. The population size is fixed at 260 individuals per pattern, and individuals are distributed within each square in as equal numbers as possible.

In this experiment, 169 patterns of data will be created 50 times. The average metric value for each pattern will be calculated, and contour plots will be generated based on these average values. The metric values are normalized by the maximum value among the 169 patterns. The behavior sought for each metric in this dataset is an increase in diversity as the number of centroids grows for any given side length. Additionally, an increase in diversity is expected as the side length of the square becomes larger for any given number of centroids.
>>>>>>> 7d4ad445cdd3a6639ca13cb6c70cf37d0ba0904b

Paper's dataset
---------------

<<<<<<< HEAD
The dataset used in the paper is at `paper dataset <>`_ folder.
=======
The dataset used in the paper is at `paper dataset <https://github.com/mascarenhasav/wcci_2024_gdms/tree/main/experiment_B_2/paper_dataset>`_ folder.
>>>>>>> 7d4ad445cdd3a6639ca13cb6c70cf37d0ba0904b

How to run
-----------

<<<<<<< HEAD
To run the benchmark with different configurations the parameters can be set in the file $config.ini$ with any text editor, for example with the command::

  nano parameters.ini

Then to run the benchmark we just need to excute the script $benchmark.py$ with the command::

  ./benchmark.py
=======
A very simple explanation in how to run the experiments
>>>>>>> 7d4ad445cdd3a6639ca13cb6c70cf37d0ba0904b

Results
-------

<<<<<<< HEAD
Once you run the script and the generated data is in the $Experiments/YYYY-MM-DD/HH-mm$ folder.
=======
Once you run the script and the generated data is in the $XXXX$ folder.
>>>>>>> 7d4ad445cdd3a6639ca13cb6c70cf37d0ba0904b
