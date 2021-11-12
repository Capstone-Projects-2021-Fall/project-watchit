import requests


#This class take the currently logged in user and find his details and make it available.
class LoggedInUser:
    def __init__(self, user):
        self.name = user['username']
        self.user = user

    #get user token, so we can access their db information
    def __getToken(self):
        login = requests.post("http://localhost:5000/login", json=self.user)
        loginDetails = login.json()
        userToken = loginDetails["token"]
        return userToken

    #this function returns videoID number found in the users db
    def __maxVideoID(self, videoArry):
        maxVideoIDCheck = 0
        for video in videoArry:  
            if video["videoID"] > maxVideoIDCheck:
                maxVideoIDCheck = video["videoID"]

        return maxVideoIDCheck   

    #this function makes an api call to get user videos
    def __getUserVideos(self):
        header = {"x-access-token": self.__getToken()}
        response = requests.get("http://localhost:5000/videos", headers=header)
        videos = response.json()
        return videos[0]  

    #function to call, to get max number for user videos
    def getMaxVideoIDNumber(self):
        return self.__maxVideoID(self.__getUserVideos())   

p = LoggedInUser({"username": "capstone", "password": "apple123"})

#print(p.name)
#print(p.getToken())

   
# to log the user in and get the token
user = {"username": "capstone", "password": "apple123"}
#print("user is " + user['username'])
login = requests.post("http://localhost:5000/login", json=user)
# view logins returned json
#print(login.json())
loginCreds = login.json()
t = loginCreds["token"]
#print(loginCreds["token"])


#r = requests.post("http://localhost:5000/login", json={"username": "capstone", "password": "apple123"})
#response = requests.get("http://localhost:5000/uu/capstone")
#y = json.dumps(response)
#video = json.loads(y)
#print(video['videos'])
# view logins returned json
header = {"x-access-token": t}
response = requests.get("http://localhost:5000/videos", headers=header)
h = response.json()
#print(h[0][4])