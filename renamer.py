import os, string

#################################
path = "test/"                  # Will search in ./test/
whitelist = string.printable    # Can be a string of characters instead
replacement_char = "-"          # Character that will be used to replace weird shit
#################################

def renamed(index, filename):
    index = "0" * ( 4 - len(str(index)) ) + str(index)
    result = f"[{index}] "

    for character in filename:
        if character in whitelist:
            result = result + character
        else:
            result = result + replacement_char

    return result

def main():
    file_count = 0

    for filename in os.listdir(path):
        filename_new = renamed(file_count, filename)
        file_count += 1
        os.rename(path+filename, path+filename_new)

main()
