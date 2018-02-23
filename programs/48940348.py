def read(pulsar_name,signal_strength):
    astro_list = []
    with open(pulsar_name, 'r') as p, open(signal_strength, 'r') as s:
        pulsar_lines = p.readlines()
        signal_lines = s.readlines()
        for i in range(len(pulsar_lines)):
            pline = pulsar_lines[i].strip().split()
            sline = signal_lines[i].strip().split()
            astro_list.append([])
            for j in range(len(pline)):
                astro_list[-1].append(pline[j].capitalize() + sline[j])
    
    with open('z.txt', 'w') as z:
        for i in range(len(astro_list)):
            z.write(' '.join(astro_list[i]))
            z.write('\n')
          
    return astro_list

#defining the main function
def main():

    #displaying a description of what the program does
    purpose = "This program proccess data from the Purdue Pulsar Laboratory"
    underheading = "=" * len(purpose)
    print(purpose)
    print(underheading)
    print("It reads the data from 2 files containing the pulsar name and signal strength, \nthen combines them and displays the results.")
    #accepting inputs from the user about file names
    pulsar_name = input("\nPulsar name file: ")
    signal_strength = input("Signal strength: ")
    #calling
    astro_list = read(pulsar_name,signal_strength)
    #reading values
    print("\nAnalyzing data from" , pulsar_name, "and", signal_strength, "files...")
    print("     ","Reading from" ,pulsar_name,"...")
    print("     ","Reading from" ,signal_strength,"...")
    print("     ","Combining values...")
    #displaying the top part of the table/ counting the number of elements that are in the list
    print("\nThe combined BOOYA data includes" ,len(astro_list) * len(astro_list[0]), "values.")
    print(underheading)
    for l in astro_list:
        print(*l)
    
if __name__ == '__main__':
    main()
