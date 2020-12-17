['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',

'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929', 
'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', 
'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"']

passports = open('passport.txt').read()
passports = passports.split("\n\n")
passport_list = []
for passport in passports:
    passport_list.append([item for item in passport.split()])
passport_dicts=[]
for p in passport_list:
    temp = { item.split(":")[0]:item.split(":")[1] for item in p} 
    temp.pop('cid',None)
    passport_dicts.append(temp)

valid_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

valid_passports = [set(x.keys()) == valid_fields for x in passport_dicts]
print(valid_passports.count(True))




