import pyttsx3
import datetime
import winsound
from colour_text import ColourText
import requests
import sys


def update():
    def download(url, filename):
        with open(filename, 'wb') as fi:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')

            if total is None:
                fi.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total / 10), 34 * 34)):
                    downloaded += len(data)
                    fi.write(data)
                    sys.stdout.flush()
        sys.stdout.write('\n')

    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/run.py', 'run.py')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/BY%20GLN.txt', 'BY GLN.TXT')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/list%20asci.txt', 'list asci.txt')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/all_star.txt', 'all_star.txt')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/get_star.txt', 'get_star.txt')
    download('https://raw.githubusercontent.com/srikargodavarthi/srikar/master/collection_star.txt', 'collection_star.txt')


def check_update():
    op = 'https://raw.githubusercontent.com/srikargodavarthi/srikar/master/UPDATE'
    response = requests.get(op)
    response.decode = 'utf-8'
    neup = response.text

    if 'YES' in neup:
        update()


def speak(audio) -> object:
    engine.say(audio)
    engine.runAndWait()


def talk(audio) -> object:
    print("-->>\t\t" + audio)
    print("\n")
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if 0 <= CurrentHour < 12:
        talk('Good Morning!')

    elif 12 <= CurrentHour < 18:
        talk('Good Afternoon!')

    elif CurrentHour >= 18 and CurrentHour != 0:
        talk('Good Evening!')


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def sound():
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


check_update()
ct = ColourText()
ct.initTerminal()
COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}

f = open("BY GLN.txt", "r")
asci = "".join(f.readlines())
print(colorText(asci))

q = open("list asci.txt", "r")
correct = "".join(q.readlines())

g=open("get_star.txt", "r")
getunderscore= "".join(g.readlines())

al=open("all_star.txt", "r")
allunderscore= "".join(al.readlines())

coll=open("collection_star.txt", "r")
collectionunderscore= "".join(coll.readlines())

sorry = ct("<>red !!!!!  sorry there is no such command !!!!!<>")
engine = pyttsx3.init()
engine.setProperty('rate', 145)  # setting up new voice rate



read = "\tThe read command,  reads the RTL file," \
       "and translates into unmapped ddc file, and then, loads designs in DC  memory, dc means, (design compiler) " \
       ".\n\t\t\t\t It sets one " \
       "of the design in memory, to the current design.\n\t\t\t\t It also loads the default tech libraries, " \
       "and user specified link libraries.\n\t\t\t\t Before giving read command make sure to adjust the current " \
       "directory and " \
       "topo. "

second = " It loads, the constraints" \
         "\t."

third = "It lists, all the timing violations" \
        "\t."

fourth = " It checks, the timing variations, for different error conditions" \
         "\t."

fifth = "It converts the rtl code, and generate a net list, mapped with the specific libraries" \
        "\t."

six = "\tSame as the read_verilog command. It reads the VHDL file which we have,\n\t\t\t The vhdl design library is " \
      "called, work by default.\n\t\t\t The work files and directories are by default placed in current working " \
      "directry called as (cwd) "

seven = "To keep your cwd relatively clean, you can redirect the VHDL Design Library’\n\t\t\t to be stored in a " \
        "separate directory. "

eight = "The target technology library is required, to synthesize the, RTL to gates. It is of .db format. " \
        "\t"

nine = "set_up_var sets a variable value, target_library is already reserved.\n\t\t\t Libs/20nm_wc tells us the " \
       "library characterized, for the appropriate PVT corner,\n\t\t\t for setup timing optimization "

ten = "It saves the netlist, before exiting the design compiler." \
      "\t"

eleven = "It is used to reduces the instantiated errors when try to read the netlist in the read command\n\t\t\t " \
         "instead of a vhdl or a verilog code. In many of the cases we use the target library as the link library "

twelve = "This is the syntax for the linking of the library. Here * represents the design in the dc memory.\n\t\t\t " \
         "We have to run the command Link after the linking of your library is done. "

thirteen = "design cells, (instance) in the current design, and in sub_blocks with, -hier" \
           "\t"

fourteen = "clocks defined from the current design, or above, on pins/ports at the current" \
             "design or sub-block level, defined by create_clock or create_generated_clock.Does not report clocks " \
             "that were created from" \
             "within a lower-level design"

fifteen = "designs loaded in DC memory, (not just in the current design)."

sixteen = "libraries loaded in dc memory"

seventeen = "library cells in the specified, library."

eighteen = "pins, of specified library cells."

