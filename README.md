# Local Setup Guide

Navigate to the relevant section below for the installation instructions specific to the operating system used by your computer.

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
pip install scikit-learn
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


## Windows

Call up "Windows Powershell" or a command line terminal.
This is usually an app called `terminal` in your list of apps on Windows 11.

You might want to attach the `terminal` app to your taskbar or start-up menu.

Clicking on the `terminal` icon will pop up a command-line interface. 
It will usually start up in your default area on the C: drive. You can see where it starts by typing at the prompt:
```bash
pwd
``` 

In the powershell (also called this the 'shell' or the 'terminal') check the python version you are using with:
```bash
python --version
```

This project code works with Python Version 3.10 but it might be OK for later or earlier versions of Python. If you do not have python installed (unlikely) then download version 3.10 of python3 from the link offered below. 

If you have a very old version of Python (version 2 or earlier) you **must** update to version 3.10. 
It is not advised (yet) to update to a python version newer than this. 

If you already have a version of python newer than 3.10 it is possible the code may work anyway, give it a try before you spend time winding back to an earlier python version.
You will need the same programs that are mentioned above, namely: 

- python3 [link to python](https://www.python.org/downloads/)
- pip: Should be installed alongside Python download
- git: [link to github](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- jupyter (must have pip installed first) [link to notebooks](https://jupyter.org/install#jupyter-notebook)

### Setup from the Windows terminal
From the Powershell (or terminal) window the downloading and installation of the code is very similar as above. Start by *cloning* the github files from the repository. 


```bash
git clone https://github.com/eimearconroy/notebooks-collection-opendata.git #Download our repository
cd notebooks-collection-opendata/ #Enter our repository
git checkout lmh_sap #git allows us to keep different versions ("branches") of our repository available at once. Switch to the correct branch
```
Change directories until you get to the area where your `github` files have been extracted.

This will be within a folder called: 
`notebooks-collection-opendata-lmh_sap`, run the remaining instructions **as given above** from within this folder.

#### after following the process of cloning the notebooks area you do
```bash
python -m venv opendata #create virtual 'opendata' environment
.\opendata\Scripts\activate #Activate 'opendata'

python -m pip install --upgrade pip #should only need this the first time
```
Next you need to initiate the series of code downloads mentioned above. 
Namely (*but keep reading, there are some quirks*):
```bash
pip install ipykernel
pip install numpy
pip install matplotlib
pip install uproot
pip install cernopendata_client
pip install hist
pip install mplhep
pip install tensorflow #see below
pip install scikit-learn
pip install pandas
```

There are potential problems with `tensorflow` the directory lengths are sometimes too long for windows machines.  
Administrator privileges might be needed to overcome this. (Check an AI for suggestions on how to increase allowed Windows directory lengths.)


### Launching Jupyter (as above) then works!
```bash
python -m ipykernel install --user --name=opendata --display-name "OpenData Env"
jupyter notebook
```
#### Windows everyday quickstart

Click on the `terminal` icon then:
```bash
cd notebooks-collection-opendata #change directories to the github area
.\opendata\Scripts\activate
jupyter notebook
```
The default browser should launch (after a bit) and everything should proceed the same from now on regardless of OS. 

