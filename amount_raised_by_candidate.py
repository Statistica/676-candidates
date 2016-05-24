# Written by Jonathan Saewitz, released May 24th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, plotly.plotly as plotly, plotly.graph_objs as go, requests
from collections import Counter
from bs4 import BeautifulSoup

candidates=[]

with open('presidential_candidates.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		c_id=row[15]
		html=requests.get('https://beta.fec.gov/data/candidate/' + c_id).text
		b=BeautifulSoup(html, 'html.parser')
		if len(b.find_all(class_='t-big-data'))==0:
			amt=0.0
		else:
			amt=float(b.find_all(class_="t-big-data")[0].text.strip().replace("$", "").replace(",", ""))
			#class "t-big-data" contains the money data
			#the 0th element contains the total receipts
			#.text gets only the text (i.e. amount raised)
			#.strip() removes all whitespace
			#.replace("$", "") removes the dollar sign	
			#.replace(",", "") removes all commas
			#we should be left with the total amount raised in the form 0.00
		name=row[14]
		candidates.append({'name': name, 'amount': amt})

candidates=sorted(candidates, key=lambda k: k['amount'])	

trace=go.Bar(
	x=[candidate['name'] for candidate in candidates],
	y=[candidate['amount'] for candidate in candidates]
)

layout=go.Layout(
	title="Presidential Candidates by Money Raised",
	xaxis=dict(
		title="Candidates",
	),
	yaxis=dict(
		title="Amount raised ($)",
	)
)

data=[trace]
fig=dict(data=data, layout=layout)
plotly.plot(fig)
