# -*- coding: utf-8 -*-
# Written by Jonathan Saewitz, released May 24th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, plotly.plotly as plotly, plotly.graph_objs as go, requests
from collections import Counter
from bs4 import BeautifulSoup

#the following candidates raised $100,000 or more (from https://github.com/Statistica/676-candidates/blob/master/amount_raised_by_candidate.py):
candidates=["QUARTEY, MARY AKU",
"LAWSON, EDGAR A",
"GILMORE, JAMES S III",
"STEIN, JILL",
"JOHNSON, GARY",
"CHAFEE, LINCOLN DAVENPORT MR.",
"EVERSON, MARK",
"PATAKI, GEORGE E",
"WEBB, JAMES",
"WILSON, WILLIE",
"PERRY, JAMES R (RICK)",
"JINDAL, BOBBY",
"SANTORUM, RICHARD J.",
"HUCKABEE, MIKE",
"WILLIAMS, ELAINE WHIGHAM",
"GRAHAM, LINDSEY O",
"O'MALLEY, MARTIN JOSEPH",
"DE  LA  FUENTE, ROQUE ROCKY",
"WALKER, SCOTT",
"CHRISTIE, CHRISTOPHER J",
"FIORINA, CARLY",
"PAUL, RAND",
"KASICH, JOHN R",
"BUSH, JEB",
"RUBIO, MARCO",
"TRUMP, DONALD J",
"CARSON, BENJAMIN S SR MD",
"CRUZ, RAFAEL EDWARD \"TED\"",
"SANDERS, BERNARD",
"CLINTON, HILLARY RODHAM"
]

c=Counter()

with open('presidential_candidates.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the headers row
	for row in reader: #loop through the candidates
		if row[14] in candidates: #row[14] is the candidate's name
								  #checks if the current candidate we're looping through is one the candidates listed above
			party=row[12]
			c[party]+=1

fig = {
	'data': [{
		'labels': c.keys(),
		'values': c.values(),
		'type': 'pie'
	}],
	'layout': {'title': '2016 US Presidential Candidates\' Party Affiliation (only candidates who raised ≥$100,000)'}
}

plotly.plot(fig)
