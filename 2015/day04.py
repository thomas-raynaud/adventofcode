import hashlib

input = 'yzbqklnj'
adventcoin_found_step1 = False
adventcoin_found_step2 = False
adventcoin = 0
while(adventcoin_found_step1 == False or adventcoin_found_step2 == False):
    new_str = input + str(adventcoin)
    new_str = new_str.encode('utf-8')
    hash = hashlib.md5(new_str).hexdigest()
    if(hash[:5] == '00000' and not adventcoin_found_step1):
        adventcoin_found_step1 = True
        print('Step 1: ', adventcoin)
    if(hash[:6] == '000000'):
        adventcoin_found_step2 = True
        print('Step 2:', adventcoin)
    adventcoin += 1
