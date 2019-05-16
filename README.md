Team Master Blaster: Call Routing Solutions:

*********Scenario 1: One-time route cost check*********************
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?
*******************************************************************

2 methods for finding the number:

1) CTRL F: to search for the number directly. If the full number does not return anything, delete the last character in the string and try again.

2) Use the grep command in the terminal.
        ex: in terminal type:
            $ grep '+15323824' data/route-costs-1000000.txt

            then if nothing is returned truncate the last character in the string and try again

***************Scenario 2: List of route costs to check*********************
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers. How can you operationalize the route cost lookup problem?
*******************************************************************

Solution: run the solution2_py file in terminal with:
$python3 solution_2.py

***********Scenario 3: Multiple long carrier route lists********************
You have 5 carrier route lists, each with 10,000,000 (10M) entries (in arbitrary order) and a list of 10,000 phone numbers. How can you speed up your route cost lookup solution to handle this larger dataset?
*****************************************************************************

3) for this solution we used an mmap type of hash table to more easily open the files. To see this solution run the routeing.py file.

$python3 routeing.py

****************Scenario 4: High-throughput pricing API**********************
You have 5 carrier route lists, each with 10,000,000 (10M) entries (in arbitrary order) and you want to create a web-service API to allow clients to price a call before it is initiated. How can you create an efficient route cost lookup solution that can handle high spikes of traffic (up to 10,000 requests per minute) without overloading your API servers?
*****************************************************************************

At the time I am writing this, We haven't gotten our flask app to work yet.
I will try to get it working at some point, but given my lack of time
before grading do not be surprised if you don't see a flask API for this
project. I do plan on revisiting this and making it work at some point.  
