"""
MIT License

Copyright (c) 2022 Peter F.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# FLZcode version 2.1 created by PFnove on YouTube
# Licensed under: MIT License (https://choosealicense.com/licenses/mit/)
# https://www.youtube.com/@pfnove3237

import sys, time

print("""
      dMMMMMP dMP     dMMMMMP .aMMMb  .aMMMb  dMMMMb  dMMMMMP 
     dMP     dMP       .dMP" dMP"VMP dMP"dMP dMP VMP dMP      
    dMMMP   dMP      .dMP"  dMP     dMP dMP dMP dMP dMMMP     
   dMP     dMP     .dMP"   dMP.aMP dMP.aMP dMP.aMP dMP        
  dMP     dMMMMMP dMMMMMP  VMMMP"  VMMMP" dMMMMP" dMMMMMP     
""")

try:
    file_open = sys.argv[1]
except:
    file_open = input("File to execute: ")
try:
    bits = sys.argv[2]
    ram_size = sys.argv[3]
except:
    bits = int(input("Enter number of bits: "))
    ram_size = int(input("Enter max ram size:   "))
file = open(file_open, "r")
file_data = file.read().lower()
file.close()

first_cyc = True
data = []
lines = 0
for i in range(len(file_data)):
    if first_cyc:
        line = ""
    first_cyc = False
    if not file_data[i] == "\n":
        line = line + file_data[i]
    elif line != "":
        data.append(line)
        line = ""
        lines += 1

ram = []
for i in range(ram_size):
    ram.append("")
out = ""
for i in range(bits):
    for j in range(len(ram)):
        ram[j] += "0"
    out += "0"

def convert_dec(bin_in):
    return int(bin_in, 2)

def write(addr, value):
    try:
        global ram, out
        value_w = limit_bin(value, bits)
        if addr == -1:
            out = value_w
        else:
            ram[addr] = value_w
    except:
        print(f"Error while writing to:   ADDR {addr}")

def read(addr):
    try:
        return ram[addr]
    except:
        print(f"Error while reading from: ADDR {addr}")
        temp_val = ""
        for i in range(bits):
            temp_val += "0"
        return temp_val

def limit_bin(bin_in, bits):
    out = ""
    for i in range(-bits, 0):
        try:
            out += bin_in[i]
        except:
            out += "0"
    return out

def add(in0, in1):
    in0_dec = int(in0, 2)
    in1_dec = int(in1, 2)
    out = in0_dec + in1_dec
    return_out = bin(out).replace("0b", "")
    return limit_bin(return_out, bits)

def invert(bin_in):
    out = ""
    tmp = ""
    for i in range(len(bin_in)):
        if bin_in[i] == "0":
            tmp = tmp + "1"
        else:
            tmp = tmp + "0"
    return limit_bin(tmp, bits)

def invertp1(bin_in):
    out = ""
    tmp = ""
    for i in range(len(bin_in)):
        if bin_in[i] == "0":
            tmp = tmp + "1"
        else:
            tmp = tmp + "0"
    return add(tmp, "1")

print("")
input0 = limit_bin(input(f"Enter IN0 ({bits}bit): "), bits)
input1 = limit_bin(input(f"Enter IN1 ({bits}bit): "), bits)
print("")
print("IN0:", convert_dec(input0), " (decimal)")
print("IN1:", convert_dec(input1), " (decimal)")

print("\nRunning emulation...")
start_time = time.perf_counter()
one_in_funcs = ["print", "invp1", "invp2", "goto"]
j = 0
while j < lines:
    main_func = ""
    alt_func = ""
    alt_func_data = ""
    write_enab = False
    write_to = 0
    varaddrs = ["0", "0", "0", "0"]
    vartypes = ["const", "const", "const", "const"]
    line = data[j]
    # Load a line
    if "debug" in line:
        main_func = "print"
    if "add" in line:
        main_func = "add"
    if "sub+0" in line:
        main_func = "inv"
    if "sub+1" in line:
        main_func = "invp1"
    if "goto" in line:
        main_func = "goto"
    if "if" in line:
        alt_func = "if"
    if "-out" in line:
        write_enab = True
        write_to = -1
    var_id = 0
    for i in range(len(line)):
        if main_func in one_in_funcs and var_id == 1:
            var_id = 2
        if line[i] == "i" and line[i+1].isdigit():
            varaddrs[var_id] = int(line[i+1])
            vartypes[var_id] = "input"
            var_id += 1
        if line[i] == "r" and line[i+1].isdigit():
            temp_val = ""
            valid_in = True
            for l in range(len(line)):
                if l > i:
                    if line[l].isdigit() and valid_in:
                        temp_val += line[l]
                    else:
                        valid_in = False
            varaddrs[var_id] = int(temp_val)
            vartypes[var_id] = "ram"
            var_id += 1
        if line[i] == "c" and line[i+1].isdigit():
            temp_val = ""
            valid_in = True
            for l in range(len(line)):
                if l > i:
                    if (line[l] == "0" or line[l] == "1") and valid_in:
                        temp_val += line[l]
                    else:
                        valid_in = False
            varaddrs[var_id] = limit_bin(temp_val, bits)
            vartypes[var_id] = "const"
            var_id += 1
        if line[i] == ">"  and line[i+1].isdigit():
            temp_val = ""
            valid_in = True
            for l in range(len(line)):
                if l > i:
                    if line[l].isdigit() and valid_in:
                        temp_val += line[l]
                    else:
                        valid_in = False
            write_enab = True
            write_to = int(temp_val)
        elif line[i] == ">" and alt_func == "if":
            alt_func_data = "higher"
        if line[i] == "<" and alt_func == "if":
            alt_func_data = "lower"
        if line[i] == "=" and alt_func == "if":
            if line[i-1] == ">":
                alt_func_data = "highereq"
            elif line[i-1] == "<":
                alt_func_data = "lowereq"
            else:
                alt_func_data = "equal"
    if "//" in line:
        main_func = ""
        alt_func = ""
        alt_func_data = ""
        write_enab = False
    # Get correct variables
    for i in range(len(varaddrs)):
        if vartypes[i] == "input":
            if varaddrs[i] == 0:
                varaddrs[i] = input0
            else:
                varaddrs[i] = input1
            vartypes[i] = "input_old"
        if vartypes[i] == "ram":
            varaddrs[i] = read(varaddrs[i])
            vartypes[i] = "ram_old"
    # Execute loaded line
    result_tmp = None
    condition_pass = True
    if alt_func == "if":
        condition_pass = False
        if alt_func_data == "equal" and int(varaddrs[2], 2) == int(varaddrs[3], 2):
            condition_pass = True
        if alt_func_data == "higher" and int(varaddrs[2], 2) > int(varaddrs[3], 2):
            condition_pass = True
        if alt_func_data == "lower" and int(varaddrs[2], 2) < int(varaddrs[3], 2):
            condition_pass = True
        if alt_func_data == "highereq" and int(varaddrs[2], 2) >= int(varaddrs[3], 2):
            condition_pass = True
        if alt_func_data == "lowereq" and int(varaddrs[2], 2) <= int(varaddrs[3], 2):
            condition_pass = True
    if condition_pass:
        if main_func == "print":
            print("DEBUG:", varaddrs[0], convert_dec(varaddrs[0]))
        if main_func == "add":
            result_tmp = add(varaddrs[0], varaddrs[1])
        if main_func == "inv":
            result_tmp = invert(varaddrs[0])
        if main_func == "invp1":
            result_tmp = invertp1(varaddrs[0])
        if main_func == "goto":
            j = convert_dec(varaddrs[0])-1
        if write_enab:
            if result_tmp == None:
                result_tmp = varaddrs[0]
            write(write_to, result_tmp)
    j += 1
finish_time = time.perf_counter()
print(f"Finished in {finish_time-start_time} seconds")

print("\n", out, convert_dec(out))

print("\nRAM DUMP:\n")
if ram_size == 0:
    print("No ram!")
ram_char_lenght = len(str(ram_size))
for i in range(len(ram)):
    string = ""
    for j in range(ram_char_lenght - len(str(i))):
        string += " "
    print(f"RAM VALUE {string}{i} : {ram[i]} - {convert_dec(ram[i])}")

print("\nProgram finished", end="")
while True:
    _ = 0