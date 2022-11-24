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

# FLZcode version 1.0 created by PFnove on YouTube
# Licensed under: MIT License (https://choosealicense.com/licenses/mit/)
# https://www.youtube.com/@pfnove3237

file_open = input("File to execute: ")
bits = int(input("Enter number of bits: "))
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

out = ""
ram0 = ""
ram1 = ""
ram2 = ""
ram3 = ""
for i in range(bits):
    ram0 += "0"
    ram1 += "0"
    ram2 += "0"
    ram3 += "0"
    out += "0"

def convert_dec(bin_in):
    return int(bin_in, 2)

def write(addr, value):
    global ram0, ram1, ram2, ram3, out
    value_w = limit_bin(value, bits)
    if addr == -1:
        out = value_w
    if addr == 0:
        ram0 = value_w
    if addr == 1:
        ram1 = value_w
    if addr == 2:
        ram2 = value_w
    if addr == 3:
        ram3 = value_w

def read(addr):
    if addr == 0:
        return ram0
    if addr == 1:
        return ram1
    if addr == 2:
        return ram2
    if addr == 3:
        return ram3

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

print("\nRunning emulation...")
for j in range(lines):
    main_func = ""
    alt_func = ""
    var0addr = 0
    var0type = ""
    var1addr = 0
    var1type = ""
    write_to = 0
    line = data[j]
    # Load a line
    if "debug" in line:
        main_func = "print"
    if "add" in line:
        main_func = "add"
    if "sub+0" in line:
        main_func = "invp0"
    if "sub+1" in line:
        main_func = "invp1"
    if "-out" in line:
        alt_func = "write"
        write_to = -1
    var_id = 0
    for i in range(len(line)):
        if line[i] == "i":
            if var_id == 0:
                var0addr = int(line[i+1])
                var0type = "input"
                var_id += 1
            else:
                var1addr = int(line[i+1])
                var1type = "input"
        if line[i] == "r" and line[i+1].isdigit():
            if var_id == 0:
                var0addr = int(line[i+1])
                var0type = "ram"
                var_id += 1
            else:
                var1addr = int(line[i+1])
                var1type = "ram"
        if line[i] == ">"  and line[i+1].isdigit():
            alt_func = "write"
            write_to = int(line[i+1])
    # Get correct variables
    var0 = "0"
    var1 = "0"
    if var0type == "input":
        if var0addr == 0:
            var0 = input0
        else:
            var0 = input1
    if var0type == "ram":
        var0 = read(var0addr)
    if var1type == "input":
        if var1addr == 0:
            var1 = input0
        else:
            var1 = input1
    if var1type == "ram":
        var1 = read(var1addr)
    # Execute loaded line
    result_tmp = None
    if main_func == "print":
        print("DEBUG:", var0)
    if main_func == "add":
        result_tmp = add(var0, var1)
    if main_func == "invp0":
        result_tmp = invert(var0)
    if main_func == "invp1":
        result_tmp = invertp1(var0)
    if alt_func == "write":
        if result_tmp == None:
            result_tmp = var0
        write(write_to, result_tmp)

print("\n", out, convert_dec(out))

print([ram0, ram1, ram2, ram3])

input("\nProgram finished!")