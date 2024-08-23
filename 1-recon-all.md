# Tutorial: Running `recon-all` on a T1 .nii File

Basic Terms for FS 
https://andysbrainbook.readthedocs.io/en/latest/FreeSurfer/FS_ShortCourse/FS_01_BasicTerms.html

Video for recon- all
https://www.youtube.com/watch?v=gkjvKMjH7iM

## Step 1: Install FreeSurfer
Ensure FreeSurfer is installed on your system. You can download and install it from the [FreeSurfer website](https://surfer.nmr.mgh.harvard.edu/fswiki/rel7downloads). Follow the installation instructions specific to your operating system.

Tutorial for install
https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall?action=AttachFile&do=get&target=installFS_demo.mp4

## Step 2: Set Up FreeSurfer Environment
Set up the FreeSurfer environment variables by adding the following lines to your `.bashrc` or `.bash_profile` file:

```bash
export FREESURFER_HOME=/Applications/freesurfer/7.4.1
source $FREESURFER_HOME/SetUpFreeSurfer.sh
````

### Step 2a: Reload shell configuration 

```bash
source ~/.bashrc
```

## Step 3: Set the subjects directory 

Example of a local directory here: 

```bash
export SUBJECTS_DIR=/Users/derekrosenzweig/PycharmProjects/electrodes/freesurfer_subjects
```

### Step 3a: Verify that 'SUBJECTS_DIR' is set correctly 

Navigate to the directory where you want the FreeSurfer outputs to be saved: 

```bash
echo $SUBJECTS_DIR
```

### Step 4: Run `recon-all`

Run the `recon-all` command with the full path to the T1 .nii file: 

```bash
recon-all -s sub-10 -i /Users/derekrosenzweig/PycharmProjects/electrodes/freesurfer_subjects/sub-10_ses-01_T1.nii -all
```
Alternatively, can run `recon-all` in parallel through homebrew
https://www.youtube.com/watch?v=XHN2tm3tNaw

Consider this as an option depending on the size of your dataset 

### Step 5: Verify the Output 

After `recon-all` completes (expect this to take several hours), verify the output by checking on an individual subject's directory in your FreeSurfer subjects directory.

```bash
ls $SUBJECTS_DIR/sub-09
```
Within the folder, you should see several subdirectories and files, including `mri`, `surf`, `stats`, etc. 

### Step 6: Visualize the Results

You can visualize the results using FreeSurfer's visualization tools. 

Example 1: View the brain surface reconstruction

```bash
freeview -v $SUBJECTS_DIR/sub-08/mri/brain.mgz \
         -f $SUBJECTS_DIR/sub-08/surf/lh.white:edgecolor=blue \
         -f $SUBJECTS_DIR/sub-08/surf/rh.white:edgecolor=red
```

Example 2: Viewing subcortical structures 

```bash
freeview -v $SUBJECTS_DIR/sub-08/mri/brain.mgz \
         -v $SUBJECTS_DIR/sub-08/mri/aseg.mgz:colormap=lut
```


Example 3: Viewing White Matter and Pial Surfaces 

```bash
freeview -v $SUBJECTS_DIR/sub-08/mri/brain.mgz \
         -f $SUBJECTS_DIR/sub-08/surf/lh.white:edgecolor=blue \
         -f $SUBJECTS_DIR/sub-08/surf/rh.white:edgecolor=blue \
         -f $SUBJECTS_DIR/sub-08/surf/lh.pial:edgecolor=red \
         -f $SUBJECTS_DIR/sub-08/surf/rh.pial:edgecolor=red
```


```bash
freeview -v $SUBJECTS_DIR/sub-08/mri/brain.mgz \
         -f $SUBJECTS_DIR/sub-08/surf/lh.thickness:colormap=heat \
         -f $SUBJECTS_DIR/sub-08/surf/rh.thickness:colormap=heat
```
