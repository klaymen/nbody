from sys import platform as _platform
from matplotlib import use
if _platform =='darwin':
    use('MacOSX') # Use Cocoa rendering for OS X
else:
    use('GTKAgg') # Use gtk as a faster back-end  
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as lines

import importlib
import numpy as np

import utils
utils.addSubfolderToPath("core")
utils.addSubfolderToPath("exp")

from body import Body
from nbody import Nbody

experiment = importlib.import_module("exp_003")

exp = experiment.Dataset()
sim = Nbody(exp.bodies)

try:
    sim.G = exp.gravitationalConstant
except:
    pass

try:
    sim.minDist = exp.minDist
except:
    pass

def main():

    initialData = sim.getCoords()
    m = sim.getMasses()
    factor = exp.markSizes[1]/max(m)
    sizes = [factor*float(i) if factor*float(i) > exp.markSizes[0] else exp.markSizes[0] for i in m]    
    x, y = initialData[0], initialData[1]
    
    fig = plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    fig.canvas.set_window_title('N-Body')
    ax = plt.axes(aspect='equal', autoscale_on=False, xlim=(-exp.plotSize, exp.plotSize), ylim=(-exp.plotSize, exp.plotSize))
    ax.set_xlabel('Distance / m')
    ax.set_ylabel('Distance / m')
    
    scat = ax.scatter(x, y, c=sim.getColors(), s=sizes, edgecolors='none')
    
    annotation = []
    for body in exp.bodies:
        annotation.append(ax.annotate(body.name, xy=(body.pos[0],body.pos[1])))

    titles = [  plt.title("", loc='left'),
                plt.title("", loc='center'),
                plt.title("", loc='right')]

    ani = animation.FuncAnimation(fig, update_plot, interval=2, frames=50, fargs=(scat, exp, sim, annotation, titles, ax), blit=False)
    plt.show()

def update_plot(i, scat, exp, sim, annotation, titles, ax):
    
    for skip in range(exp.skipFrames):
        sim.step(exp.timeStep)
    else:
        sim.step(exp.timeStep)
    
    data = sim.getCoords()
    
    for body in range(len(exp.bodies)):
        annotation[body].xyann = (data[0][body] + exp.annotationShift,data[1][body] + exp.annotationShift)
    
    titles[2].set_text(str(sim.elapsedTime/60/60/24) + ' day(s)')
    
    names = '(' + exp.bodies[0].name + ', ' + exp.bodies[1].name + ')'
    titles[1].set_text('D' + names + '=' + str(int(exp.bodies[0].getDistance(exp.bodies[1])/1000)) + ' km')

    if exp.lockedBody > -1:
        ax.set_xlim([exp.bodies[exp.lockedBody].pos[0]-exp.plotSize, 
                     exp.bodies[exp.lockedBody].pos[0]+exp.plotSize])
                     
        ax.set_ylim([exp.bodies[exp.lockedBody].pos[1]-exp.plotSize, 
                     exp.bodies[exp.lockedBody].pos[1]+exp.plotSize])

    scat.set_offsets(zip(*[data[0],data[1]])) #Needs transpose

    plt.draw()

    return

main()
