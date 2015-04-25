import json

willWriteFiles = True
willWriteBatchFiles = False
outputFolder = 'output'
fileName = 'SampleSequenceInput'

inputFileName = '{}.json'.format(fileName)
inputFile = open(inputFileName, 'r')
root = json.load(inputFile)
inputFile.close();

contents = root["Sequence"]
streams = contents["Streams"]
connections = contents["Connections"]
frames = contents["Frames"]

print (len(streams))
print (len(connections))
print (len(frames))

for s in streams:
    print (s)

for c in connections:
    print (c)

for f in frames:
    print (f)

if willWriteFiles:
    outputFileName = '{}/{}.dot'.format(outputFolder, fileName)
    outputFile = open(outputFileName, 'w')
    outputFile.write('digraph {} {{'.format(fileName))
    outputFile.write('nodesep=1')
    outputFile.write('compound=true')
    outputFile.write('}')
    outputFile.close()

    if willWriteBatchFiles:
        renderFileName = '{}/{}.bat'.format(outputFolder, fileName)
        renderFile = open(renderFileName, 'w')
        renderFile.write('dot -Tsvg {0}.dot -o {0}.svg', fileName)
        renderFile.close()

