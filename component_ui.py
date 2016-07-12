'''
the user interface for the titan_runner component 
Created on May 12, 2014

@author: dgrewal
'''

import argparse

__version__ = 'titan_plot_v0.1'

##Make a UI

parser = argparse.ArgumentParser(prog='''TITAN PLOT''',
                                 description = '''Plot TITAN results''')

parser.add_argument("--obj_file", 
                    required = True, 
                    help= '''The object file generated by titan ''')

parser.add_argument("--outdir", 
                    required = True, 
                    help="The path to output directory")

parser.add_argument("--num_clusters", 
                    default = '1',  
                    help="Number of clonal clusters")

parser.add_argument("--id", 
                    required = True,  
                    help="the sample id ")

parser.add_argument("--rid", 
                    required = True,  
                    help="the run id ")

parser.add_argument("--chr",
                    default = None,
                    help='''chromosome to be used for plotting,
                          If not provided all chromosomes except Y will be plotted''')

args = parser.parse_args()
