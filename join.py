import csv
csv_file = 'insults.csv'
txt_file = 'insults.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)[1:-1]+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()