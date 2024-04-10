"""Demo context manager making a resource context-capable."""
from contextlib import contextmanager

@contextmanager
def opening(filename):
   """making opening a context-capable resource that can be used in with."""
   f = open(filename)
   try:
       yield f
   finally:
       f.close()
