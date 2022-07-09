import re
from argparse import ArgumentParser






def breakWords(word: str):
    words = []
    if(word.find('.') != -1):
        words.append(word.split('.'))
    if(word.find('-') != -1):
        words.append(word.split('-'))
    if(word.find('_') != -1):
        words.append(word.split('_'))
    if(word.find('/') != -1):
        words.append(word.split('/'))
    if(word.find('\\') != -1):
        words.append(word.split('\\'))
    if(word.find(' ') != -1):
        words.append(word.split(' '))
    if(word.find('#') != -1):
        words.append(word.split('#'))
    if(word.find('@') != -1):
        words.append(word.split('@'))
    if(word.find('%') != -1):
        words.append(word.split('%'))
    return word

def upperCaseCheck(word: str):
    words = re.findall('[A-Z][^A-Z]*', word)
    return words

def main():
    parser = ArgumentParser("Detect Bad Names")
    parser.add_argument("name", help="The name to be verified", type=str, nargs='+')
    args = parser.parse_args()
    brWords = []
    ucWords = []
    for name in args.name:
        brWords.append(breakWords(name))
        ucWords.append(upperCaseCheck(name))
    print(brWords)
    input('')
    print(ucWords)
        



if __name__ == '__main__':
    main()