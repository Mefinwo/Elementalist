import os

ver = "Alpha 0.1.0"

#List of all symbols
Elemente = ["H", "Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr", "Ba", "Ra", "B", "Al", "Ga", "In", "Tl", "C", "Si", "Ge",
            "Sn", "Pb", "N", "P", "As", "Sb", "Bi", "O", "S", "Se", "Te", "Po", "F", "Cl", "Br", "I", "At", "He", "Ne", "Ar", "Kr", "Xe", "Rn"]

#List of all elements
Elemente_name = ["Wasserstoff", "Lithium", "Natrium", "Kalium", "Rubidium", "Ceasium", "Francium", "Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium", "Bor", "Aluminium", "Gallium", "Indium", "Thallium", "Kohlenstoff", "Silicium",
                 "Germanium", "Zinn", "Blei", "Stickstoff", "Phosphor", "Arsen", "Antimon", "Bismut", "Sauerstoff", "Schwefel", "Selen", "Tellur", "Polonium", "Flour", "Chlor", "Brom", "lod", "Astat", "Helium", "Neon", "Argon", "Kypton", "Xenon", "Radon"]

#List of all main groups
Hauptgruppe = ["1", "1", "1", "1", "1", "1", "1", "2", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3", "4", "4", "4",
               "4", "4", "5", "5", "5", "5", "5", "6", "6", "6", "6", "6", "7", "7", "7", "7", "7", "8", "8", "8", "8", "8", "8"]

#List of all atomic numbers
Ordnungszahl = ["1", "3", "11", "19", "37", "55", "87", "4", "12", "20", "38", "56", "88", "5", "13", "31", "49", "81", "6", "14", "32",
                "50", "82", "7", "15", "33", "51", "83", "8", "16", "34", "52", "84", "9", "17", "35", "53", "85", "2", "10", "18", "36", "54", "86"]

#List of Electronegativity values
En = ["2.2", "0.98", "0.93", "0.82", "0.82", "0.79", "0.7", "1.57", "1.31", "1.0", "0.95", "0.89", "0.89", "2.04", "1.61", "1.81", "1.78", "1.62", "2.55", "1.9", "2.01",
      "1.96", "2.33", "3.04", "2.19", "2.18", "2.05", "2.02", "3.44", "2.58", "2.55", "2.66", "2.0", "3.98", "3.16", "2.96", "2.1", "2.2", "/", "/", "/", "/", "/", "/"]

#List of atomic density
Dichte = ["0.09", "0.53", "0.97", "0.86", "1.53", "1.90", "?", "1.85", "1.74", "1.55", "2.63", "3.59", "5.50", "2.46", "2.70", "5.90", "7.31", "11.85", "2.26", "2.34", "5.32",
          "7.26", "11.35", "1.25", "2.69", "5.73", "6.70", "9.75", "1.43", "2.07", "4.82", "6.25", "9.20", "1.70", "3.21", "3.12", "4.94", "?", "0.18", "0.90", "1.78", "3.75", "5.90", "9.73"]

#List of main group 1
hg1 = ["H = Wasserstoff", "Li = Lithium", "Na = Natrium", "K = Kalium", "Rb = Rubidium", "Cs = Ceasium", "Fr = Francium"]
#List of main group 2
hg2 = ["Be = Beryllium", "Mg = Magnesium", "Ca = Calcium", "Sr = Strontium", "Ba = Barium", "Ra = Radium"]
#List of main group 3
hg3 = ["B = Bor", "Al = Aluminium", "Ga = Gallium", "In = Indium", "Ti = Thallium"]
#List of main group 4
hg4 = ["C = Kohlenstoff", "Si = Silicium", "Ge = Germanium", "Sn = Zinn", "Pb = Blei"]
#List of main group 5
hg5 = ["N = Stickstoff", "P = Phosphor", "As = Arsen", "Sb = Antimon", "Bi = Bismut"]
#List of main group 6
hg6 = ["O = Sauerstoff", "S = Schwefel", "Se = Selen", "Te = Tellur", "Po = Polonium"]
#List of main group 7
hg7 = ["F = Flour", "Cl = Chlor", "Br = Brom", "I = Iod", "At = Astat"]
#List of main group 8
hg8 = ["He = Helium", "Ne = Neon", "Ar = Argon", "Kr = Krypton", "Xe = Xenon", "Rn = Radon"]

