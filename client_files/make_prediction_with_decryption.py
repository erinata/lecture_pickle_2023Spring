import pickle
import pandas

from cryptography.fernet import Fernet
import base64

password = b'12345678123456781234567812345678'
key = base64.urlsafe_b64encode(password)
fkey = Fernet(key)


with open("encrypted_machine.pickle", "rb") as file:
  encrypted_machine = pickle.load(file)
  
decrypted_machine = fkey.decrypt(encrypted_machine)

machine = pickle.loads(decrypted_machine)


new_survey = pandas.read_csv("new_survey.csv")
new_survey = new_survey.values

print(machine.predict(new_survey))

