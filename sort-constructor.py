import csv

def sortedconstructor(input_file, constructor_list):
    with open(input_file, "r", newline='') as file:
        csv_reader = csv.reader(file)

        headers = next(csv_reader)

        with open("sortedconstructor.csv", "w", newline='') as output_file:
            csv_writer = csv.writer(output_file)

            csv_writer.writerow(headers)

            for row in csv_reader:
                constructor_ref = row[headers.index('constructorRef')]

                if constructor_ref in constructor_list:
                    csv_writer.writerow(row)

sortedconstructor('./Datas/constructors.csv',  ['mclaren', 'red_bull', 'ferrari', 'mercedes', 'aston_martin', 'rb', 'alpine', 'williams', 'haas', 'sauber'])
