import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('path_to_your_data.csv')
numerical_data = data[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_ghgs_ch4', 'mean_ghgs_n2o', 'mean_watuse', 'mean_acid']]

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Plot the correlation matrix
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Environmental Impacts', fontsize=16)
plt.savefig('path_to_save_image.png')
plt.show()
