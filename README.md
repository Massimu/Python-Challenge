# Python-Challenge
------------------------------
particles_in_square_lattice.py
------------------------------

This py file includes the desired program to implement a MC simulation
of particles in a square lattice. One can insert the size of the box,
the number of particles, and the number of iterations as L_box, N, n_steps.


  It is necessary to consider some points to enter this arguments for running 
the program: 

  1- As the box is a littice of points and particle can not place 
on the legends there are some available points for each box, e.g. if one picking 
the L-box = 5, the number of particles can not be greater than 25. 
NOTICE: the code will be terminated in this case with a message.

  2- For each set up, depending on the arguments the system goes to equilibrium 
at a certain time when the configuration energy of the system reach to the minimum
value.


  Run in Terminal:

  example: 

  `python3 particles_in_square_lattice.py 10 10 1000`


  This code follows this algorithm:

  1- Establish an initial configuration randomly.

  2- Choose a particle at random and make a trial change in its position.

  3- Compute DeltaE, the change in the potential energy of the system due to the trial move.

  4- If DeltaE is less than or equal to zero, accept the new configuration.

  5- If DeltaE is positive, compute the quantity w = exp(-DeltaE)/KT.

  6- Generate a uniform random number r in the unit interval [0,1].

  7- If r less or equal than w, accept the trial move; otherwise retain the previous microstate.

  The code stores the configurations as pictures and particles positions as trajectory.
  It also plot the energy at the end and then store the energy as a single file.

  ----------------------------------------------------------------------------------------

------------------------------
mammal_list.py
------------------------------

  This code will help to create a txt file including three type of mammals and thier
  sex, age, and specific features just like problem wants.

  one will be asked for the number of mammals, and then depending on the choose 
  other quetions comes to create a list as an input file for the Main program.

  Run in Terminal:

  `python3 mammal_list.py`

  ----------------------------------------------------------------------------------------
------------------------------
Mammal_class.py
------------------------------

  This code gives the 'mammals.txt' as an input data. The code impleneted a class 
  Mammal with three subclasses as Dog , Cat, and Whale. The main class has two 
  generic elements sex, and age. Each subclasses has an extra element as specific
  as they are available at code.

  Run in Terminal:

  `python3 Mammal_class.py`

  the factory within class opens the file and put it in different lists to show. 
  one can print the list or the result of factory.

  The result of running the code is a table including classification of data 
  from file and also a list of objects in data indicating their class name.
