import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path, output_path):
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Ensure the dataset has the required columns
    if not {'ID_A', 'ID_B', 'Distance'}.issubset(df.columns):
        raise ValueError("The dataset must contain 'ID_A', 'ID_B', and 'Distance' columns.")

    # Create a unique list of IDs
    unique_ids = pd.concat([df['ID_A'], df['ID_B']]).unique()
    
    # Initialize a distance matrix with NaN values
    distance_matrix = pd.DataFrame(np.nan, index=unique_ids, columns=unique_ids)

    # Populate the distance matrix with known distances
    for _, row in df.iterrows():
        distance_matrix.at[row['ID_A'], row['ID_B']] = row['Distance']
        distance_matrix.at[row['ID_B'], row['ID_A']] = row['Distance']  # Symmetric
    
    # Fill diagonal values with 0 (distance from an ID to itself)
    np.fill_diagonal(distance_matrix.values, 0)

    # Calculate cumulative distances for known routes
    for k in unique_ids:
        for i in unique_ids:
            for j in unique_ids:
                if pd.notna(distance_matrix.at[i, k]) and pd.notna(distance_matrix.at[k, j]):
                    new_distance = distance_matrix.at[i, k] + distance_matrix.at[k, j]
                    if pd.isna(distance_matrix.at[i, j]) or new_distance < distance_matrix.at[i, j]:
                        distance_matrix.at[i, j] = new_distance

    # Save the distance matrix to a CSV file
    distance_matrix.to_csv(output_path)

    return distance_matrix

# Usage example
distance_matrix = calculate_distance_matrix('MapUp-DA-Assessment-2024\datasets\dataset-2.csv', 'MapUp-DA-Assessment-2024\submissions\excel_assessment\output_matrix.csv')
print(distance_matrix)