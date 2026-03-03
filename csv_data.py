import csv

with open ('iris.csv', 'r') as csv_file:

    csv_reader =csv.DictReader(csv_file)
    
    # next(csv_reader)

    with open('new_iris.csv', 'w') as new_csv:
        filed_names = ['150', '4', 'setosa', 'versicolor']

        print(filed_names)

                       
                       
        csv_writer = csv.DictWriter(new_csv,fieldnames=filed_names)

        csv_writer.writeheader()

        



       

        for lines in csv_reader:
             del lines['verginica']
        # print(lines['virginica'])
             csv_writer.writerow(lines)



    # next(csv_reader)

    # for line in csv_reader:
    #     print(line[0])