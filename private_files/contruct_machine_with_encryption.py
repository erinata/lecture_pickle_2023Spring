import pandas
from sklearn.ensemble import RandomForestClassifier

import pickle

from cryptography.fernet import Fernet
import base64

password = b'12345678123456781234567812345678'
key = base64.urlsafe_b64encode(password)
fkey = Fernet(key)



dataset = pandas.read_csv("private_dataset.csv")

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

machine = RandomForestClassifier(n_estimators=11, criterion="gini", max_depth=10, random_state=1)
machine.fit(data, target)

serialized_machine = pickle.dumps(machine)
encrypted_machine = fkey.encrypt(serialized_machine)

with open("encrypted_machine.pickle", "wb") as file:
  pickle.dump(encrypted_machine, file)
  
  
  
  