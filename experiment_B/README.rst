Experiment B - Centroids
===================================================

Description
-----------

Elements that contribute to the promotion of increased diversity include the number of niches within a population and the variability of individuals. Understanding how each metric evaluates different scenarios allows for the adoption of metrics tailored to the diversity needs of users. An experiment is conducted using a easily creatable 2D landscape datasets to visualize the impact of the number of niches and the variability of individuals on metric values.

The dataset utilized in the experiment is created by providing several centroids and generating individuals uniformly within squares centered around these centroids. The number of centroids ranges from 1 to 13, with 13 possible configurations, distributed on a 2D landscape in the range of $[0, 1]$. 
The positions of the centroids are determined by selecting 13 points from an infinite set of points within the $[0, 1]^2$. When multiple centroids are used, they are utilized in the order in which they are selected. The side length of the square takes 13 equally spaced values ranging from 0.002 to 0.250. The choice of 0.250 ensures that even with the maximum number of centroids, the squares do not overlap. From the above, a total of 169 patterns of data will be generated. The population size is fixed at 260 individuals per pattern, and individuals are distributed within each square in as equal numbers as possible.

In this experiment, 169 patterns of data will be created 50 times. The average metric value for each pattern will be calculated, and contour plots will be generated based on these average values. The metric values are normalized by the maximum value among the 169 patterns. The behavior sought for each metric in this dataset is an increase in diversity as the number of centroids grows for any given side length. Additionally, an increase in diversity is expected as the side length of the square becomes larger for any given number of centroids.

Paper's dataset
---------------

The dataset used in the paper is at `paper dataset <https://github.com/mascarenhasav/wcci_2024_gdms/tree/main/experiment_B_2/paper_dataset>`_ folder.

How to run
-----------

A very simple explanation in how to run the experiments

Results
-------

Once you run the script and the generated data is in the $XXXX$ folder.
