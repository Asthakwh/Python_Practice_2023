import pandas as pd

# Sample data
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 40000, 55000, 45000, 60000]
}

df = pd.DataFrame(data)

# Group by Department and find average salary
grouped = df.groupby('Department')['Salary'].mean()

print(grouped)
