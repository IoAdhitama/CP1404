COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
                "brown": "#a52a2a", "burlywood": "#deb887", "chocolate": "#d2691e", "coral": "#ff7f50",
                "cyan": "#00ffff", "firebrick": "#b22222"}

colour_input = input("Enter colour name: ").lower()
while colour_input != "":
    if colour_input in COLOUR_CODES:
        print("{}'s colour code is {}".format(colour_input, COLOUR_CODES[colour_input]))
    else:
        print("Invalid colour/colour not available")
    colour_input = input("Enter colour name: ").lower()