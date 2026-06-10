# Local Setup Guide

## MacOS/ Unix

You should make sure the following software is installed on your machine before proceeding with the notebook setup. Usually, you can check whether a programme is installed with the terminal command `${myprogramme} --version`:

- python3 [link](https://www.python.org/downloads/)
- pip: Should be installed alongside Python download
- git: [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- jupyter (must have pip installed first) [link](https://jupyter.org/install#jupyter-notebook)

### Setup from the terminal

#### Downloading the notebooks
```bash
git clone https://github.com/eimearconroy/notebooks-collection-opendata.git
cd notebooks-collection-opendata/
git checkout sept_26_accounts
```

#### Installing dependencies
```bash
python -m venv opendata
source opendata/bin/activate

pip install ipykernel
pip install numpy
pip install matplotlib
pip install uproot
pip install cernopendata_client
pip install hist
pip install mplhep
pip install tensorflow
pip install sklearn
pip install pandas
```

### Launch Jupyter
```bash
python -m ipykernel install --user --name=opendata --display-name "OpenData Env"
jupyter notebook
```
Jupyter should launch in a browser tab. If it doesn't launch automatically, the terminal should have included in the Jupyter launch output lines like:

```
Jupyter Notebook 6.5.7 is running at:
http://localhost:8888/?token=da8511adafd33d66daa3a624e1d939be5b0c368dc1bb1411
```

Note that your url will be slightly different. Copy/paste the link into a fresh browser tab to launch.

Every time you enter a notebook for the first time, do Kernel → Change Kernel → OpenData Env. This should activate the correct environment with all dependencies installed. Whenever you open a new notebook. Check the box in the top-right (underneath the Python logo and the Logout button) that the correct kernel, and not the default, is running.

### Everyday Quickstart
```bash
source opendata/bin/activate
jupyter notebook
```


### Notes
- If `python` commands don't seem to be working, try `python3` instead
- There's a chance I've left out some dependencies in my installation list! Your first port of call when receiving the error `"ModuleNotFoundError: No module named 'X'"` should be to go to the terminal and do:
    
    ```bash
    source opendata/bin/activate
    pip install <packagename>
    ```


## Windows???