import json
import random

# List of input files
input_files = [f'dataset_output_{i}.json' for i in range(1, 7)]
output_file = 'merged_dataset_HarryPotter.json'
train_file = 'train_dataset_HarryPotter.json'
train_size = 30000

# Load and merge all JSON entries
merged_data = []
for file in input_files:
    with open(file, 'r') as f:
        data = json.load(f)
        merged_data.extend(data)

# Save the merged data and training set to files
with open(output_file, 'w') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)
print(f'Merged dataset saved to {output_file}')

# Shuffle the merged data
random.shuffle(merged_data)

# Split the data into training set
train_data = merged_data[:train_size]

with open(train_file, 'w') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

print(f'Training dataset saved to {train_file}')

# Split the remaining data into test set
test_data = merged_data[train_size:]

# Save the test set to a file
test_file = 'test_dataset_HarryPotter.json'
with open(test_file, 'w') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=4)

print(f'Test dataset saved to {test_file}')