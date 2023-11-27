# Function needs to get MM/DD/YYYY or Month Day, YYYY convert to YYYY-MM-DD

def main():
    date = get_date()
    output = convert(date)
    try:
        if output[1] < 10 and output[2] < 10:
            print(f"{output[0]}-0{output[1]}-0{output[2]}")
        elif output[1] < 10 and output[2] >= 10:
            print(f"{output[0]}-0{output[1]}-{output[2]}")
        elif output[1] >= 10 and output[2] < 10:
            print(f"{output[0]}-{output[1]}-0{output[2]}")
        else:
            print(f"{output[0]}-{output[1]}-{output[2]}")

    except TypeError:
        pass

# adding in acceptable Months, Days and Years

months =["January",
             "February",
             "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
         ]
int_days = []
i = 1
for _ in range(31):
    int_days.append(i)
    i += 1

days = []

for integer in int_days:
    if integer < 10:
        str_day = "0" + str(integer)
        days.append(str_day)
    else:
        str_day = str(integer)
        days.append(str_day)

int_years = []
counter = 1
for _ in range(2023):
    int_years.append(counter)
    counter += 1

years = []
for int_year in int_years:
        if int_year < 10:
            str_year = "000" + str(int_year)
            years.append(str_year)
        elif int_year < 100:
            str_year = "00" + str(int_year)
            years.append(str_year)
        elif int_year < 1000:
            str_year = "0" + str(int_year)
            years.append(str_year)
        else:
            str_year = str(int_year)
            years.append(str_year)


# Get valid date from user
def get_date():
    while True:
        n = input("Enter MM/DD/YYYY or Month, Day, Year: ".strip().title())

        for month in months:
            if n.startswith(month):
                m, d_proto, y =n.split(" ")
                string_day = d_proto.replace(",", "")
                for d in days:
                    if d.startswith("0"):
                        no_zero_d = d.replace("0", "")
                        if no_zero_d == string_day:
                            int_d = int(string_day)
                            for year in years:
                                if year == y:
                                    return y, m, int_d
                    else:
                        if d == string_day:
                            int_d = int(string_day)
                            for year in years:
                                if year == y:
                                    return y, m, int_d
            elif "/" in n:
                mm, dd, yy = n.split("/")
                int_dd = int(dd)
                int_mm = int(mm)
                return yy, int_mm, int_dd
            else:
                continue

#change YYYY, MM, DD tuple or if YYYY, Month, DD tuple into proper output
def convert(inp):
    count = 0
    for mmm in months:
        count += 1
        if mmm == inp[1]:
            if inp[2] < 10 and count < 10:
                print(f"{inp[0]}-0{count}-0{inp[2]}")
            elif count < 10 and inp[2] >= 10:
                print(f"{inp[0]}-0{count}-{inp[2]}")
            elif count >= 10 and inp[2] < 10:
                print(f"{inp[0]}-{count}-0{inp[2]}")
            else:
                print(f"{inp[0]}-{count}-{inp[2]}")
            return None

    return inp




main()
