# RbRG Impelementation
Download, configuration and deploying:

    1. clone repository into a <folder>, that is, run the following commands in the terminal:
            - cd <folder>
            - git clone (https://github.com/kipronokoech/RbRG.git)
    2. cd rbrg/Python
    3. create virtual environment: virtualenv . (if you have multiple python versions, run: virtualenv -p python3 .)
    4. enter virtual environment: source ./bin/activate
    5. Install requirements: pip install -r requirements.txt (if it fails, try upgrading pip: pip install --upgrade pip)
    6. recompile "callRGR", which compiles .cpp file for Python usage:
            - python setup.py build_ext --inplace
    7. run the .py code of your choice:
            - Refine CNN coarse segmentation: python runRGR.py
            - Grow segmentation mask from traces: python runRGR_traces.py


[title](https://www.example.com)
