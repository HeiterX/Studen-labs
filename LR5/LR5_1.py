import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.colors import LinearSegmentedColormap

# Load the dataset
df = pd.read_csv('diamonds.csv')

# Define color grades in order
color_grades = ['D', 'E', 'F', 'G', 'H', 'I', 'J']

# Create a custom colormap from purple to yellow
cmap = LinearSegmentedColormap.from_list('custom', ['purple', 'blue', 'cyan', 'green', 'lime', 'yellow', 'gold'], N=len(color_grades))

# Create the polar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(color_grades)
theta_step = 2 * np.pi / num_categories
scale_factor = theta_step / 2  # Scale for violin width

for i, color in enumerate(color_grades):
    data = df[df['color'] == color]['price'].values
    if len(data) < 2: continue  # Skip if insufficient data
    
    # Compute KDE
    kde = gaussian_kde(data)
    r_min, r_max = data.min(), data.max()
    r = np.linspace(r_min, r_max, 200)
    density = kde(r)
    
    # Scale density for width
    max_density = density.max()
    if max_density == 0: continue
    density_scaled = (density / max_density) * scale_factor
    
    # Base theta
    base_theta = i * theta_step
    
    # Theta for left and right sides of violin
    theta_left = base_theta - density_scaled
    theta_right = base_theta + density_scaled
    
    # Fill the violin shape
    ax.fill(np.append(theta_left, theta_right[::-1]), np.append(r, r[::-1]), alpha=0.7, label=color, color=cmap(i / (len(color_grades) - 1)))

# Set theta ticks and labels
ax.set_thetagrids(np.degrees(np.arange(num_categories) * theta_step), labels=color_grades)
ax.set_theta_zero_location('N')  # Start at top
ax.set_theta_direction(-1)  # Clockwise
ax.set_rlabel_position(90)  # Position radial labels
ax.set_title('График №9')
ax.set_ylabel('price')  # Radial label
plt.legend(title='Color', bbox_to_anchor=(1.1, 1.1))
plt.show()