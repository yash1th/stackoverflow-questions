import csv

# country = ['Togo', 'Nauru', 'Palestine, State of', 'Malawi']
# with open('temp.csv', 'wt') as output_write:
#     csvout = csv.writer(output_write)
#     for item in country:
#         csvout.writerow(list(item))

# country = ['Togo', 'Nauru', 'Palestine, State of', 'Malawi']
# with open('temp.csv', 'wt') as output_write:
#     csvout = csv.writer(output_write)
#     for item in country:
#         csvout.writerow(list(item))

country = ['Togo', 'Nauru', 'Palestine, State of', 'Malawi']
with open('temp.csv', 'wt') as output_write:
    csvout = csv.writer(output_write)
    for item in country:
        csvout.writerow((item, ))
