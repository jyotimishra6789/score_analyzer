import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Study Hours': [2, 3, 1, 4, 0.5],
    'Scores': [85, 90, 70, 95, 50]
}
df = pd.DataFrame(data)

# Step 2: Analyze the dataset
average_score = df['Scores'].mean()
print(f"The average score is: {average_score}")

# Check if more study hours correlate with higher scores
correlation = df['Study Hours'].corr(df['Scores'])
print(f"Correlation between study hours and scores: {correlation}")

# Step 3: Visualize the data
plt.scatter(df['Study Hours'], df['Scores'], color='blue')
plt.title('Study Hours vs Scores')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.grid(True)
plt.show()
