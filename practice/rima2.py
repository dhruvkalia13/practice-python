"""
unstrcutured log parsing
"""

import re
domain = "organisation2.com"
logs = ["user1@organisation1.com20180910",
        "user3@organisation1.com20180912",
        "user4@organisation1.com20180912",
        "user2@organisation2.com20180912",
        "user2@organisation1.com20180911",
        "user4@organisation2.com20180912",
        "user5@organisation2.com20180910",
        "user6@organisation2.com20180910",
        "user2@organisation1.com20180910",
    "user2"
    "organisation1.com20180910",
    "20180910",
        ]
from collections import Counter, defaultdict
dateCounter = Counter()
domainToDateCounterMap = defaultdict(Counter)

"""
strip()
'  ishan  '
'ishan'

'ish     aaan guliani     '
'ish     aaan guliani'
"""

"""
split - returns a list
"""

"""
string()
""""""
''''''
"""

"""
ishanguliani.coma


Regular expressions
+ at least 1
* greedy
? 0/1
{m,n} inclusive

"""




regexForDomain = "[http|https]?(\:\/\/)?(www)?[a-zA-Z1-9]+(\.[a-z]{2,3})"
for log in logs:
    extracted_user, extracted_domainWithDate = log.strip().split('@')
    extracted_date = re.split(regexForDomain, extracted_domainWithDate.strip())[-1]
    dateStartIndex = extracted_domainWithDate.find(extracted_date)
    extracted_domain = extracted_domainWithDate[:dateStartIndex]
    domainToDateCounterMap[extracted_domain][extracted_date] += 1

import sys
dayWithMaxEntries = 0
numberOfMaxEntries = -sys.maxsize
for date, count in domainToDateCounterMap[domain].items():
    # for singleDate in dateCounter:
    if count >= numberOfMaxEntries:
        numberOfMaxEntries = countorganisation1
        dayWithMaxEntries = date

print(dayWithMaxEntries)
print(type(dayWithMaxEntries))




