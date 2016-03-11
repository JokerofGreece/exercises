import tweepy

consumer_key="T7G8F5PlsmRD4rT3W5QO1ylWv"
consumer_secret="uWDeax1VGMbLCB9gCiEQO7Cqv8wwXgcWOZjCdxzN3E7rpm5CLc"
access_token="707717663464751105-3uOJONBzrUhYY3DHQmjNIXVkAwwujKd"
access_token_secret="26zub7rIyIi6vTO8ISmJfPu3B4dGUe6PhpLBzENUM42WL"
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api =tweepy.API(auth)
user1 =api.get_user(raw_input("Enter the first twitter profile: "))
name1=user1.name
tweets1=user1.statuses_count
following1=user1.friends_count
followers1=user1.followers_count
likes1=user1.favourites_count
print "Profile @",
print name1,
print ", TWEETS",
print tweets1,
print ", FOLLOWING",
print following1,
print ", FOLLOWERS",
print followers1,
print ", LIKES",
print likes1


user2 =api.get_user(raw_input("Enter the second twitter profile: "))
name2=user2.name
tweets2=user2.statuses_count
following2=user2.friends_count
followers2=user2.followers_count
likes2=user2.favourites_count
print "Profile @",
print name2,
print ", TWEETS",
print tweets2,
print ", FOLLOWING",
print following2,
print ", FOLLOWERS",
print followers2,
print ", LIKES",
print likes2

score1=0
score2=0
if tweets1>tweets2:
	score1=score1 +1
elif tweets1<tweets2:
	score2=score2 +1
if following1>following2:
	score1=score1 +1
elif following1<following2:
	score2=score2 +1
if followers1>followers2:
	score1=score1 +1
elif followers1<followers2:
	score2=score2 +1
if likes1>likes2:
	score1=score1 +1
elif likes1<likes2:
	score2=score2 +1
print "THE FINAL SCORE IS",
print score1,
print "-",
print score2


