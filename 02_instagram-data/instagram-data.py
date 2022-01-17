from datetime import datetime
import instaloader

loader = instaloader.Instaloader()

instaUsername = 'INSTAGRAM_USERNAME'
instaPassword = 'INSTAGRAM_PASSWORD'

loader.login(instaUsername, instaPassword)

profile = instaloader.Profile.from_username(loader.context, instaUsername)

followers = profile.get_followers()

followees = profile.get_followees()

isPrivate = profile.is_private

biography = profile.biography

print('Username: ' + instaUsername + '\n')
print('Bio: ' + biography + '\n')

print('Private account: ')
print(isPrivate)

print('Followers: ' + str(followers._data['count']))
print('\n')

print('Followees: ' + str(followees._data['count']))
print('\n')

print('Followers list: ' + '\n')
for follower in followers:
    print(follower)    

print('\n')
print('Followees list: ' + '\n')
for follower in followees:
    print(follower)

print('\n')
