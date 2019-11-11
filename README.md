# RbRG Impelementation
Download, configuration and deploying:

    1. clone repository
    2. cd rgr-public/Python
    3. create virtual environment: virtualenv . (if you have multiple python versions, run: virtualenv -p python3 .)
    4. enter virtual environment: source ./bin/activate
    5. Install requirements: pip install -r requirements.txt (if it fails, try upgrading pip: pip install --upgrade pip)
    6. recompile "callRGR", which compiles .cpp file for Python usage:
      ..* python setup.py build_ext --inplace
    7. run the .py code of your choice:
        ..* Refine CNN coarse segmentation: python runRGR.py
        ..* Grow segmentation mask from traces: python runRGR_traces.py

1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
