import os

white_list = [
]

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:

        if ".tex" in name:

            path = os.path.join(root, name)

            if white_list and name in white_list:
                os.system(f"aspell check {path}")
            
            if not white_list:
                os.system(f"aspell check {path}")
            
            
        


    