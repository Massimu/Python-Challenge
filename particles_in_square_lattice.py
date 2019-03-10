#Packages:
import random , os , pylab , math, copy, sys
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
#setting input arguments L_box / N / n_steps
if(len(sys.argv) < 4 or len(sys.argv) > 4):
	print ('Not enough arguments,\n Please ENTER the box length as "L_box"\
        \n ,the number of particles "N", and \the number of iterations as "n_steps" ')
	exit() 
if(len(sys.argv)>1):
	L_box = int(sys.argv[1])
if(len(sys.argv)>2):
	N = int(sys.argv[2])  
if(len(sys.argv)>3):
	n_steps = int(sys.argv[3])
if(N > pow(L_box-1,2)):
       print("This number is not valid.Consider the box size!!")
       sys.exit()
#------------------------------------------------------------------------------
#create a file to store coordinates of particles
filepath = os.path.join(os.getcwd(), 'traj.xyz')
if not os.path.exists(filepath):
    with open(filepath, 'w'):
        pass
#------------------------------------------------------------------------------
#Graphic part
#openning a directory to store the pics
output_dir = 'Particles_in_square_box'
img = 0
if not os.path.exists(output_dir): os.makedirs(output_dir)
def snapshot(pos,colors):
    global img
    pylab.subplots_adjust(left=0.10, right=0.90, top=0.90, bottom=0.10)
    pylab.gcf().set_size_inches(6, 6)
    pylab.axis([0, 1, 0, 1])
    pylab.title('t = '+ str(step))
    pylab.setp(pylab.gca(), xticks=[0, L_box], yticks=[0, L_box])
    for (x, y), c in zip(pos,colors):
        circle = pylab.Circle((x, y), radius= 0.3, fc=c)  #Radius is r of particle in pics
        pylab.gca().add_patch(circle)
    pylab.savefig(os.path.join(output_dir, '%d.png' % img), transparent=True)
    pylab.close()
    img += 1
#------------------------------------------------------------------------------
#Wall potentional:
def V_wall(x):
    temp = float(-1./x[0])
    return(temp)
##painr potentioal:
def V_pair(x1,x2):
     temp = pow(q,2)/(math.sqrt(pow((x2[0]-x1[0]),2)+ pow((x2[1]-x1[1]),2)))
     return (temp)
#------------------------------------------------------------------------------
#State Energy
def E(L):
    E_Wall = []
    E_pair = []
    E      = []
    #Calculating WALL potential of the particles 
    E_Wall = [V_wall(a) for a in L]

    #Calculating PAIR potential of the particles 
    for i in range(N):
        a = L[i]
        eng = [V_pair(a,c) for c in L if c != a] 
        e = sum(list(eng))
        E_pair.append(e)
    E = [sum(x) for x in zip(E_pair, E_Wall)]
    E_tot = sum(E)
    return(E_tot)
#------------------------------------------------------------------------------
#Direction function to choose a direction with same transition probability
def direction(x):
    d = [[0,-1],[1,0],[0,1],[-1,0]]   #movement vectors: down, right, up, left
    dd = d[random.randint(0,3)]       #a random choose from direction list
    move = [sum(m) for m in zip(x,dd)] 
    return move
#------------------------------------------------------------------------------
#constants
q = 1.60217662*pow(10,-19)                  
K = 1.38064852 * pow(10,-23)
T = 300
#------------------------------------------------------------------------------
#initialization of system:
sigma = 1  #lenght step to move correctly and provide oundary conditions.

condition = False
while condition == False:
    L = [[int(random.uniform(sigma, L_box )), int(random.uniform(sigma, L_box ))]]
    for k in range(1, N):
        a = [int(random.uniform(sigma, L_box )), int(random.uniform(sigma, L_box ))]
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
        if min_dist <  sigma: 
            condition = False
            break
        else:
            L.append(a)
            condition = True
#------------------------------------------------------------------------------
#Write file
with open(filepath, "a") as f:
    f.write("0\n")  
for i in range(N):
    with open(filepath, "a") as f:
        f.write("1  %s\t%s\n" % (L[i][0],L[i][1]))         
colors = ['r' for i in range(N)]   #color of particles
#------------------------------------------------------------------------------
#initial ENERGY of the system
E0 = E(L)
E_list = []
E_list.append(E0)  #list of timestep Energies
#------------------------------------------------------------------------------
#iteration      
for step in range(n_steps):
     L_copy = copy.deepcopy(L)          #to make a clone copy
     a = random.choice(L_copy)  #random choice of a disk to modify its coordinates
     b = direction(a)
     min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L_copy if c != a) 
     box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > L_box - sigma #overlab test
     if not (box_cond or min_dist < sigma):  
         a[:] = b    
         Delta_E = E(L_copy) - E_list[step] 
         if(Delta_E <= 0): 
             L = L_copy
             E_list.append(E(L_copy))
         else: 
            if(math.exp(-(Delta_E)/K*T) >= random.uniform(0,1)):
               L = L_copy
               E_list.append(E_list(L),"\n")
            else:
               E_list.append(E_list[step])
     else:
         E_list.append(E_list[step])
     snapshot(L,colors)
     with open(filepath, "a") as f:
         f.write("\n%d\n" % (step+1,))
     for i in range(N):
         with open(filepath, "a") as f:
            f.write("1  %s\t%s\n" % (L[i][0],L[i][1]))
     print(step+1,"-->",L,"\n")
     
#Save the configuration energy:
f = open("Energy.txt", "w")
mylist = E_list
f.write("\n".join(map(lambda x: str(x), mylist)))
f.close() 

#Store the configuration enery plot
plt.plot(E_list)
plt.title("Configuration Energy")
plt.xlabel("Step")
plt.grid()
plt.ylabel("E")
plt.savefig('Configuration_Energy.png')
     
     
     
     
     
     