# RbRG Impelementation
Download, configuration and deploying:

    1. clone repository
    2. cd rgr-public/Python
    3. create virtual environment: virtualenv . (if you have multiple python versions, run: virtualenv -p python3 .)
    4. enter virtual environment: source ./bin/activate
    5. Install requirements: pip install -r requirements.txt (if it fails, try upgrading pip: pip install --upgrade pip)
    * recompile "callRGR", which compiles .cpp file for Python usage:
        --python setup.py build_ext --inplace
    * run the .py code of your choice:
        --Refine CNN coarse segmentation: python runRGR.py
        --Grow segmentation mask from traces: python runRGR_traces.py
