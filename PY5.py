from PY2 import confirmed_cases, covid_deaths
import matplotlib.pyplot as plt
# Create bar chart
plt.bar(confirmed_cases, covid_deaths)
# Customize chart appearance
plt.xlabel('Confirmed_cases')  # Set x-axis label
plt.ylabel('covid_deaths')  # Set y-axis label
plt.title('Bar Chart ')  # Set chart title

# Show chart
plt.show()
