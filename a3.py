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
    print(l)

    if args.interactive:
        country = input("Enter the name of the country: ")
        args.countries = country

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


    list_of_years = []
    if args.overall:
        for l in all_lines:
            year = []
            if l[7] == args.countries:
                if l[len(l)-1] != "NA":
                    if year not in list_of_years:
                        year = [l[9], l[len(l)-1]]
                        list_of_years.append(year)
        n =0
        for n in range(0,len(list_of_years)-2):
            if n >= len(list_of_years) or n == len(list_of_years):
                break
            if list_of_years[n][0] == list_of_years[n+1][0]:
                list_of_years[n].append(list_of_years[n+1][1])
                list_of_years.remove(list_of_years[n+1])
        print(list_of_years)
        final = 0
        num =0
        year_of_max = []
        for y in list_of_years:
            if len(y) >= num:
                year_of_max.clear()
                final = y[0]
                num = len(y)
            if len(y) == num:
                year_of_max.append(y[0])
                final = f"We have a lot of years with {num-1} medals. For example:{year_of_max}"
        print(final)





