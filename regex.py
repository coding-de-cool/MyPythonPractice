import re

def main():
    print('hello')

    file = open('test_regex.txt') # Create a text file named as test_regex.txt

    for i in file:
        patternMatch = re.search('ruby', i)
        if patternMatch:
            print(patternMatch.group())


if __name__ == '__main__': main()