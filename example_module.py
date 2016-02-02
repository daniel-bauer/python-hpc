""" 
A module to illustrate modules .
"""
class A (object):
  def __init__ ( self , * args ) :
    self.args = args

  def quadruple ( x ) :
    return x **4

x = 42
print (" This is an example module .")
