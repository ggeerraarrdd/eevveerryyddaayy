# #########################################################################
#
# WARNING: DO NOT MODIFY THIS CONFIG FILE.
#
# Manual modifications can cause unintended behavior.
# The system will manage this file automatically.
#
# #########################################################################





"""
Locations of Critical Directories
===========================================================================

Controls the paths to critical directories.

Parameters
----------
SOLUTIONS_DIR : str
    Relative path to the directory containing solution files
    Default: 'solutions'
CONFIG_DIR : str
    Relative path to the configuration files directory
    Default: 'src/main/config'
TEMPLATES_DIR : str
    Relative path to the templates directory
    Default: 'src/main/templates' 
"""
import os
ROOT_DIR_1=os.path.abspath(os.path.join(os.getcwd(), '.'))
ROOT_DIR_2=os.path.abspath(os.path.join(os.getcwd(), '..'))
SOLUTIONS_DIR="solutions"
CONFIG_DIR="src/config"
TEMPLATES_DIR="src/templates"
