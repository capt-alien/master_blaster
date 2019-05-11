from hashtable import HashTable


def open_target_phone_numbers(filename):
    """opens a file with phone numbers for testing"""
    with open(filename) as file:
        lines = file.read()
    return lines

def get_costs(filename):
    """Takes cost and imports into hashtable"""
    prefix_cost = HashTable()
    with open('data/'filename) as file:
        lines = [line.rstrip('\n') for line in open('filename')]
        for i in lines:
            i = i.split(',')
            prefix_cost.set(i[0], i[1])
        #parse lines into a hashtable
        return prefix_cost

def cost_return(numbers, hashtable):
    """take in a phone number and return the costs based on
    the dictionary referance"""
    results = []
    for i in numbers:
        for j in reverse(range(9)):
            if hashtable.contains(i[:j]):
                results.append(hashtable.get(i))


if __name__ == '__main__':
    get_costs('route-costs-10.txt')
    dictionary = get_dictionary("route-costs-4.txt")
    numbers = open_phone_numbers("phone-numbers-3.txt")
    print(cost_return(numbers, dictionary))
