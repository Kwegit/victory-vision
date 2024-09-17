import csv

def sorteddrivers(input_file, drivers_list: list):
    with open(input_file, "r", newline='', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)

        # Ouvrir le fichier de sortie
        with open("sorteddrivers.csv", "w", encoding="utf-8", newline='') as output_file:
            csv_writer = csv.writer(output_file)

            csv_writer.writerow(headers)

            for row in csv_reader:
                driver_ref = row[headers.index('driverRef')].lower()

                if driver_ref in drivers_list:
                    csv_writer.writerow(row)

sorteddrivers('./Datas/drivers.csv', ["hamilton", "bottas", "russell", "leclerc", "sainz", "vettel", "verstappen", "perez", "norris", "ricciardo", "alonso", "stroll", "gasly", "ocon", "latifi", "albon", "magnussen", "schumacher", "zhou", "räikkönen"])
