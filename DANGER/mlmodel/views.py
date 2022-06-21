import pickle
filename = 'random_forest'

# load the model
loaded_model = pickle.load(open(filename, 'rb'))
result =loaded_model.predict([[1,0,1,1]])
print(result)