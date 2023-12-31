from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):

    # Create a parser
    parser = ConfigParser()

    # Read config file
    parser.read(filename)

    if parser.has_section(section):

        params = parser.items(section)
        db = dict(params)

    else:
        raise Exception(f"Section {section} is not found in the {filename} file.")

    return db
