import json

filename = 'SampleSequenceInput'
inputFile = open('SampleSequenceInput.json', 'r')
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

outputFile = open('output/SampleSequenceInput.dot', 'w')
outputFile.write('digraph Name {')
outputFile.write('}')
outputFile.close()

renderFile = open('output/render_SampleSequenceInput.bat', 'w')
renderFile.write('dot -Tsvg SampleSequenceInput.dot -o SampleSequenceInput.svg')
renderFile.close()

