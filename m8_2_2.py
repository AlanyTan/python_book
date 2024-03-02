from contextlib import contextmanager

@contextmanager
def opening(filename):
   f = open(filename)
   try:
       yield f
   finally:
       f.close()
