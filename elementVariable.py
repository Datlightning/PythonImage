class elementInfo:
    elementList = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 39, 40, 40, 45, 48, 51, 52, 55, 56,
                       59, 59, 64, 65, 70, 73, 75, 79, 80, 84, 85, 88, 89, 91, 93, 96, 98, 101, 103, 106, 108, 112, 115,
                       119, 122, 128, 127, 131, 133, 137, 139, 140, 141, 144, 145, 150, 152, 157, 159, 163, 165, 167, 169,
                       173, 175, 179, 181, 184, 186, 190, 192, 195, 197, 201, 204, 207, 209, 210, 210, 220, 223, 226, 226,
                       231, 232, 237, 238, 243, 244, 247, 247, 251, 252, 257, 258, 259, 262, 261, 262, 266, 264, 277, 268,
                       271, 272, 285, 284, 289, 288, 292, 292, 294]
    ##Element Names
    elementName = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
                   "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
                   "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron",
                   "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
                   "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
                   "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium",
                   "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
                   "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium",
                   "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium",
                   "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine",
                   "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
                   "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
                   "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium",
                   "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium",
                   "Moscovium", "Livermorium", "Tennessine", "Oganesson"]
    ##Element Symbols
    elementSymbol = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                     "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br",
                     "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb",
                     "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
                     "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
                     "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es",
                     "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
                     "Lv", "Ts", "Og"]
    ##Every integer from 0 to 118. Fixes conflict when searching the element info.
    possibleAnswers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                       "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
                       "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
                       "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65",
                       "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81",
                       "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97",
                       "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111",
                       "112", "113", "114", "115", "116", "117", "118"]
    latinNames = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
                   "Neon", "Natrium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
                   "Kalium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Ferrum",
                   "Cobalt", "Nickel", "Cuprum", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
                   "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
                   "Ruthenium", "Rhodium", "Palladium", "Argentum", "Cadmium", "Indium", "Stannum", "Stibium", "Tellurium",
                   "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
                   "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium",
                   "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Wolfram", "Rhenium", "Osmium",
                   "Iridium", "Platinum", "Aurum", "Hydragyrum", "Thallium", "Plumbum", "Bismuth", "Polonium", "Astatine",
                   "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
                   "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
                   "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium",
                   "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium",
                   "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

    allNames = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
                   "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
                   "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron",
                   "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
                   "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
                   "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium",
                   "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
                   "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium",
                   "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium",
                   "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine",
                   "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
                   "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
                   "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium",
                   "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium",
                   "Moscovium", "Livermorium", "Tennessine", "Oganesson", "Natrium", "Kalium", "Ferrum", "Cuprum", "Stibium", "Aurum", "Plumbum", "Hydragyrum","Argentum","Stannum","Wolfram"]

##The rows of the periodic table of elements.
class Periods:
    period1 = [1, 2]
    period2 = [3, 4, 5, 6, 7, 8, 9, 10]
    period3 = [11, 12, 13, 14, 15, 16, 17, 18]
    period4 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    period5 = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
    period6 = [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86]
    period7 = [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
               110, 111, 112, 113, 114, 115, 116, 117, 118]
##The columns of the periodic table of elements.
class Groups:
    group1 = [1, 3, 11, 19, 37, 55, 87]
    group2 = [4, 12, 20, 38, 56, 88]
    group3 = [21, 39, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 89, 90, 91, 92, 93, 94, 95, 96, 97,98, 99, 100, 101, 102, 103]
    group4 = [22, 40, 72, 104]
    group5 = [23, 41, 73, 105]
    group6 = [24, 42, 74, 106]
    group7 = [25, 43, 75, 107]
    group8 = [26, 44, 76, 108]
    group9 = [27, 45, 77, 109]
    group10 = [28, 46, 78, 110]
    group11 = [29, 47, 79, 111]
    group12 = [30, 48, 80, 112]
    group13 = [5, 13, 31, 49, 81, 113]
    group14 = [6, 14, 32, 50, 82, 114]
    group15 = [7, 15, 33, 51, 83, 115]
    group16 = [8, 16, 34, 52, 84, 116]
    group17 = [9, 17, 35, 53, 85, 117]
    group18 = [2, 10, 18, 36, 54, 86, 118]
