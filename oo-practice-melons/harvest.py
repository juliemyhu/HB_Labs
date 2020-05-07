############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = [] # melon.pairings = ['mint','strawberries']
        self.name= name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        # ['mint','strawberries']

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code 
        print(f'Code is now {new_code}')


def make_melon_types():
    """Returns a list of current melon types."""

    #list of instances of each melon 
    all_melon_types = []

    #                self,code, first_harvest, color,pairs well with, has seeds
    musk = MelonType('musk','Muskmelon',1998,'green',True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003,'orange', True, True)
    musk.add_pairing('strawberries')
    musk.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green',False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                   False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    # print(all_melon_types)
    return all_melon_types 

#melon_types would be something like all_melon_types
def print_pairing_info(melon_types): 
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs well with: ')
        for pairing in melon.pairings:
            print (f'- {pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    dic_of_melon_type_by_codes = {}

    for melon in melon_types:
        if melon.code not in dic_of_melon_type_by_codes:
            dic_of_melon_codes[melon.code]= melon 

    return dic_of_melon_type_by_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


print_pairing_info(make_melon_types())


