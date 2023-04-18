#Common functions we use that have outputs 
length = len(formatted_name)

#Return as an realy exit 
def format_name(f_name, l_name):
    #Docstring is to document and explain functions 
    """Take a first and last name 
    and format it 
    to return the title case version of the name"""
    if f_name == "" or l_name== "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"