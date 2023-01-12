def seperation(n): # seperates extension and name
    s = n.split(sep=".") 
    filename,extension = s[0],s[1]

    return filename,extension

def store(filename_withextension:str,data): # writes according to extension
    import json
    import pickle
    
    filename,extension = seperation(filename_withextension)
    if extension == "json":    
        with open(f'{filename}.json','w') as file:
            json.dump(data,file)
    elif extension == "txt":    
        with open(f'{filename}.txt','w') as file:
            for line in data:
                file.writelines(line)
    else:
        with open(filename_withextension,'wb') as file:
            pickle.dump(data,file)

def extract(filename_withextension:str): # extracts data from file and rueturns it
    import json
    import pickle
    
    filename,extension = seperation(filename_withextension)
    if extension == "json":    
        with open(f'{filename}.json','r') as file:
            return json.load(file)
    elif extension == "txt":    
        with open(f'{filename}.txt','r') as file:
                return file.read()
    else:
        with open(filename_withextension,'rb') as file:
            return pickle.load(file)

