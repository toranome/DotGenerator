import json
import unittest

filename = 'SampleSequenceInput'
inputFile = open('{}.json'.format(filename), 'r')
root = json.load(inputFile)
inputFile.close();
print (root)

class JsonParser:

    def GetGraphFromStructure(container, parent=""):
        isDict = False
        content = []

        if type(container) is dict: # TODO refactor
            isDict = True
            content = container.items()
        elif type(container) is list:
            isDict = False
            content = list(enumerate(container))
        else:
            return {'Nodes': [container], 'Edges': [(parent, container)]}

        if len(list(content)) == 0:
            print ("Empty")
        else:
            return JsonParser.ParseContent(content, parent, isDict)

    def ParseContent(content, parent, isDict=False):
        nodes = []
        edges = []
        for key, value in content:
            if not isDict:
                key = parent
            result = JsonParser.GetGraphFromStructure(
                value,
                key
            )
            nodes.extend(result["Nodes"])
            edges.extend(result["Edges"])
            if isDict:
                nodes.extend([key])
                edges.extend([(parent, key)])
        return {'Nodes': nodes, 'Edges': edges}

    def CreateNodeIds(structure):
        if type(structure) is dict:
            new_dict = {}
            for item in structure.items(): 
                key = item[0]
                value = item[1]
                new_key = "Node_{:04d}_{}".format(0, key)
                new_dict[new_key] = JsonParser.CreateNodeIds(value)
            return new_dict
        elif type(structure) is list:
            new_list = []
            for item in structure:
                new_list.append(JsonParser.CreateNodeIds(item))
            return new_list
        else:
            return "Node_{:04d}_{}".format(0, structure)

    def PrintFormattedStructure():
        pass

graph = JsonParser.GetGraphFromStructure(root)

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

    def test_CreateNodeIds_AllNodesAreRenamed(self):
        expected = {
             'Node_0000_Root':
            {'Node_0000_List':
            ['Node_0000_A',
             'Node_0000_B',
             'Node_0000_C',
            {'Node_0000_Nested List':
            ['Node_0000_1',
             'Node_0000_2',
             'Node_0000_3',
            ['Node_0000_4',
             'Node_0000_5']]}]}}
        result = JsonParser.CreateNodeIds(self.structure)
        print (result)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
