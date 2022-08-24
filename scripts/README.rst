Example Scripts
===============

The example scripts provided here are intended to give the interested user
some idea on how to use ``cloudynight`` functionality.

The following example scripts are included here:

* ``generate_mask.py``: generate an image mask to mask the local horizon
* ``populate_subregions.py``: create subregions and plot their locations
  on the sky
* ``extract_features.py``: read in images, mask them, and extract
  per-subregion image features
* ``model_lightgbm.py``: load a feature file, train the `lightGBM` model and
  predict cloud coverage for individual subregions
* ``model_resnet.py``: train the ResNet model and derive accuracy scores

All these example scripts are intended to work with the example data
provided and should be run in this order.

It should not be hard to modify these scripts to work with
data from other all-sky cameras.
