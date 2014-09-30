__author__ = 'andydelso'

def get_col_index(column_letter):
    col_to_num_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11
    }

    return col_to_num_dict[column_letter]



def get_steps_list(worksheet, cell):
    #grab the value from cell at the given cell
    value = worksheet.acell(cell).value

    #split by return characters
    #split_cell = value.split("\n")

    #remove blanks lines
    #for each in split_cell:
        #if each is ' ':

    # Found a better way here:
    # http://stackoverflow.com/questions/3711856/remove-empty-lines
    # Figure out exactly what this is doing sometime

    return [each for each in value.split('\n') if each.strip() != '']

def get_results_list(worksheet, cell):
    # grab the value from cell at the given cell
    value = worksheet.acell(cell).value
    #split_cell = value.split("\n")
    return [each for each in value.split('\n') if each.strip() != '']
