#input = "1,2,3,4"
#read_delimited(input)  # --> ["1","2","3","4"]

# line: "bat##cat##rat"
#separator: "##"
#output: ["bat", "cat", "rat"]

def read_delimited(line, separator):
    words = line.split(separator)
    return words