nineteen = "nets at the current design level, and sub-block level with -hier"

twenty = "input/output pins of cells (instances) at the current design level, and sub block level with -hier; pins " \
          "are always associated with a cell."

twentyone = "primary input/output/bidir ports at the current design level, and sub-block level with  -hier."

twentytwo = "Gets all input, and inout ports, of the current design."

twentythree = "Gets all output, and inout ports, of the current design."

twentyfour = "Gets all clocks defined from the current design at the current design level,or below"

twentyfive = "Gets all register cells, in the entire current design's hierarchy"

twentysix = "Gets all ideal nets, of the current design."

twentyseven = "Gets all fanin details."

twentyeight = "Gets all fanout details."

twentynine = "Add object(s)."

thirty = "compares two collections "

thirtyone = "Make a copy of a collection"

thirtytwo = "Filter a collection, resulting in a new collection"

thirtythree = "Iterate over a collection "

thirtyfour = "Extract object from collection "

thirtyfive = "Remove object (s) from a collection "

thirtysix = "Number of objects in a collection "

thirtyseven = "Create a sorted copy of a collection "

thirtyeight = "Used to define, the false path that are present in the design."

greetMe()
talk('hai, i am bot, and my name is sta.')
talk('For better view, please maximise the window.')
talk('enter the command, which you want to know.')
talk('for example, to see, the list of commands, enter the command as shown below. ')
print('\n\t\t\t\tlist')
if __name__ == '__main__':
    while True:
        print("\n")
        query = input("--->\t")
        query = query.lower()
        if 'get_*' in query:

            print(colorText(getunderscore))
        elif 'all_*' in query:
            print(colorText(allunderscore))
        elif 'collection_*' in query:
            print(colorText(collectionunderscore))
        elif 'list' in query:

            talk('these are the list, of some commands')
            print(colorText(correct))
        elif 'read_verilog rtl/filename_rtl.v' in query:
            talk(read)

        elif 'source cons/filename.con' in query:
            talk(second)
        elif 'repot_constraints -all violators' in query:
            talk(third)
        elif 'check_timing' in query:
            talk(fourth)
        elif 'compile_ultra' in query:
            talk(fifth)
        elif 'read_vhdl' in query:
            talk(six)
        elif "define_design_lib " in query:
            talk(seven)

        elif 'set_app_var target_library libs/20nm_wc.db' in query:
            talk(nine)
        elif 'write_file -format verilog-  output\directory_name/file_name.v' in query:
            talk(ten)
        elif 'link_library' in query:
            talk(eleven)
        elif 'set_app_var link_library “* $target_library”' in query:
            talk(twelve)
        elif 'target_library' in query:
            talk(eight)
        elif 'get_cells' in query:
            talk(thirteen)
        elif 'get_clocks' in query:
            talk(fourteen)
        elif 'get_designs' in query:
            talk(fifteen)
        elif 'get_libs' in query:
            talk(sixteen)
        elif 'get_lib_cells <libname/cellname>' in query:
            talk(seventeen)
        elif 'get_lib_pins <libname/cellname/pinname>' in query:
            talk(eighteen)
        elif 'get_nets' in query:
            talk(nineteen)
        elif 'get_pins <cell/pin>' in query:
            talk(twenty)
        elif 'get_ports' in query:
            talk(twentyone)
        elif 'all_inputs' in query:
            talk(twentytwo)
        elif 'all_outputs' in query:
            talk(twentythree)
        elif 'all_clocks' in query:
            talk(twentyfour)
        elif 'all_registers' in query:
            talk(twentyfive)
        elif 'all_ideal_nets' in query:
            talk(twentysix)
        elif 'all_fanin' in query:
            talk(twentyseven)
        elif 'all_fanout' in query:
            talk(twentyeight)
        elif 'add_to_collection' in query:
            talk(twentynine)
        elif 'compare_collections' in query:
            talk(thirty)
        elif 'copy_collection' in query:
            talk(thirtyone)
        elif 'filter_collection' in query:
            talk(thirtytwo)
        elif 'foreach_in_collection' in query:
            talk(thirtythree)
        elif 'index_collection' in query:
            talk(thirtyfour)
        elif 'remove_from_collection' in query:
            talk(thirtyfive)
        elif 'sizeof_collection' in query:
            talk(thirtysix)
        elif 'sort_collection' in query:
            talk(thirtyseven)
        elif 'set_false_path' in query:
            talk(thirtyeight)



        else:
            print("\t\t\t\t\t" + sorry)
            sound()
            speak('sorry, there is no such command')

