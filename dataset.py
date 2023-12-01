import pandas as pd
import random

# Generate synthetic data for car sales
num_records = 100  # Number of car sales records

# Sample data for model, condition
models = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Tesla']
conditions = ['Excellent', 'Good', 'Fair']

# Generate random data for the dataset
data = {
    'Model': [random.choice(models) for _ in range(num_records)],
    'Price': [random.randint(15000, 50000) for _ in range(num_records)],
    'Mileage': [random.randint(10000, 80000) for _ in range(num_records)],
    'Age': [random.randint(1, 10) for _ in range(num_records)],
    'Condition': [random.choice(conditions) for _ in range(num_records)]
}

# Create a DataFrame
car_sales_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
car_sales_df.to_csv('car_sales_dataset.csv', index=False)
