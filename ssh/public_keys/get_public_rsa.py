import os

def find_pub_keys(directory):
    keys = []
    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            keys.extend(find_pub_keys(os.path.join(directory, file)))
        elif file.endswith(".pub"):
            keys.append(os.path.join(directory, file))

    return keys

keys = find_pub_keys(".")
keys = [key for key in keys if "rsa" in key]
with open("public_rsa_keys.txt", "w") as f:
    for key_file in keys:
        with open(key_file, "r") as key:
            f.write(key.read())
