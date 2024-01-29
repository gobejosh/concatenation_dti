import numpy as np
import nibabel as nib
import os



def concatenation(a,b):
    x1, y1, z1, t1 = np.shape(a)
    x2, y2, z2, t2 = np.shape(b)

    final = np.zeros((x1, y1, z1 + z2, t1))

    for z in range(z2):
        final[:,:,(z2-(z+1)),:] = b[:,:,(z2-(z+1)),:]
    for z in range(z1):
        final[:,:,(z2 + (z1 - (z+1))),:] = a[:,:,(z1-(z+1)),:]
    return final



parts = []

img1 = nib.load('sub-fluorinert_run-01_dwi.nii.gz')
nimg1 = np.array(img1.dataobj)
parts.append(nimg1)

img2 = nib.load('sub-fluorinert_run-02_dwi.nii.gz')
nimg2 = np.array(img2.dataobj)
parts.append(nimg2)

img3 = nib.load('sub-fluorinert_run-03_dwi.nii.gz')
nimg3 = np.array(img3.dataobj)
parts.append(nimg3)

img4 = nib.load('sub-fluorinert_run-04_dwi.nii.gz')
nimg4 = np.array(img4.dataobj)
parts.append(nimg4)

defvol = np.zeros(np.shape(nimg1))
for part in parts:
    defvol = concatenation(defvol, part)

final_img = nib.Nifti1Image(defvol, np.eye(4))
nib.save(final_img, os.path.join("/home/gobej/Documents/23_Singe/concatenation", 'fluorinert_2023.nii.gz'))