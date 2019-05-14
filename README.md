# Autonomous-Parking-Control-System
Training:
•	The vehicle is controlled manually using the Raspberry Pi and made to park itself. The corresponding camera feed (pictures taken at a rate of 30 frames per second) is stored on the Raspberry Pi itself.
•	This process of manually training the vehicle is done several times so as to get enough variance in the data obtained in order to get a good quality dataset.
•	The pictures taken by the camera are transferred to the PC and classified according to the motor driver commands at each instant.
•	The classified images are then passed as inputs to an artificial neural network and the weights are generated using backpropagation.
The interactive.py is used to control the Car manually, which moves the vechicle based on the key input and takes pictures by naming them based on key press.

Then after classifying the images manually, python train.py 0.001 100 is used to train the NN. The learning rate and hidden layer size are given as arguments.
A .pkl file is generated and stored in Optimized thethas folder. This is the object file which contains the NN.

Autonomous Run:
•	The weights generated after training is then transferred to the Raspberry Pi and assigned to the controlling neural net.
•	The camera feed (pictures taken at a rate of 5 frames per second) is programmed to be given as input to the controlling neural network.
•	The motor drivers on the vehicle are configured to receive input from the output of the controlling net, which will enable the vehicle to run.
•	The vehicle is then started and the neural network controls (drives) the vehicle according to the camera feed and parks itself in an available parking lot.

python autonomous.py executes the latest model in the optimized_thethas folder. This program autonomously guides the car to a vacant parking space.

Note: the images taken during training are 640 x 320, these are compressed to 100x100 while training the NN. Similarly, the input camera feed during autonomous run also compresses the image to 100x100 amd feeds it to the NN


