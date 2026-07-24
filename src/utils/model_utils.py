import pickle

def save_model(model,path):
    with open(path,'wb') as file:
        pickle.dump(model,file)

def load_model(path):
    with open(path,"rb") as file:
        model=pickle.load(file)

    return model