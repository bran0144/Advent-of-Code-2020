with open('passwords.txt') as file:
    password_list = [line.strip() for line in file]

sample = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

# lowest to most number of times letter can be in passwords

def password_check(plist):
    total_count = 0
    
    for str in plist:
        str.split()
        times = str.split('-')
        low_num = int(times[0])
        split_num = times[1].split()
        high_num = int(split_num[0])
        almost_letter = split_num[1].split(':')
        letter = almost_letter[0]
        password = split_num[2]
        letter_count = password.count(letter)
        if letter_count >= low_num and letter_count <= high_num:
            total_count +=1
    return print(total_count)
            

# password_check(password_list)

def password_check_specific(plist):
    total_count = 0
    
    for str in plist:
        str.split()
        times = str.split('-')
        low_num = int(times[0])
        split_num = times[1].split()
        high_num = int(split_num[0])
        almost_letter = split_num[1].split(':')
        letter = almost_letter[0]
        password = split_num[2]
        if letter == password[low_num-1] and password[high_num-1]:
            continue
        elif letter == password[low_num-1] or password[high_num-1]:
            total_count +=1
        
    return print(total_count)

password_check_specific(password_list)