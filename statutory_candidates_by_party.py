# Written by Jonathan Saewitz, released May 24th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, plotly.plotly as plotly
from collections import Counter

c=Counter()

with open('presidential_candidates.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the headers row
	for row in reader: #loop through the candidates
		if row[1]=='C': #row[1] is the candidate's status; C means Statutory Candidate
			party=row[12] #row[12] is the candidate's political party
			c[party]+=1

fig = {
	'data': [{
		'labels': c.keys(),
		'values': c.values(),
		'type': 'pie'
	}],
	'layout': {'title': '2016 US Statutory Presidential Candidates\' Party Affiliation'}
}

plotly.plot(fig)
