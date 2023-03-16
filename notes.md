





Without encryption

private files
private_dataset.csv  ->  machine -> machine.pickle


client files
machine.pickle -> machine  -> prediction



With encryption

private files
private_dataset.csv  ->  machine -> serialized_machine -> encrypted_machine -> encrypted_machine.pickle

client files
encrypted_machine.pickle -> encrypted_machine -> decrypted_machine -> machine -> prediction
