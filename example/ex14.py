from sys import argv

script,user_name = argv

prompt = '>'

print('Hi{},I\'m the {} script'.format(user_name,script))
print('I\'d like to ask you some questions')
print('Do you like me %s?' % user_name)
likes = input(prompt)
print('Where do you live {}?'.format(user_name))
lives = input(prompt)
print('What kind of computer do you have {}'.format(user_name))
computer = input(prompt)

print('''
Alright,so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer, Nice.
'''.format(likes,lives,computer))