class Solution:
    def formatPage(self, paragraphs, width):
        result = [] 
        # adding first line
        result.append("*"*width)
        paragraphsSize = len(paragraphs)
        to_add = []
        # Loop to correctly subdivide lines
        for line in paragraphs:
            temp_line = ""
            index = 0
            indexLine = 0
            lineSize = len(line)
            indexWord = 0
            while indexWord < lineSize:
                if temp_line and len(temp_line)+len(line[indexWord]) > width:
                    temp_line = temp_line.strip()
                    to_add.append(temp_line)
                    temp_line = "" 
                temp_line += line[indexWord]
                temp_line += " "
                if len(temp_line) >= width or indexWord >= len(line)-1:
                    temp_line = temp_line.strip()
                    to_add.append(temp_line)
                    temp_line = ""              
                indexWord += 1 
                
        for line in to_add:
            formated_line = line.center(width)
            formated_line = "*"+formated_line+"*"
            result.append(formated_line)
            
        
            
        #adding last line
        result.append("*"*width)
        return result

if __name__ == '__main__':
    solution = Solution()
    paragraphs = [["hello","word"],["How", "are", "you","?"],["please visit","link","call everyone","and","text your", "neighbours"]]
    width = 16
    result = solution.formatPage(paragraphs, width)
    print(result)

'''
# Code challenge 
# text lengh per line has to be max of "width"
# first line and last line has to composed only by '*'
# each line has to begin and end with '*'
# if the line text length does not add to the value of "width", it has to be completed with empty spaces
# if there is an even number of empty spaces, add the extra one on the right
# input example: paragraphs = [["hello","word"],["How", "are", "you","?"],["please visit","link","call everyone","and","text your", "neighbours"]]  width = 16
output example: result = [
    "****************"
    '*   hello word   *'
    '* How are you ?  *'
    '*  please visit  *'
    '*      link      *'
    '* call everyone  *'
    '* and text your  *'
    '*   neighbours   *'
    "****************"
]
'''