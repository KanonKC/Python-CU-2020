# Prog-05: Solving TSP by simple-SA
# ID: Name
# ...
# I hereby declare that I coded the SA part by myself.

import math
import random

from matplotlib import pyplot as plt
from matplotlib import animation, rc
#------------------------------------------------
def animate(X, Y, tour_log):
  fig, ax = plt.subplots()

  line, = ax.plot(X, Y, color='blue')
  line.set_marker('o')
  line.set_markersize(4)  
  min_x, max_x = min(X), max(X)
  min_y, max_y = min(Y), max(Y)
  w = max_x - min_x
  h = max_y - min_y
  width = 6 if w > h else 6*w/h
  height = 6 if h > w else 6*h/w
  fig.set_size_inches(max(4,width), max(4,height))
  dy = abs(0.1*(max_y - min_y))
  txt = ax.text(min_x, min_y-1.7*dy, '', fontsize=10)
  ax.set_ylim(min_y-2*dy, max_y+dy)
  ani = animation.FuncAnimation(fig, next_path,
                  frames=len(tour_log),
                  fargs=[X, Y, tour_log, line, txt],
                  interval=10,
                  repeat=False,
                  blit=True)
  plt.show()

def next_path(k, X, Y, tour_log, line, txt):
  T, tour = tour_log[k]
  N = len(tour)
  d = sum(D[tour[i]][tour[i-1]] for i in range(N))  
  txt.set_text("T = " + str(round(T,3)) + \
               "\ntour length = " + str(round(d,2)))
  x = [X[p] for p in tour] + [X[tour[0]]]
  y = [Y[p] for p in tour] + [Y[tour[0]]]
  line.set_data(x, y)
  if k == len(tour_log)-1:
    txt.set_color('red')
    line.set_color('red')
  return (line, txt)

def read_map(fname):
  f = open(fname)
  X, Y = [], []
  for line in f:
    if line.strip()=='EOF': break
    d = line.split()
    X.append(float(d[1]))
    Y.append(float(d[2]))
  f.close()
  return X, Y

def dist(p1, p2):
  return D[p1][p2]

def calc_all_pair_distances(X, Y):
  N = len(X)
  D = [[0.0]*N for i in range(N)]
  for i in range(N):
    for j in range(i, N):
      D[i][j] = D[j][i] = \
                math.hypot(X[i]-X[j], Y[i]-Y[j])
  return D

#------------  main program -----------------------
map_name = input()
X, Y = read_map(map_name)
D = calc_all_pair_distances(X, Y)
N = len(X)                # number of points
tour_log = []
tour = list(range(N))     # [0,1,2,3,4,...,N-1]

#--- let's the SA begins --------------
loop = 0

T = N*10                  # starting temperature
#????? ? ? ????? :         # while not finished

# create a new tour from the current tour
i = random.randint(0, N-2)
j = random.randint(i+1, N-1)
    
tour1 = list(tour)  # copy list
tour1[i], tour1[j] = tour1[j], tour1[i]  # swap
# compute dE = length_of_tour1 ????????? length_of_tour
dE = dist(tour1[i-1], tour1[i      ]) + \
     dist(tour1[i  ], tour1[i+1    ]) + \
     dist(tour1[j-1], tour1[j      ]) + \
     dist(tour1[j  ], tour1[(j+1)%N]) - \
     dist(tour[ i-1], tour[ i      ]) - \
     dist(tour[ i  ], tour[ i+1    ]) - \
     dist(tour[ j-1], tour[ j      ]) - \
     dist(tour[ j  ], tour[(j+1)%N ])
# accept new tour if shorter or within prob.
#if ????????? :
    #tour = tour1

#? ?? ????   # lower the temperature
# keep tour changes in tour_log
loop += 1
if loop % N == 0:
    tour_log += [[T, tour]]
    tour_log += [[T, tour]] # the final tour
print(tour)


animate(X, Y, tour_log ) # let's animate