# AOSP framework permissions list
This tool is meant to extract:
* permission groups (name, icon, label, description)
* permissions (name, label, description, group, protection level)

from the AOSP framework base source and generate a JSON file containing information listed above in the locale you choose. 

This tool uses the [VectorDrawable2Svg script of Alessandro Lucchet](https://gitlab.com/Hyperion777/VectorDrawable2Svg) which has been lightly modified.

**This tool is only compatible with Python >= 3.5**

## Preliminaries
First of all, you have to clone the huge AOSP repository:
```
mkdir AOSP
git clone https://android.googlesource.com/platform/frameworks/base AOSP
```
## Usage
```
pip install git+https://github.com/mayankmetha/aosp_framework_perm_list
aosp_framework_perm_list [path to AOSP folder] [2-letter locale] [destination folder]
```
the destination folder will be automatically created.