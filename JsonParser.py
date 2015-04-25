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
                nodes = []
                edges = []
                for item in content.items():
                    print ("{}{} -> {}".format(tab, parent, item[0]))
                    result = JsonParser.ParseStructure(
                        item[1],
                        item[0],
                        tab+"  "
                    )
                    edges.extend(result["Edges"])
                    nodes.extend([item[0]])
                    nodes.extend(result["Nodes"])
                    edges.extend([(parent, item[0])])
                return {'Nodes': nodes, 'Edges': edges}
        elif type(content) is list:
            if len(content) == 0:
                print ("Empty List")
            else:
                nodes = []
                edges = []
                for item in content:
                    result = JsonParser.ParseStructure(
                        item,
                        parent,
                        tab
                    )
                    nodes.extend(result["Nodes"])
                    edges.extend(result["Edges"])
                return {'Nodes': nodes, 'Edges': edges}
        else:
            print ("{}{} -> {} : {}".format(
                tab,
                parent,
                content,
                type(content))
            )
            return {'Nodes': [content], 'Edges': [(parent, content)]}

    def PrintNodes():
        pass

    def PrintEdges():
        pass

if False:
    outputFile = open('output/SampleSequenceInput.dot', 'w')
    outputFile.write('digraph Name {')
    outputFile.write('}')
    outputFile.close()

    renderFile = open('output/render_SampleSequenceInput.bat', 'w')
    renderFile.write('dot -Tsvg SampleSequenceInput.dot -o SampleSequenceInput.svg')
    renderFile.close()

class TestJsonParser(unittest.TestCase):

    def setUp(self):
        self.structure = {'Root':
                             {'List':
                                 ['A','B','C',{'Nested List':
                                     ['1','2','3',['4','5']]}]}}

    def test_ParseStructure_ParserReturnsCorrectDict(self):
        # TODO convert node and edge lists into sets
        result = JsonParser.ParseStructure(self.structure)
        self.assertEqual(dict, type(result))
        self.assertIn('Nodes', result.keys())
        self.assertIn('Edges', result.keys())

    def test_ParseStructure_AllNodesAreParsed(self):
        expected = [
            'Root',
            'List', 'A', 'B', 'C',
            'Nested List', '1', '2', '3', '4', '5'
        ]
        result = JsonParser.ParseStructure(self.structure)
        self.assertEqual(expected, result["Nodes"])

    def test_ParseStructure_AllEdgesAreParsed(self):
        expected = [
            ('List', 'A'),
            ('List', 'B'),
            ('List', 'C'),
            ('Nested List', '1'),
            ('Nested List', '2'),
            ('Nested List', '3'),
            ('Nested List', '4'),
            ('Nested List', '5'),
            ('List', 'Nested List'),
            ('Root', 'List'),
            ('', 'Root')    # TODO remove this
        ]
        result = JsonParser.ParseStructure(self.structure)
        self.assertEqual(expected, result["Edges"])

if __name__ == '__main__':
    normal = 1
    more = 2
    unittest.main(verbosity = normal)
