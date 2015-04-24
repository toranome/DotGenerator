import json

filename = 'SampleSequenceInput'
inputFile = open('{}.json'.format(filename), 'r')
root = json.load(inputFile)
inputFile.close();

nodes = []
edges = []

def PrintStructure(content, parent="", tab=""):
    if type(content) is dict:
        if len(content.keys()) == 0:
            print ("Empty Dict")
        else:
            for item in content.items():
                print ("{}{} -> {}".format(tab, parent, item[0]))
                PrintStructure(item[1], item[0], tab+"  ")
    elif type(content) is list:
        if len(content) == 0:
            print ("Empty List")
        else:
            for item in content:
                PrintStructure(item, parent, tab)
    else:
        print ("{}{} -> {} : {}".format(tab, parent, content, type(content)))

PrintStructure(root)

outputFile = open('output/SampleSequenceInput.dot', 'w')
outputFile.write('digraph Name {')
outputFile.write('}')
outputFile.close()

renderFile = open('output/render_SampleSequenceInput.bat', 'w')
renderFile.write('dot -Tsvg SampleSequenceInput.dot -o SampleSequenceInput.svg')
renderFile.close()

