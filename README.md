# RbRG Impelementation
Download, configuration and deploying:

    1. clone repository into a <folder>, that is, run the following commands in the terminal:
            - cd <folder>
            - git clone (https://github.com/kipronokoech/RbRG.git)
    2. cd rbrg/Python Implementation
    3. create virtual environment: virtualenv . (if you have multiple python versions, run: virtualenv -p python3 .)
    4. enter virtual environment: source ./bin/activate
    5. Install requirements: pip install -r requirements.txt 
    6. recompile "callRGR", which compiles .cpp file for Python usage:
            - python setup.py build_ext --inplace
    7. you can now run mainRbRG as notebook or as .py file
    
### Virtual environment 
For information on how to create and activate virtual environment check [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).

## Repository Structure:

        ├── Example #Contains files to demonstrate the perfomance of RbRG
        ├── Python Implementation├── modules #Contains all user-defined modules used in the project.
        |                        └──  ...
        ├── README.md
        └── RbRG paper
