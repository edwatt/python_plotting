import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
from math import sin, cos, pi

# class that holds analog data for N samples
class AnalogData:
  # constr
  def __init__(self, maxLen):
    self.ax = deque([0.0]*maxLen)
    self.ay = deque([0.0]*maxLen)
    self.az = deque([0.0]*maxLen)
    self.maxLen = maxLen

  # ring buffer
  def addToBuf(self, buf, val):
    if len(buf) < self.maxLen:
      buf.append(val)
    else:
      buf.popleft()
      buf.append(val)

  # add data
  def add(self, data):
    assert(len(data) == 3)
    self.addToBuf(self.az, data[0])
    self.addToBuf(self.ax, data[1])
    self.addToBuf(self.ay, data[2])
    
# plot class
class AnalogPlot:
  # constr
  def __init__(self, analogData):
    # set plot to animated
    plt.ion() 
    self.axline, = plt.plot(analogData.ax)
    self.ayline, = plt.plot(analogData.ay)
    self.plt = plt
    plt.ylim([-2,2])

  # update plot
  def update(self, analogData):
    ticks = range(len(analogData.az))[0::int(len(analogData.az)/5)]
    myticks = list(analogData.az[i] for i in xrange(0, len(analogData.az),int(len(analogData.az)/4)))
    self.plt.xticks(ticks, myticks)
    self.axline.set_ydata(analogData.ax)
    self.ayline.set_ydata(analogData.ay)
    plt.draw()

# main() function
def main():


  # plot parameters
  analogData = AnalogData(101)
  analogPlot = AnalogPlot(analogData)

  print 'plotting data...'

  num_arr = range(1000)
  x = [x*2*pi/30 for x in range(101)]
  y1 = [[t,sin(t),cos(t)] for t in x]

  for y in y1:
      data = y
      #print data
      if(len(data) == 3):
        analogData.add(data)
        analogPlot.update(analogData)
      sleep(0.5)

# call main
if __name__ == '__main__':
  main()
