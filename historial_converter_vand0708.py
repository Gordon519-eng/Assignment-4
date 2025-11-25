#Owen Van Delst

ModernM = input("""
1- Liters
2- Quarts
3- Cups
4- Pints
Please select a messurment: """)
#print(ModernM)

Input = input("Please enter an amount: ")
#print(Input)

HistoricalM = input("""
1- Gill
2- Hogshead
3- Tun
4- Butt
Please enter a historical messurment: """)
#print(HistoricalM)

#convert all measurements to liters to keep math simple
Input2 = 0.0
if ModernM == "1":
    Input2 = Input
elif ModernM == "2":
    Input2 = float(Input) * 0.946
elif ModernM == "3":
    Input2 = float(Input) * 0.236
elif ModernM == "4":
    Input2 = float(Input) * 0.473
else:
    print("ERROR: invalid input")
#(Input)

OUTPUT = 0.0
if HistoricalM == "1":
    OUTPUT = float(Input2) * 8.453
elif HistoricalM == "2":
    OUTPUT = float(Input2) / 238.5
elif HistoricalM == "3":
    OUTPUT = float(Input2) / 953.92
elif HistoricalM == "4":
    OUTPUT = float(Input2) / 480
else:
    print("ERROR: invalid input")
#print(OUTPUT)

#making the output look good
if ModernM == "1":
    if HistoricalM == "1":
        print(str(Input) + " Liters is " + str(OUTPUT) + " Gill's")
    elif HistoricalM == "2":
        print(str(Input) + " Liters is " + str(OUTPUT) + " Hogshead's")
    elif HistoricalM == "3":
        print(str(Input) + " Liters is " + str(OUTPUT) + " Tun's")
    elif HistoricalM == "4":
        print(str(Input) + " Liters is " + str(OUTPUT) + " Butt's")
    else:
        print("ERROR: Output out of range")
elif ModernM == "2":
    if HistoricalM == "1":
        print(str(Input) + " Quarts is " + str(OUTPUT) + " Gill's")
    elif HistoricalM == "2":
        print(str(Input) + " Quarts is " + str(OUTPUT) + " Hogshead's")
    elif HistoricalM == "3":
        print(str(Input) + " Quarts is " + str(OUTPUT) + " Tun's")
    elif HistoricalM == "4":
        print(str(Input) + " Quarts is " + str(OUTPUT) + " Butt's")
    else:
        print("ERROR: Output out of range")
elif ModernM == "3":
    if HistoricalM == "1":
        print(str(Input) + " Cups is " + str(OUTPUT) + " Gill's")
    elif HistoricalM == "2":
        print(str(Input) + " Cups is " + str(OUTPUT) + " Hogshead's")
    elif HistoricalM == "3":
        print(str(Input) + " Cups is " + str(OUTPUT) + " Tun's")
    elif HistoricalM == "4":
        print(str(Input) + " Cups is " + str(OUTPUT) + " Butt's")
    else:
        print("ERROR: Output out of range")
elif ModernM == "4":
    if HistoricalM == "1":
        print(str(Input) + " Pints is " + str(OUTPUT) + " Gill's")
    elif HistoricalM == "2":
        print(str(Input) + " Pints is " + str(OUTPUT) + " Hogshead's")
    elif HistoricalM == "3":
        print(str(Input) + " Pints is " + str(OUTPUT) + " Tun's")
    elif HistoricalM == "4":
        print(str(Input) + " Pints is " + str(OUTPUT) + " Butt's")
    else:
        print("ERROR: Output out of range")
else:
    print("ERROR: Output out of range")