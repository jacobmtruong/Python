
# Assignment: User
# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age

# Also include default attributes:
# is_rewards_member - default value of False
# gold_card_points = 0

# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.


class user:
    def __init__(self, firts_name, last_name, email, age):
        self.first_name = firts_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

# Methods:

# display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print(f"This is {self.last_name} {self.first_name} details")
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"is a reward member? {self.is_reward_member}")
        print(f"card points: {self.gold_card_points}")

# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        self.is_reward_member = True
        print(f"reward member status {self.is_reward_member}")
        print(f"{self.first_name} is now a reward member")
        self.gold_card_points = 200
        print(f"The points of {self.first_name} is now {self.gold_card_points}")


# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

    def spend_point(self, amount):
        self.gold_card_points -= amount
        print(f"{self.first_name} used {amount} points")
        print(f"{self.first_name}'s point left is {self.gold_card_points}.")


# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.

    def re_enroll(self):
        if self.is_reward_member == True:
            print(f"{self.first_name} is already a reward member.")
            self.is_reward_member = False
        else:
            self.is_reward_member = True
            print(f"{self.first_name} reward member status: {self.is_reward_member}")
            print(f"{self.first_name} is now a reward member")
            self.gold_card_points = 200
            print(f"The points of {self.first_name} is now {self.gold_card_points}")


# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.

    def spend_point2(self,amount):
        if self.gold_card_points < amount:
            print(f"You don't enough points to spend, your current point is {self.gold_card_points}.")
        else:
            self.gold_card_points -= amount
            print(f"{self.first_name} used {amount} points.")
            print(f"{self.first_name}'s point left is {self.gold_card_points}.")



# test:

Jacob = user("Jacob", "Truong", "jacob@dojo.com", 27)


Jacob.display_info()
Jacob.enroll()
Jacob.re_enroll()
Jacob.spend_point(8)
Jacob.spend_point2(200)


# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
