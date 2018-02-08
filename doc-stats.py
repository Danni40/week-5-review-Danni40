def getTextFile():
    fileName = input("Enter the text file name: ")
    textFile = open( fileName, 'r' )
    return fileName, textFile

def outputCountResults( fileName, lineCount, wordCount, charCount, nonWordCount ):
    print()
    print( "******* {} *******".format( fileName ))
    print( "Line Count: {}".format( lineCount ))
    print( "Word Count: {}".format( wordCount ))
    print( "Char Count: {}".format( charCount ))
    print( "Non-Article Words: {}".format( nonWordCount))
    
def countCharacters(line):
    charCount = 0
    for c in line:
        if not c.isspace():
            charCount = charCount + 1
    return charCount
    
def countWords( line ):
    words = line.split()
    return len( words )
    
def nonArticles(line):
    nonWords = 0
    for words in line.split():
        if words != 'the' and words != 'an' and words != 'a' and words != 'aN' and words != 'AN':
            nonWords = nonWords + 1
    return nonWords
    #nonWords=line.split()
    #if nonWords != 'an' or nonWords != 'aN' or nonWords != 'AN' or nonWords != 'a' or nonWords != 'the':    
        #return len(nonWords)
    
def countDocStats( docFile ):
    lineCount = 0
    totalCharacters = 0
    totalWords = 0
    totalNonWords = 0
    for line in docFile:
        lineCount = lineCount + 1
        totalCharacters = totalCharacters + countCharacters( line )
        totalWords = totalWords + countWords( line )
        totalNonWords = totalNonWords + nonArticles(line)
    return lineCount, totalCharacters, totalWords, totalNonWords

def main():
    fileName, textFile = getTextFile()
    lineCount, totalCharacters, totalWords, totalNonWords = countDocStats( textFile )
    outputCountResults( fileName, lineCount, totalWords, totalCharacters, totalNonWords )
    
main()