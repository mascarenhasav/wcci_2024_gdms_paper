Experiment B2 - Controlled Diversity Benchmark (Supplementary Material)
===================================================

Description
-----------

To gain a deeper understanding, let's delve into how these metrics behave in both uni-modal and multi-modal problems. To facilitate this exploration, an appropriate benchmark is essential. Common benchmarks in Evolutionary Algorithms (EAs) often lack a controlled variable for population diversity. Consequently, information about the actual diversity status of a population is scarce, except through the comparison of Genotypic Diversity Metrics (GDMs). This creates an ill-defined problem, as different GDMs may yield varied estimations, complicating the determination of the most accurate representation of authentic diversity.

The benchmark's definition is also crucial. Genotypic diversity focuses solely on the distribution of individuals across a landscape, irrespective of their respective fitness functions. Thus, creating an environment for GDMs necessitates transitioning the population from a fully dispersed state to a completely aggregated one. Additionally, the number of optimal solutions across the landscape is expected to impact GDMs. A well-defined benchmark should simulate the influence of modalities. In this context, we adopt the benchmark proposed by `Corriveau et al <https://dl.acm.org/doi/10.1109/TEVC.2011.2170075>`_.

The benchmark's concept involves creating an environment where the diversity of individuals in the population can be known and controlled, ensuring a clear evaluation of diversity metrics. In each generation, the landscape linearly decreases, and a new population is randomly created.

To assess the performance of GDMs on a uni-modal problem. The landscape progressively reduces by 1\% of the initial size in each dimension in every generation, and the population becomes less spread until converging in generation 100.

To test the performance of the GMDs on a multi-modal problem, making the landscape 1\% of the initial size smaller in each dimension in each generation and randomly recreating the population less spread until the convergence on the generation 100. But in this case, instead of only one optimum point, we have 5 and the population was divided in 5, where each of these subpopulations is in charge to converge to a different optimum point.

Finally in order to evaluate the metric’s consistency under different numbers of optima points and dimensions we are going now to consider only the value of the last generation. As a controlled system, we know that this is the generation where the populations have converged.

Paper's dataset
---------------

The dataset used in the paper is at `paper dataset <>`_ folder.

How to run
-----------

To run the benchmark with different configurations the parameters can be set in the file $config.ini$ with any text editor, for example with the command::

  nano parameters.ini

Then to run the benchmark we just need to excute the script $benchmark.py$ with the command::

  ./benchmark.py

Results
-------

Once you run the script and the generated data is in the $Experiments/YYYY-MM-DD/HH-mm$ folder.
