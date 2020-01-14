def increment(string):
    s = list(string)
    i = len(string) - 1
    nextletter = True
    while i >= 0 and nextletter:
        s[i] = chr((ord(s[i]) - 96) % 26 + 97)
        nextletter = s[i] == 'a'
        i = i - 1
    return "".join(s)

def check_string(string):
    cond1 = False
    cond2 = True
    cond3 = False
    pc = -1
    ppc = -1
    cond3_fc = -1
    counter = 0
    for c in string:
        i = ord(c)
        if c in ['i', 'o', 'l']:
            cond2 = False
            break
        if i == pc + 1 and pc == ppc + 1:
            cond1 = True
        elif not cond3 and i == pc:
            if cond3_fc != -1 and cond3_fc < counter - 1:
                cond3 = True
            else:
                cond3_fc = counter
        counter = counter + 1

        ppc = pc
        pc = i
    return cond1 and cond2 and cond3

def next_pass(string):
    string = increment(string)
    while(not check_string(string)):
        string = increment(string)
    return string
   
input = "hxbxwxba"
pass1 = next_pass(input)
pass2 = next_pass(pass1)
print("Pass 1:", pass1)
print("Pass 2:", pass2)
