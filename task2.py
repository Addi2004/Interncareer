import pandas as pd
import matplotlib.pyplot as plt
from apscheduler.schedulers.blocking import BlockingScheduler
def read_data(file_path):
    # Read the dataset into a Pandas DataFrame
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty. Please provide a valid dataset.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the dataset. Please ensure it's in a proper format.")
        return None

def calculate_summary_statistics(data):
    # Convert 'Price' column to numeric
    data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
    
    # Drop rows with missing values in the 'Price' column
    data = data.dropna(subset=['Price'])
    
    # Calculate summary statistics
    summary_stats = {
        'Mean': data['Price'].mean(),
        'Median': data['Price'].median(),
        'Standard Deviation': data['Price'].std()
    }
    return summary_stats

def filter_data(data, column, criteria):
    # Filter data based on specific criteria
    filtered_data = data[data[column] == criteria]
    return filtered_data

def generate_histogram(data, column):
    # Generate a histogram for a specific column
    plt.hist(data[column], bins=20)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title('Histogram of ' + column)
    plt.show()

def save_processed_data(data, output_file):
    # Save processed data to a new file (e.g., CSV)
    data.to_csv(output_file, index=False)

# Example usage:
file_path = '/Users/rishabpaul/Desktop/interncareer/task2/car_sales_dataset.csv'
output_file_path = '/Users/rishabpaul/Desktop/interncareer/task2'

# Read data
dataset = read_data(file_path)

if dataset is not None:
    # Calculate summary statistics
    stats = calculate_summary_statistics(dataset)
    print("Summary Statistics:")
    for key, value in stats.items():
        print(f"{key}: \n{value}\n")

    # Filter data (example: filter based on 'Condition' being 'Good')
    filtered = filter_data(dataset, 'Condition', 'Good')
    print("Filtered Data:")
    print(filtered.head())

    # Generate histogram (example: 'Price' distribution)
    generate_histogram(dataset, 'Price')

    # Save processed data
    save_processed_data(filtered, output_file_path)


# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the scraping function to run every hour (you can change the interval as needed)
scheduler.add_job(read_data, 'interval', hours=1)

try:
    # Start the scheduler
    scheduler.start()
except KeyboardInterrupt:
    # If you want to stop the scheduler manually (Ctrl+C)
    pass
