# RbRG Impelementation
Download, configuration and deploying:

    -clone repository
    -cd rgr-public/Python
    -create virtual environment: virtualenv . (if you have multiple python versions, run: virtualenv -p python3 .)
    -enter virtual environment: source ./bin/activate
    -install requirements: pip install -r requirements.txt (if it fails, try upgrading pip: pip install --upgrade pip)
    -recompile "callRGR", which compiles .cpp file for Python usage:
        --python setup.py build_ext --inplace
    -run the .py code of your choice:
        --Refine CNN coarse segmentation: python runRGR.py
        --Grow segmentation mask from traces: python runRGR_traces.py
