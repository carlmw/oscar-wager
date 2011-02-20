import csv
import simplejson as json

reader = csv.reader(open('oscar-data.csv', 'rU'), delimiter=',', quoting=csv.QUOTE_NONE)

count = 0
def uniqify(old):
    new = []
    [new.append(i) for i in old if not new.count(i)]
    return new

awards = []
award_map = {}
nominees = []
fixtures = []
for row in reader:
  nominees.append({'award':row[0], 'name':row[1], 'reference':row[2]})
  awards.append(row[0])

for i, award in enumerate(uniqify(awards)):
    fixtures.append({'pk': i+1, 'model': 'wager.Award', 'fields':{'name':award}})
    award_map[award] = i+1
    count = i+1

for nom in nominees:
    count = count + 1
    fixtures.append({'pk': count, 'model': 'wager.Entry', 'fields':{'name':nom['name'],'reference':nom['reference'], 'award':award_map[nom['award']]}})
    
print json.dumps(fixtures)