import pickle as pc
with open('model_2018-03-22_11-54-37_l0.001_h100.pkl', 'rb') as mod:
        model=pc.load(mod)
thetas=model['optimized_theta']
hidden_layer_size=model['hidden_layer_size']
input_layer_size=10000
number_of_labels=5
theta1_params=thetas[0: (hidden_layer_size * (input_layer_size+1))]
theta2_params=thetas[hidden_layer_size * (input_layer_size+1) :]
theta1=theta1_params.reshape(hidden_layer_size, (input_layer_size+1))
theta2=theta2_params.reshape(number_of_labels, hidden_layer_size+1)                        
print'input layer size= ', input_layer_size                   
print'hidden layer size= ', hidden_layer_size
print'number of labels = ',number_of_labels
print('theta 1 values')
print(theta1)
print('theta 2 values')
print(theta2)
