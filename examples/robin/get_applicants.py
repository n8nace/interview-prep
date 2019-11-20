# Parse the applicants.csv file into an applicant list
import csv
from slap import slap_fight
applicants = []
with open("applicants.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        applicants.append(dict(row))
csvfile.close()
player_1_index = 0
player_2_index = 1
for i in range(player_1_index, len(applicants)):
    applicants[i]['Wins'] = 0
    applicants[i]['Matches'] = 0
for i in range(player_1_index, len(applicants) - 1):
    for j in range(i+1, len(applicants)):
        print (applicants[i]['Name'] + " VS " + applicants[j]['Name'])
        applicants[i]['Matches'] += 1
        applicants[j]['Matches'] += 1
        result = slap_fight(applicants[i],applicants[j])
        if result == 1:
            applicants[i]['Wins'] += 1
        else:
            applicants[j]['Wins'] += 1
for applicant in applicants:
    win_percent = float(float(applicant['Wins']) / float(applicant['Matches']))
    win_percent = round(win_percent, 4)
    print(applicant['Name'] + " win percentage: " + str(win_percent))