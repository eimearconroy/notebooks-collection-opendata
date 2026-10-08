import os, sys

os.environ["PATH"] = f"{os.path.dirname(sys.executable)}/../bin:" + os.environ["PATH"] #Add venv to $PATH if running in a virtual envirnoment
#May not be needed at RAL
    
from cernopendata_client import searcher as searcher
from cernopendata_client import config as config
    
def get_files(my_doi):
    server = config.SERVER_HTTP_URI 
    protocol = "xrootd"
    expand = True
   
    record_json = searcher.get_record_as_json(server=server, doi=my_doi)
    
    search_file_list = searcher.get_files_list(server, record_json, protocol, expand)
    my_file_list = [f[0].replace("root://eospublic.cern.ch//eos","http://opendata.cern.ch/eos") for f in search_file_list]
    return my_file_list
    
def print_files(my_doi):
    my_file_list = get_files(my_doi)
    for f in my_file_list: print(f)