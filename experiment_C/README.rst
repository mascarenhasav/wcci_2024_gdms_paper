Experiment C - Centroids
===================================================

Description
-----------

A proposed benchmark based on the previous experiment is using an easily creatable 2D landscape dataset visualizes the impact of the number of niches and individual variability on metric values.

The dataset used in the experiment is created by establishing several centroids and uniformly generating individuals within squares centered around these centroids. The number of centroids ranges from 1 to 13, with 13 possible configurations, distributed on a 2D landscape within the $[0, 1]$ range. The positions of the centroids are determined by selecting 13 points from a set of points within the $[0, 1]^2$. When multiple centroids are used, they are utilized in the order of their selection. The square's side length has 13 equally spaced values, ranging from 0.002 to 0.250, ensuring no overlap even with the maximum number of centroids. Consequently, 169 different landscape configurations will be generated. The population size is fixed at 260 (NP = 260) individuals per pattern, distributed as equally as possible within each square.

In this experiment, the average of 169 patterns generated over 50 runs will be utilized, and contour plots based on these averages will be created. The metric values are normalized using the maximum value among all patterns. The expected behavior for each metric in this dataset is an increase in diversity corresponding to the growth in the number of centroids for any given side length. Furthermore, a rise in diversity is anticipated as the square's side length increases, regardless of the centroid count. Ideally, the contour plots should exhibit higher elevations towards the top-right, indicating this relationship.

Paper's dataset
---------------

The dataset used in the paper is at `paper dataset <https://github.com/mascarenhasav/wcci_2024_gdms/tree/main/experiment_B_2/paper_dataset>`_ folder.

How to run
-----------

A very simple explanation in how to run the experiments

Results
-------

Once you run the script and the generated data is in the $XXXX$ folder.


