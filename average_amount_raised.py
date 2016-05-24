# Written by Jonathan Saewitz, released May 24th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)
import csv, numpy

amount=0
amounts=[]

num_candidates=0
num_candidates_greater_than_0=0

with open('candidates_and_money_raised.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the headers row
	for row in reader: #loop through the candidates
		amount+=float(row[1]) #row[1] is the amount raised
		num_candidates+=1
		if float(row[1])>0:
			amounts.append(float(row[1]))
			num_candidates_greater_than_0+=1

print "Total amount raised: $", "{:,}".format(amount) #"{:,}" makes it comma-separated
print "Average amount raised: $", "{:,}".format(amount/num_candidates)
print "Average amount raised by candidates who raised >$0: $", "{:,}".format(amount/num_candidates_greater_than_0)

print "The median amount raised was $", "{:,}".format(numpy.median(numpy.array(amounts)))

#prints out:
#Total amount raised: $ 743,035,255.9
#Average amount raised: $ 1,099,164.57973
#Average amount raised by candidates who raised >$0: $ 7,505,406.62525
#The median amount raised was $ 10,061.0
