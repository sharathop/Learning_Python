message = 'Hello world'

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('world'))

print(len(message))

print(message[0:11])
print(message[::-1])

new_message=message.replace('Hello', 'Universe')

print(message)
print(new_message)

greet='Hello'
name='Python'
messages=greet + ' ' +  name

m='{},{}.Welcome!'.format(greet,name)
print(messages)
print(m)







first_name='Sharath'
Last_name='M'

full_name='{} {}'.format(first_name,Last_name)
print(full_name)


print(f"My name is {full_name}")

print(help(str))