# modules
import mne
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from surfer import Brain

import os
os.environ["QT_MAC_WANTS_LAYER"] = "1"

# paths
base_dir = '/Users/derekrosenzweig/Documents/GitHub/lab-scripts'
elec_info = f'{base_dir}/electrodes/concatenated/master-electrodes.tsv'
subjects_dir = '/Users/lauragwilliams/Documents/projects/iEEG/summer_2024/subjects_dir'
subject_id = 'fsaverage'

# load elecs
elecs = pd.read_csv(elec_info, sep='\t')

# load mni coordinates
coords = elecs[['x', 'y', 'z']].values

# plot 3d brain
brain = Brain(subject_id, 'both', 'pial', subjects_dir=subjects_dir, cortex='low_contrast', alpha=0.3, background='white')


# otherwise need to plot the elecs of the lh and rh separately
lh_idx = coords[:, 0] < 0
rh_idx = coords[:, 0] > 0

brain.add_foci(coords[lh_idx, :], color="k", hemi='lh', scale_factor=0.2, alpha=0.8)
brain.add_foci(coords[rh_idx, :], color="k", hemi='rh', scale_factor=0.2, alpha=0.8)