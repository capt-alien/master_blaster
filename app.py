from hashtable import HashTable


def open_target_phone_numbers(filename):
    """opens a file with phone numbers for testing"""
    target = ('data/'+filename)
    with open(target) as file:
        lines = [line.rstrip('\n') for line in open(target)]
    return lines

def get_costs(filename, size):
    """Takes cost and imports into hashtable"""
    prefix_cost = HashTable(size)
    f_name=('data/'+ filename)
    with open(f_name) as file:
        lines = [line.rstrip('\n') for line in open(f_name)]
        for i in lines:
            i = i.split(',')
            prefix_cost.set(i[0], i[1])
        #parse lines into a hashtable
        return prefix_cost

# def _read_routes(self, file_name):
#     """Read route costs file into a dictionary and return the result.
#     Runtime: Θ(n) Space: Θ(n)"""
#     data = {}
#     with open('data/' + file_name) as f:
#         for line in f:
#             row = line.strip().split(',')
#             # if the route is already in dictionary
#             # and the current route has a lower price,
#             # or if the route is not in dictionary
#             if (row[0] in data and data[row[0]] > row[1]) or (row[0] not in data):
#                 if row[0] not in data:
#                     self.route_costs += 1
#                 # update/insert the route cost
#                 data[row[0]] = row[1]
#     return data


def cost_return(numbers, hashtable):
    """take in a phone number and return the costs based on
    the dictionary referance
        time complexity: O(n)"""
    results = []
    for num in numbers:
        for j in range(11, 0, -1):
            if hashtable.contains(num[:j]):
                results.append(( num, hashtable.get(num[:j])))

    if len(results) == 0:
        print("Were sorry but these numbers cannot be found, please check the number and try again")
    return results

# def tester_loop(phone_number):
#     for j in range(11, 0, -1):
#         print(phone_number[:j])

if __name__ == '__main__':
    dictionary = get_costs('route-costs-106000.txt', 200000)
    numbers = open_target_phone_numbers("phone-numbers-1000.txt")
    print(cost_return(numbers, dictionary))