#Var Error: For any types of errors. They will be printed in the main menu
error = ""

#Definition to clear system
def cls():
    os.system('clear')

#Definition for the logo
def logo_popup():
    print("""

  _______  ___       _______  ___      ___   _______  _____  ___  ___________   __      ___        __      ________  ___________  
 /"     "||"  |     /"     "||"  \    /"  | /"     "|(\"   \|"  \("     _   ") /""\    |"  |      |" \    /"       )("     _   ") 
(: ______)||  |    (: ______) \   \  //   |(: ______)|.\\   \    |)__/  \\__/ /    \   ||  |      ||  |  (:   \___/  )__/  \\__/  
 \/    |  |:  |     \/    |   /\\  \/.    | \/    |  |: \.   \\  |   \\_ /   /' /\  \  |:  |      |:  |   \___  \       \\_ /     
 // ___)_  \  |___  // ___)_ |: \.        | // ___)_ |.  \    \. |   |.  |  //  __'  \  \  |___   |.  |    __/  \\      |.  |     
(:      "|( \_|:  \(:      "||.  \    /:  |(:      "||    \    \ |   \:  | /   /  \\  \( \_|:  \  /\  |\  /" \   :)     \:  |     
 \_______) \_______)\_______)|___|\__/|___| \_______) \___|\____\)    \__|(___/    \___)\_______)(__\_|_)(_______/       \__|     
                                                                                                                                  




 
 
      __      ___         _______    __    __       __              ______         ____              ______    
     /""\    |"  |       |   __ "\  /" |  | "\     /""\            /    " \       /  " \            /    " \   
    /    \   ||  |       (. |__) :)(:  (__)  :)   /    \          // ____  \     /__|| |           // ____  \  
   /' /\  \  |:  |       |:  ____/  \/      \/   /' /\  \        /  /    ) :)       |: |          /  /    ) :) 
  //  __'  \  \  |___    (|  /      //  __  \\  //  __'  \      (: (____/ //_____  _\  |    _____(: (____/ //  
 /   /  \\  \( \_|:  \  /|__/ \    (:  (  )  :)/   /  \\  \      \        /))_  ")/" \_|\  ))_  ")\        /   
(___/    \___)\_______)(_______)    \__|  |__/(___/    \___)      \"_____/(_____((_______)(_____(  \"_____/    
                                                                                                               

                                                                                             

                                                                                             


""")

#Definition for the main menu
def main_menu():
    cls()
    logo_popup()
    print("——————————————————————————————————————————————————————————————————————————————————")  
    print("Main Menu")
    if not error == "":
        print(error)

    print("——————————————————————————————————————————————————————————————————————————————————")
    print("Enter 'L' for list of elements. ")
    print("Enter 'E' to recieve data a specific element.")
    print("Enter 'T' to calculate the particial charge.")
    print("Note: Elements have to be written in the right upper/lower cases!")
    print("——————————————————————————————————————————————————————————————————————————————————") 

#Definition for function to list all elements with their matching symbols
def list():
    logo_popup()
    print("——————————————————————————————————————————————————————————————————————————————————")                    
    print("Main group 1:", hg1)
    print("Main group 2:", hg2)
    print("Main group 3:", hg3)
    print("Main group 4:", hg4)
    print("Main group 5:", hg5)
    print("Main group 6:", hg6)
    print("Main group 7:", hg7)
    print("Main group 8 :", hg8)
    print("——————————————————————————————————————————————————————————————————————————————————")
    input("Press Enter to continue...")
    main_menu()

#Definition for function to calculate the particial charge between two elements
def particial_charge():
    try:
        logo_popup()
        print("——————————————————————————————————————————————————————————————————————————————————") 
        k = input("Enter first symbol: ")
        k2 = input("Enter second symbol: ")
        n = Elemente.index(k)
        n2 = Elemente.index(k2)
        h = float(En[n])
        h2 = float(En[n2])            
        s = h - h2 
        g = round(s, 2)

        if g < 0:
            g = g * (-1)
        print("You have a particial charge of: ", g)
        if g < 0.5 and g > 0:
            print("Your bond is non-polar.")
        if g < 1.8 and g > 0.4:
            print("Your bond is polar.")
        if g > 1.7:
            print("Your bond is an ionic bond.")
        print("——————————————————————————————————————————————————————————————————————————————————") 
        a = input("Restart particial charge calculator? (J/N)")
        if a == "J":
            particial_charge_()
        elif a == "N":
            main_menu()
        
    except:
        cls()
        logo_popup()
        print(f"Error 003: '{k}'or'{k2}' couldn't be found! Please check your input!")
        input("Press Enter to continue...")
        main_menu()

