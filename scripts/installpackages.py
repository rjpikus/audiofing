import sys
import subprocess

# 1) If on UBUNTU you need these too: Sudo apt-get install python-tk ffmpeg portaudio19-dev  

# 2) PYTHON STANDARD LIBRARY used in the app: 
# json, os sys, sqlite3, itertools, hashlib, operator, wave, argparse, config 

# 3) Must install the following packages:
# Matplotlib 3.5 - might not work on py3.10
# Pymongo 4.1.1 - 
# Db 0.5.3 - 
# Numpy - 1.22.3, Mar 7, 2022
# Scipy 1.8.0 - requires python 3.8, numpy 1.17.3
# Reader 2.12, py3.7 +>
# Termcolor 1.1.0, 2011
# Pydub 0.25.1, 3.8
# Pyaudio 0.2.11 , 2017, requires portaudio


packages = [
    'db',
    'reader',
    'pymongo',
    'termcolor',
    'numpy',
    'scipy',
    'pydub',
    'matplotlib',
    'portaudio',
    'pyaudio'
    ]
    

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'<packagename>'])