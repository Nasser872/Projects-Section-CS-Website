from Post import Post

all_posts_archive = []

def save_transmission():
   signal_content = input("Enter a transmission to store in the rebel database:\n")
   post = Post(sender_callsign,signal_content)
   all_posts_archive.append(post)
   print("Transmission added")

sender_callsign = input("What is your callsign?\n")

user_input = input(""" What would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")

while user_input not in ["add", "remove", "change user", "print", "quit"]:
   user_input = input("Please enter only one of the options\n")
while user_input != "quit":
   if user_input == "add":
       save_transmission()
       user_input = input(""" \nWhat would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")
       while user_input not in ["add", "remove", "change user", "print", "quit"]:
           user_input = input("Please enter only one of the options\n")
   if user_input == "remove":
       for post in all_posts_archive:
           print(post)
       remove_input = input("Which transmission would you like to remove? Enter a number for the one you want to remove\n")
       if int(remove_input) > len(all_posts_archive):
           remove_input = input("Please enter a number within the database's length\n")
       index = int(remove_input) - 1
       del all_posts_archive[index]
       print("Transmission removed\n")
       user_input = input(""" What would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")
       while user_input not in ["add", "remove", "change user", "print", "quit"]:
           user_input = input("Please enter only one of the options\n")
   if user_input == "change user":
       sender_callsign = input("Please enter a new callsign that will be used for future transmissions\n")
       user_input = input(""" \nWhat would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")
       while user_input not in ["add", "remove", "change user", "print", "quit"]:
           user_input = input("Please enter only one of the options\n")
   if user_input == "print":
       if all_posts_archive == []:
           print("There is nothing in the database currently\n")
           user_input = input(""" What would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")
       while user_input not in ["add", "remove", "change user", "print", "quit"]:
           user_input = input("Please enter only one of the options\n")
       else:
           for eachPost in all_posts_archive:
               print(eachPost)
           user_input = input(""" \nWhat would you like to do?\n
"add" - Add a transmission to the rebel archive\n
"remove" - Remove a transmission from the rebel archive\n
"change user" - Change the call sign associated with any future transmissions\n
"print" - Display the current up to date list of all transmissions\n
"quit" - End the program\n
""")
       while user_input not in ["add", "remove", "change user", "print", "quit"]:
           user_input = input("Please enter only one of the options\n")