#
# common-version.py
# Convenience script to apply customizations to CPP flags
#
from __future__ import print_function

Import("env", "projenv")

import subprocess
import datetime

git_branch = None
try:
  git_branch = subprocess.check_output("git rev-parse --abbrev-ref HEAD")
except:
  pass

if git_branch:

  def escape_string(s):
    return f"\\\"{s}\\\""

  git_branch = git_branch.decode('utf-8').strip()
  today = str(datetime.date.today())

  print(f'SHORT_BUILD_VERSION={git_branch}')
  print(f'STRING_DISTRIBUTION_DATE={today}')

  projenv.ProcessUnFlags("-DSHORT_BUILD_VERSION")
  projenv.ProcessUnFlags("-DSTRING_DISTRIBUTION_DATE")

  projenv.Append(CPPDEFINES=[
    ("SHORT_BUILD_VERSION", escape_string(git_branch.upper())),
    ("STRING_DISTRIBUTION_DATE", escape_string(today))
  ])

  #print(env.Dump())
