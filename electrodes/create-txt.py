import os
import pandas as pd

# Loop through tsv files
val_dir = '/Users/derekrosenzweig/Documents/GitHub/lab-scripts/electrodes/individual/valid'

native_dir = '/Users/derekrosenzweig/Documents/GitHub/lab-scripts/electrodes/txt/native'
mni_dir = '/Users/derekrosenzweig/Documents/GitHub/lab-scripts/electrodes/txt/native'


# Convert CSV Files to TXT Files
for analysis_type in files_and_titles:
    # Construct the input file path
    input_file_path = os.path.join(weights_path, f'{freq}_CCA_weights_{analysis_type}.csv')

    # Check if the file exists
    if not os.path.exists(input_file_path):
        print(f"File does not exist: {input_file_path}")
        continue

    # Load electrode data from CSV
    try:
        electrode_data = pd.read_csv(input_file_path)

        print(f"Loaded {input_file_path} with shape: {electrode_data.shape}")
        print(electrode_data.head())

        # Split electrode data based on hemisphere
        lh_data = electrode_data[electrode_data['LvsR'] == 'L']
        rh_data = electrode_data[electrode_data['LvsR'] == 'R']

        # Prepare the output file paths
        lh_file = os.path.join(output_dir, f'top_{n}_electrodes_{analysis_type}_{freq}_lh.txt')
        rh_file = os.path.join(output_dir, f'top_{n}_electrodes_{analysis_type}_{freq}_rh.txt')

        # Save split data to separate files without headers
        lh_data[['fsaverageINF_coord_1', 'fsaverageINF_coord_2', 'fsaverageINF_coord_3', 'LvsR', 'weight', 'WMvsGM']].to_csv(lh_file, sep=' ', index=False, header=False)
        rh_data[['fsaverageINF_coord_1', 'fsaverageINF_coord_2', 'fsaverageINF_coord_3', 'LvsR', 'weight', 'WMvsGM']].to_csv(rh_file, sep=' ', index=False, header=False)

        print(f"Saved {lh_file} and {rh_file}")

    except Exception as e:
        print(f"Error processing {input_file_path}: {e}")

print("Finished processing all files.")



# Script for txt of master electrodes for anatomical locations on fsaverage

