import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-medals","--country")
parser.add_argument("--years")
parser.add_argument("-total","--year")
parser.add_argument("-overall","--countries")
parser.add_argument("-interactive","--interactive")
args = parser.parse_args()
print(args)

with (open(args.input_file, "rt") as file):
    all_lines = []
    next(file)
    for line in file:
        line = line[:-1]
        split = line.split('\t')
        l = []
        for i in range(0,len(split)):
            l.append(split[i])
        all_lines.append(l)
    print(all_lines)


    if args.country:
        list_of_medals =[]
        for l in all_lines:
            if l[9]== args.years:
                if l[7] == args.country:
                    if l[len(l)-1] != "NA":
                        list_of_medals.append(l[len(l)-1])
        print(f"All teams from {args.country} in {args.years} get {list_of_medals}")