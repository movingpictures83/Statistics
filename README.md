# Statistics
# Language: Python
# Input: CSV 
# Output: none (screen only)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin to output statistics (mean, standard deviation, etc.) on the most abundant taxa in a sample.

The plugin takes as input a CSV file with samples as rows and columns as abundances.

It will then output all statistics to the screen.  This plugin generally works best with normalized abundances, as its "threshold" for the most abundant taxa is 5%.
