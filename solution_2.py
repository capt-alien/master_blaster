#!.py
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


if __name__ == '__main__':
   dictionary = get_costs('route-costs-106000.txt', 200000)
   numbers = open_target_phone_numbers("phone-numbers-1000.txt")
   print(cost_return(numbers, dictionary))
