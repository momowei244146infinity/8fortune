import os
import shutil
import pandas as pd
 
#folder_path = os.getcwd()
#print(folder_path)
#absolute_path = os.path.abspath(folder_path)
#p2 = os.path.abspath("./8fortune/users")
#print(p2)
#shutil.rmtree(absolute_path)
#df = pd.DataFrame(columns=["username", "password"])


#folder_list = os.listdir(p2)
#if len(folder_list) == 0:
#    new_folder_name = 'user1'
#    new_folder_path = os.path.join(p2, 'user1')
#    os.mkdir(new_folder_path)
#    df.loc[len(df)] = ["user1", "pass123"]
#    df.to_csv("./8fortune/users/user1/user1.csv", index=False)
#folders = [name for name in os.listdir(absolute_path) ]

#print(os.listdir(absolute_path))


"""
print(os.getcwd())
print(os.path.abspath("./users"))
print(os.listdir(os.path.abspath("./users")))

#df = pd.DataFrame(columns=["username", "password"])
#df.to_csv("username password.csv", index=False)

df = pd.read_csv("username password.csv", delimiter=",")
df.loc[len(df)] = ["user1", "pass123"]
df.to_csv("username password.csv", index=False)
"""

"""

if len(os.listdir(os.path.abspath("./users"))) == 0:
    
    new_user = "user1"
    new_folder_name = new_user
    new_folder_path = os.path.join(os.path.abspath("./users"), new_folder_name)
    os.mkdir(new_folder_path)
    df = pd.read_csv("username password.csv")
    df.loc[len(df)] = [new_user, "pass123"]
    df.to_csv("username password.csv", index=False)

"""
df = pd.read_csv("username password.csv", delimiter=",")
idx = df['username'] == "user3"
correct_password = df.loc[idx, "password"].values[0]


           
print(repr(correct_password))
print(str(correct_password) == "12345678")




