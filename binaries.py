ip = "10.20.12.45"
binaries = [128, 64, 32, 16, 8, 4, 2, 1]
bin_nums = ip.split(".")


def octo(base):
    octetos = []
    temp = 0
    for num in binaries:
        if base >= num:
            temp += num
            if temp > base:
                octetos.append(0)
                temp -= num
            else:
                octetos.append(1)
        else:
            octetos.append(0)

    return octetos


oct = []
for x in bin_nums:
    oct.append(octo(int(x)))

for octeto in oct:
    print(octeto)
# print(f"zero one: {octetos}")
