from hashtable import HashTable
import mmap

def open_target_phone_numbers(filename):
    """opens a file with phone numbers for testing"""
    target = ('data/'+filename)
    with open(target) as file:
        lines = [line.rstrip('\n') for line in open(target)]
    return lines

def get_costs(filename):
    """Takes cost and imports into hashtable"""
    f_name=('data/'+ filename)
    result = {}
    with open(f_name, "r+") as file:
        map = mmap.mmap(file.fileno(), 0)
        line = 0
        while line is not None:
            line = map.readline()
            values = line.split(b",")
            print(values)
            try:
                result[str(values[0])[2:-1]] = str(values[1])[2:-3].replace("\\", "")
            except:
                break
        return result


def cost_return(numbers, dic):
    """take in a phone number and return the costs based on
    the dictionary referance
        time complexity: O(n)"""
    results = []
    for num in numbers:
        for j in range(11, 0, -1):
            if num[:j] in dic:
                results.append(( num, dic.get(num[:j])))

    if len(results) == 0:
        print("Were sorry but these numbers cannot be found, please check the number and try again")
    return results


if __name__ == '__main__':
    numbers = open_target_phone_numbers("phone-numbers-10000.txt")
    dictionary = get_costs('route-costs-1000000.txt')
    print(dictionary)
    print(cost_return(numbers, dictionary))
