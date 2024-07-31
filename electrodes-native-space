# Tutorial: Plotting Intracranial Electrodes in Native Space Using FreeView

### Step 1: Prepare your data

1. T1-weighted MRI image in native space (run `recon-all`)

2. A text file containing electrode coordinates (ie. sub-01_electrodes.txt)

From BIDS formatted tsv files, convert tsv files to txt files

The sub-01_electrodes.txt file should be formatted with one electrode per line, containing the X, Y, and Z coordinates separated by spaces or tabs.

-29.5 10.3 24.1
-31.2 12.1 26.8
...

Note: no columns added to the txt file

### Step 2: Load the corresponding MRI image in FreeView

```bash
freeview -v /path/to/sub-01_ses-01_T1.nii
```

### Step 3: Add Electrode Coordinates

To add the electrode coordinates, use the following steps within FreeView:

Open the Control Panel:
Click on the "Tools" menu and select "Point Set."

Load the Electrode Coordinates:
In the "Point Set" panel, click the "Load Point Set" button. Select the electrodes.txt file containing your electrode coordinates.

Display Electrode Locations:
Once loaded, the electrodes should appear as points in the MRI image. You can adjust the display settings (e.g., point size, color) using the "Point Set" panel.

### Step 4: Save the Point Set

To save the electrode point set for future use, click the "Save Point Set" button in the "Point Set" panel and specify the desired file format and location.

### Step 5: Customize the Point size and Color

Adjust Point Size and Color:
In the "Point Set" panel, you can adjust the size and color of the points representing the electrodes.

Overlay Other Data:
If you have additional data (e.g., functional maps, segmentation labels), you can overlay them on the MRI image by clicking the "Add Volume" button in the main FreeView window.

Save a Screenshot:
To save a screenshot of the current view, click the "File" menu and select "Save Screenshot." Choose the desired file format and location.

### Step 6: Verify Electrode Locations

Use the segmentations as a way to check valid electrode locations (especially important when plotting in fsaverage space)

It's essential to verify that the electrode locations are accurate. Cross-check the electrode coordinates with known anatomical landmarks or other reference images.
