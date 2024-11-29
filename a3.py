import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--medals", nargs=2)
parser.add_argument("--total",nargs="*")
parser.add_argument("--overall", nargs="*")
parser.add_argument("--interactive", nargs = "*")
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

    if args.interactive:
        country1 = input("Enter the name of the country: ")
        dic_of_the_c = {}
        list_of_y = []
        suc = 0
        year_of_suc = 0
        for l in all_lines:
            if l[14] != "NA":
                if country1 in l[6]:
                    if l[9] in list_of_y:
                        dic_of_the_c[l[9]] += f", {l[14]}"
                    else:
                        dic_of_the_c[l[9]] = l[14]
                        list_of_y.append(l[9])

                    for y in list_of_y:
                        dic = dic_of_the_c[y].split(",")

                        if len(dic) >= suc:
                            suc = len(dic)
                            year_of_suc = y
        print(f"In {year_of_suc} {country1} had {suc} medals. It is the biggest amount of medals in {country1}'s history")

    for i in range(0, len(list_of_y)-1):
        if int(list_of_y[i]) <= int(list_of_y[i+1]):
            first = list_of_y[i]
        else:
            first = list_of_y[i+1]
    print(f"In {first} {country1} was on olimpic at first time.")


    list_of_p = ["Gold", "Silver", "Bronze"]
    if args.medals:
        country = args.medals[0]
        year = args.medals[1]
        list_of_medals =[]
        for l in all_lines:
            if country in l[6]:
                if year in l[9]:
                    if l[14] in list_of_p:
                        list_of_medals.append(l[14])
        print(f"All teams from {country} in {year} get {list_of_medals}")

    dic_of_the_year = {}
    list_of_c = []
    if args.total:
        year_for_all = args.total[0]
        for l in all_lines:
            if year_for_all in l[9]:
                if l[len(l) - 1] != "NA" and l[len(l) - 1] != "N":
                    if l[6] in list_of_c:
                        dic_of_the_year[l[6]] += f", {l[14]}"
                    else:
                        dic_of_the_year[l[6]] = l[14]
                        list_of_c.append(l[6])
        print(dic_of_the_year)


    if args.overall:
        for e in args.overall:
            dic_of_the_c = {}
            list_of_y =[]
            suc = 0
            year_of_suc = 0
            for l in all_lines:
                if l[14] != "NA":
                    if e in l[6]:
                        if l[9] in list_of_y:
                            dic_of_the_c[l[9]] += f", {l[14]}"
                        else:
                            dic_of_the_c[l[9]] = l[14]
                            list_of_y.append(l[9])

                        for y in list_of_y:
                            dic = dic_of_the_c[y].split(",")

                            if len(dic) >= suc:
                                suc = len(dic)
                                year_of_suc = y
            print(f"In {year_of_suc} {e} had {suc} medals. It is the biggest amount of medals in {e}'s history")









