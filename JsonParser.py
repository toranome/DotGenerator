import json
import unittest

filename = 'SampleSequenceInput'
inputFile = open('{}.json'.format(filename), 'r')
root = json.load(inputFile)
inputFile.close();
print (root)

class JsonParser:

    def GetGraphFromStructure(container, parent=""):
        if type(container) is dict: # TODO refactor
            content = container.items()
            if len(list(content)) == 0:
                print ("Empty")
            else:
                return JsonParser.ParseContent(content, parent, True)
        elif type(container) is list:
            content = list(enumerate(container))
            if len(list(content)) == 0:
                print ("Empty")
            else:
                return JsonParser.ParseContent(content, parent, False)
        else:
            return {'Nodes': [container], 'Edges': [(parent, container)]}

    def ParseContent(content, parent, addNode=False):
        nodes = []
        edges = []
        for key, value in content:
            result = JsonParser.GetGraphFromStructure(
                value,
                key
            )
            nodes.extend(result["Nodes"])
            edges.extend(result["Edges"])
            if addNode:
                nodes.extend([key])
                edges.extend([(parent, key)])
        return {'Nodes': nodes, 'Edges': edges}

    def CreateNodeIds():
        pass

    def PrintFormattedStructure():
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

    def test_GetGraphFromStructure_ParserReturnsCorrectDict(self):
        # TODO convert node and edge lists into sets
        result = JsonParser.GetGraphFromStructure(self.structure)
        self.assertEqual(dict, type(result))
        self.assertIn('Nodes', result.keys())
        self.assertIn('Edges', result.keys())

    def test_GetGraphFromStructure_AllNodesAreParsed(self):
        expected = [
            'A',
            'B',
            'C',
            '1',
            '2',
            '3',
            '4',
            '5',
            'Nested List',
            'List',
            'Root'
        ]
        result = JsonParser.GetGraphFromStructure(self.structure)
        self.assertEqual(expected, result["Nodes"])

    def test_GetGraphFromStructure_AllEdgesAreParsed(self):
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
        result = JsonParser.GetGraphFromStructure(self.structure)
        self.assertEqual(expected, result["Edges"])

if __name__ == '__main__':
    normal = 1
    more = 2
    unittest.main(verbosity = normal)
