import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print('1062368.csv -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('1062368.csv -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
    print(output_file)
    read_csv(input_file, output_file, format)

#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        #print(len(title))  = 4
        n = 0
        p = 0
        month = 1
        day = 1
        file_name = 2000
        csv_rows[month] = {}
        #the following loop runs the number of rows times i.e. 6412
        for row in reader:
            csv_rows[month][day] = {}
            csv_rows[month][day] = {title[i]:(float)(row[title[i]]) for i in range(len(title))}
            day = day + 1
            if day == 31:
                day = 1
                month = month + 1
                csv_rows[month] = {}
            n = n+1
            if n == 365:
                temp_file = (str)(file_name+p)
                write_json(csv_rows, temp_file+'.json', format)
                n = 0
                p = p+1
                csv_rows={}
                month = 1
                day = 1
                csv_rows[month] = {}
        #write_json(csv_rows, json_file, format)
#python3 getcsv.py -i 1062368.csv -o users.json -f dump
#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

if __name__ == "__main__":
   main(sys.argv[1:])