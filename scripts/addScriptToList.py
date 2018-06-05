import sys
import os
cwd = sys.path[0]
if(len(sys.argv) > 1):
  datafile = sys.argv[1]
  if (os.path.isfile(datafile) and datafile.endswith('.py')):
    with open(cwd+'/allPlots.sh', 'a') as f:
      f.write("python -u '"+os.path.abspath(datafile)+"'\n")