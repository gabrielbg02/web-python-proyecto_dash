from controller.user import User
data = {
    "firstname" : "raul",
    "lastname" : "jose",
    "username" : "soyraul",
    "country" : "ve",
    "password_user" : "33333"
}

user= User(data)
user.create_user()
