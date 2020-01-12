def decode_instructions(input, variables):
    # Get the instructions
    for instr in input:
        instr_sp = instr.split()
        if len(instr_sp) == 3:
            if instr_sp[2] in variables:
                continue
            if instr_sp[0].isdigit():
                variables[instr_sp[2]] = int(instr_sp[0])
            else:
                instructions.append(["", instr_sp[0], -1, instr_sp[2]])
        else:
            # Instruction format: gate param1 param2 result
            instr_f = []
            if instr_sp[0] == "NOT":
                instr_f = [instr_sp[0], instr_sp[1], -1, instr_sp[3]]
            else:
                params = [instr_sp[0], instr_sp[2]]
                p1, p2 = [int(x) if x.isdigit() else x for x in params]
                instr_f = [instr_sp[1], p1, p2, instr_sp[4]]
            instructions.append(instr_f)

    # Solve the instructions
    while len(instructions) > 0:
        i = 0
        while i < len(instructions):
            instr = instructions[i]
            # Solve instructions if params are known
            params = [instr[1], instr[2]]
            p1_known, p2_known = [x in variables or isinstance(x, int) for x in params]
            res_known = instr[3] in variables
            if p1_known and p2_known and not res_known:
                gate = instr[0]
                p1, p2 = [variables[x] if not isinstance(x, int) else x for x in params]
                res = -1
                if gate == "NOT":
                    res = p1 ^ 65535
                elif gate == "AND":
                    res = p1 & p2
                elif gate == "OR":
                    res = p1 | p2
                elif gate == "RSHIFT":
                    res = p1 >> p2
                elif gate == "LSHIFT":
                    res = p1 << p2
                else:
                    res = p1
                variables[instr[3]] = res
                del instructions[i]
            else:
                i = i + 1

input = open("input.txt", "r")

instructions = []
variables = dict()
decode_instructions(input, variables)

input.seek(0)
a = variables["a"]
variables.clear()
variables["b"] = a

decode_instructions(input, variables)
print(variables)
print("a: ", variables["a"])
input.close()
