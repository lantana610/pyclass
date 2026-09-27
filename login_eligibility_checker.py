age = int(input('enter your age:'))
has_id = input('enter your ID? (yes/no):')

if age >= 18 and has_id.lower() == 'yes':
    print('granted access')
else:
    print('access denied')  

# bonus challenge 

is_admin = input('are you a admin?:')
is_moderator = input('are you a moderator?:')

if is_admin  == 'yes' or is_moderator == 'yes':
    print('you can manage the platform')
else:
    print('standard user access')    

