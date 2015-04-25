import json
import unittest

filename = 'SampleSequenceInput'
inputFile = open('{}.json'.format(filename), 'r')
root = json.load(inputFile)
inputFile.close();
print (root)

class JsonParser:

    nodes = []
    edges = []

    def ParseStructure(content, parent="", tab=""):
        if type(content) is dict:
            if len(content.keys()) == 0:
                print ("Empty Dict")
            else:
                results = []
                for item in content.items():
                    print ("{}{} -> {}".format(tab, parent, item[0]))
                    results.append(JsonParser.ParseStructure(
                        item[1],
                        item[0],
                        tab+"  ")
                    )
                return results
        elif type(content) is list:
            if len(content) == 0:
                print ("Empty List")
            else:
                results = []
                for item in content:
                    results.append(JsonParser.ParseStructure(
                        item,
                        parent,
                        tab)
                    )
                return results
        else:
            print ("{}{} -> {} : {}".format(
                tab,
                parent,
                content,
                type(content))
            )

    def PrintNodes():
        pass

    def PrintEdges():
        pass

#outputFile = open('output/SampleSequenceInput.dot', 'w')
#outputFile.write('digraph Name {')
#outputFile.write('}')
#outputFile.close()

#renderFile = open('output/render_SampleSequenceInput.bat', 'w')
#renderFile.write('dot -Tsvg SampleSequenceInput.dot -o SampleSequenceInput.svg')
#renderFile.close()

class TestJsonParser(unittest.TestCase):

    def setUp(self):
        self.structure = {'Root':
                        {'List':
                            [1,2,3,{'Nested List':
                                [1,2,3,[4,5]]}]}}

    def test_ParseStructure_AllNodesAreParsed(self):
        result = JsonParser.ParseStructure(self.structure)
        self.assertEqual(list, type(result))

if __name__ == '__main__':
    unittest.main()
