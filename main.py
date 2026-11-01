from control import program_end, per_one, per_two, per_three, per_four, per_five, per_six, per_seven, per_eight, fin_print
from var import cont

while cont != 1 and cont != 2:
    print("----------------------------------------------------------")
    print("               RRHS Freahman GPA Calculator")
    print("         Check Your GPA Before Your GPA Gets You")
    print("\nWould You Like To Continue?\n1. Yes\n2. No")
    cont = int(input("Type A Number: "))
    if cont == 1:
        per_one()
        per_two()
        per_three()
        per_four()
        per_five()
        per_six()
        per_seven()
        per_eight()
        fin_print()
    elif cont == 2:
        program_end()
        
