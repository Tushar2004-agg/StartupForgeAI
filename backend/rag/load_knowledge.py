import os

def load_knowledge():

    knowledge = ""

    data_folder = "data"

    for file in os.listdir(data_folder):

        if file.endswith(".txt"):

            with open(
                os.path.join(data_folder, file),
                "r",
                encoding="utf-8"
            ) as f:

                knowledge += f.read()
                knowledge += "\n\n"

    return knowledge