def main():
    usernumber = get_number("FORTUNE TELLING (1-10)", "\n PICK A NUMBER (1-10) ")
    if 0 < usernumber < 11:
        strnumber = str(usernumber)
        scenario = get_scenarios(strnumber)
        print(scenario)
    else:
        print("FUCKER READ THE INSTRUCTIONS!!! AND REDO IT")
        main()

def get_number(Q, prompt):
    print(Q)
    while True:
        try:
            Val = int(input(prompt))
            if 10 < Val < 0:
                print("FUCKER READ THE INSTRUCTIONS!!!")
        except ValueError:
            print("Enter a number from 1-10, dumbfuck")
        else:
            return Val


def get_scenarios(number):

    dic =  {"1" : "Dhriti unknowingly inhales helium from a tank meant for inflating balloons, leading to a high-pitched voice and floating away like a balloon herself.",
             "2" : "A massive pile of rubber ducks in a bathtub collapses onto Dhriti, burying her in an avalanche of squeaky toys.",
             "3" : "Dhriti engages in an unintentional staring contest with a harmless basilisk that turns them to stone.",
             "4" : "Transported to a whimsical dessert-themed world, dhriti gets trapped in a vast sea of custard and drowns.",
             "5" : "Dhriti finds herself at a never-ending meet-and-greet event dies from sheer exhaustion after shaking hands with countless well-wishers.",
             "6" : "While attempting a daring selfie in a precarious location, dhriti loses balance and falls to her demise, illustrating the risks of extreme photo-taking behavior.",
             "7" : "In a comical twist, Dhriti attempts to devour a massive doughnut in one bite, leading to a choking accident that leads to her tragic death",
             "8" : "Dhriti manages to be in the wrong place at the wrong time when an incredibly slow-moving tractor runs her over, proving that even the slowest vehicles can be deadly.",
             "9" : "In an unexpected squirrel attack, Dhriti encounters a particularly aggressive rodent and succumbs to a series of small yet deadly squirrel bites.",
             "10" : "Dhriti's obsession with a new couch, combined with a series of unfortunate adhesive mishaps, results in them getting stuck and eventually perishing in a tragicomic furniture incident."

}

    return dic[number]


main()
