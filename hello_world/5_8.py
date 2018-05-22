current_users = ['admin','anderson','eric','python','java']
# temp = sorted(current_users,reverse=True)
# print(temp)
user = input("Please enter your name: ")
# for user in current_users:
# if user=='admin':
#     print("Hello " + user + ", would you like to see a status report?")
# else:
#     print("Hello " + user + ", thank you for logging in again.")
if not user:
    user = input("Please enter your name!\nuser name: ")
    if user not in current_users:
        print("Hello " + user + ", please register first.")
    elif user == "admin":
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
