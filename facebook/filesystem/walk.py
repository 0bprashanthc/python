import os

for file in os.walk('/'):
    print(file)
    print(os.path.isfile(file))
    print(os.path.exists(file))
    os.makedirs("test-python")
    break
