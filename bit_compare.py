def convert_binary(num):
    return '{0:08b}'.format(num)


def bit_compare(line):
    nums = line.split(",")
    a = str(convert_binary(int(nums[0])))
    print(a)
    b = int(nums[1])
    print(b)
    c = int(nums[2])
    print(c)
    if int(a[-b]) == int(a[-c]):
        return True
    else:
        return False

#  if __name__ == 'main':
test_cases = ["212294,3,17", "548230,11,15", "445542,5,15", "837199,3,20",
              "390036,8,15", "156629,2,16", "988123,6,11", "914762,2,8",
              "885310,17,20", "992115,14,19", "556121,3,5", "639151,6,20",
              "661893,14,20", "397276,1,19", "972354,18,18", "139449,1,13",
              "506567,11,11", "880994,5,9", "805743,1,13", "899269,17,19"]
# open(sys.argv[1], 'r')
for test in test_cases:
    print(test)
    print(bit_compare(test))
#  test_cases.close()
