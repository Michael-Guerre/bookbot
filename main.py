def main():
    writeReport("books/frankenstein.txt")



def countWord(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(len(file_contents.split()))
    
def countCharacter(file_path):
    char_count = {}
    with open(file_path) as f:
        file_contents = f.read().lower()
        for char in file_contents:
            if (char.isalpha()):
                if(char in char_count) :
                    char_count[char] += 1
                else :
                    char_count[char] = 1
    return char_count

def writeReport(file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{countWord(file_path)} words found in the documents")
    charater_count = countCharacter(file_path)
    charater_count = dict(sorted(charater_count.items(), key=lambda item: item[1],reverse=True))
    print(charater_count)
    for char in charater_count :
        print(f"The '{char} character was found {charater_count[char]} times")
    print("--- End report ---")




main()