#Definition for function to calculate the particial charge between two elements. Again
def particial_charge_():
    try:
        print("——————————————————————————————————————————————————————————————————————————————————") 
        k = input("Enter first symbol: ")
        k2 = input("Enter second symbol: ")
        n = Elemente.index(k)
        n2 = Elemente.index(k2)
        h = float(En[n])
        h2 = float(En[n2])            
        s = h - h2
        g = round(s, 2)
    
        if g < 0:
            g = g * (-1)
        print("You have a particial charge of: ", g)
        if g < 0.5 and g > 0:
            print("Your bond is non-polar.")
        if g < 1.8 and g > 0.4:
            print("Your bond is polar.")
        if g > 1.7:
            print("Your bond is an ionic bond.")
        print("——————————————————————————————————————————————————————————————————————————————————") 
        a = input("Restart particial charge calculator? (J/N)")
        if a == "J":
            particial_charge_()
        elif a == "N":
            main_menu()
        
    except:
        cls()
        logo_popup()
        print(f"Error 003: '{k}'or'{k2}' couldn't be found! Please check your input!")
        input("Press Enter to continue...")
        main_menu()

#Definition for function to print out information about a specific element
def elemantalist(error):
    try:
        logo_popup()
        print("——————————————————————————————————————————————————————————————————————————————————") 
        x = input("Enter element symbol: ")
        y = Elemente.index(x)
        print("——————————————————————————————————————————————————————————————————————————————————")
        print("Element: ", Elemente_name[y])
        print("Symbol: ", Elemente[y])
        print("Main group: ", Hauptgruppe[y])
        print("Atomic number: ", Ordnungszahl[y])
        print("Electronegativity value: ", En[y])
        print("Density: ", Dichte[y])
        print("——————————————————————————————————————————————————————————————————————————————————") 
        a = input("Restart Elementalist? (J/N)")
        if a == "J":
            elemantalist_(error)
        elif a == "N":
            main_menu()
    except:
        cls()
        print(f"Error 002: '{x}' couldn`t be found!")
        input("Press Enter to continue...")
        main_menu()

#Definition for function to print out information about a specific element. Again
def elemantalist_(error):
    try:
        print("——————————————————————————————————————————————————————————————————————————————————") 
        x = input("Enter element symbol: ")
        y = Elemente.index(x)
        print("——————————————————————————————————————————————————————————————————————————————————")
        print("Element: ", Elemente_name[y])
        print("Symbol: ", Elemente[y])
        print("Main group: ", Hauptgruppe[y])
        print("Atomic number: ", Ordnungszahl[y])
        print("Electronegativity value: ", En[y])
        print("Density: ", Dichte[y])
        print("——————————————————————————————————————————————————————————————————————————————————") 
        a = input("Restart Elementalist? (J/N)")
        if a == "J":
            elemantalist_(error)
        elif a == "N":
            main_menu()
    except:
        cls()
        print(f"Error 002: '{x}' couldn`t be found!")
        input("Press Enter to continue...")
        main_menu()

#At the start open up the main menu to introduce the programm and teach the user how to navigate through the programm.
main_menu()

#This while loop is to ask the user what funktion they want to use. In the ifs/elifs we ask the short forms for the funktion and in the else we activate an error if it doesn't match any symbol.
while True:
    v = input(f"{ver}] ")    
    cls() 
    if v == "L" or v == "l":
        error = ""
        list()
    elif v == "E" or v == "e":
        error = ""
        elemantalist(error)
    elif v == "T" or v == "t":
        error = ""
        particial_charge()
    else:
        error = f"Error 001: '{v}' is a invalid input!"
        cls()
        main_menu()
        continue