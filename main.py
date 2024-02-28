
def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        char_dict = {}

        for word in word_list:
            for char in word:
                char = char.lower()
                if char in char_dict.keys():
                    char_dict[char] += 1 
                else:
                    char_dict[char] = 1

        char_list = [] 

        for key, val in char_dict.items():
            if key.isalpha():
                char_list.append([key,val])

        char_list.sort(reverse=True, key=sort_on)

        print("** Starting Report **")
        print(f"There are {len(file_contents.split())} words")
        
        for item in char_list:
            print(f"The {item[0]} character occurs {item[1]} times.")

        print("** Ending Report **")


def sort_on(dict):
    return dict[1]

main()