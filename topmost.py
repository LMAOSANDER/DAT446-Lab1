import sys
import urllib.request
import wordfreq


def is_url(string):
    if string[:7] == "http://" or string[:8] == "https://":
        return True
    return False


def main():
    url = False
    args = sys.argv
    stop_words_file = args[1]
    in_string = args[2]
    n = int(args[3])

    if is_url(in_string):
        in_file = urllib.request.urlopen(in_string).read().decode("utf8").splitlines()
        url = True
    else:
        in_file = open(in_string)

    word_list = wordfreq.tokenize(in_file)
    word_dict = wordfreq.countWords(word_list, stop_words=stop_words_file)
    wordfreq.printTopMost(frequencies=word_dict, n=n)

    if url:
        urllib.request.urlcleanup()
    else:
        in_file.close()


if __name__ == "__main__":
    main()