import sys

import pylint

if __name__ == '__main__':
  sys.argv[0] = "pylint"
  pylint.run_pylint()
