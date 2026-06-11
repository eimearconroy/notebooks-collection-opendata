# Local Setup Guide

## MacOS/ Unix

You should make sure the following software is installed on your machine before proceeding with the notebook setup. Usually, you can check whether a programme is installed with the terminal command `${myprogramme} --version`:

- python3 [link](https://www.python.org/downloads/)
- pip: Should be installed alongside Python download
- git: [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- jupyter (must have pip installed first) [link](https://jupyter.org/install#jupyter-notebook)

### Setup from the terminal

#### Downloading the notebooks

First, we want to download the notebooks from the remote repository in which they're stored. The software used to manage the remote hosting, downloading, and version control for developers is called `git`. To download, type the following commands into the terminal:

```bash
git clone https://github.com/eimearconroy/notebooks-collection-opendata.git #Download our repository
cd notebooks-collection-opendata/ #Enter our repository
git checkout lmh_sap #git allows us to keep different versions ("branches") of our repository available at once. Switch to the correct branch
```

#### Installing dependencies

The notebooks we will run do not have all the code they will need written out inside them! Instead, they employ several external "packages" containing pre-written code. Python packages are often incredibly helpful, as many are professionally written and very well maintained. However, before installing our packages, it is good practice to first set up a "virtual environment". This sets up an isolated area in which to run our code, and also prevents any packages we install from impacting the rest of our machine. The capacity to create a virtual environment comes inbuilt in our python installation. Type into the terminal: 

```bash
python -m venv opendata #Set up a virtual environment called 'opendata'
source opendata/bin/activate #Activate 'opendata'
```

You will know your virtual environment has been correctly activated if the next line on your terminal begins with `(opendata) ${your_machine}:notebooks-collection-opendata ${your_username} $`

Another benefit of python packages is that they are very easy to install. `pip`, the Package Installer for Python comes inbuilt in our python installation. Before installing anything, it is good practice to ensure our version of `pip` is up to date by typing into the terminal `pip install --upgrade pip`. Then, use `pip` to install the packages our code depends on ("dependencies") by typing into the terminal:

```bash
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

Finally, we will launch `jupyter`, the programme we will use to view, run, and edit the notebooks. The easiest way to do this is to type into the terminal:

### Launch Jupyter
```bash
python -m ipykernel install --user --name=opendata --display-name "OpenData Env"
jupyter notebook
```
Jupyter should launch in a browser tab. If it doesn't launch automatically, the terminal output should include lines like:

```
Jupyter Notebook 6.5.7 is running at:
http://localhost:8888/?token=da8511adafd33d66daa3a624e1d939be5b0c368dc1bb1411
```

Note that your url will be slightly different. Copy/paste the link into a fresh browser tab to launch.

Every time you enter a notebook for the first time, do Kernel → Change Kernel → OpenData Env. This should activate the correct environment with all dependencies installed. Whenever you open a new notebook, check the box in the top-right (underneath the Python logo and the Logout button) that the correct kernel, and not the default, is running.

### Everyday Quickstart

We now have everything we need installed for using the notebooks. The next time you want to launch the notebooks, all you need to type into the terminal is:

```bash
source opendata/bin/activate
jupyter notebook
```

Once Jupyter has launched, interact with the notebooks via the jupyter browser tab as normal. 


### Notes
- If `python` commands don't seem to be working, try `python3` instead
- There's a chance I've left out some dependencies in my installation list! Your first port of call when receiving the error `"ModuleNotFoundError: No module named 'X'"` should be to go to the terminal and do:
    
```bash
source opendata/bin/activate
pip install ${packagename}
```


## Windows???