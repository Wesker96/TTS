from lxml import etree, objectify
import sys

class schematicBlock:

    nameBlock = ''

    widthMainBlock = 0
    heightMainBlock = 0

    listInput = []
    listOutput = []

    paddingMainBlockX = 0
    paddingMainBlockY = 0
    paddingPins = 0

    widthBusRect = 0
    heightBusRect = 0

    lengthPin = 0

    def __init__(self, path):
        root = self.openXML(path)

        self.getParameterMainBlock(root)
        self.getParameterPins(root)

    def openXML(self, path):
        try:
            tree = etree.ElementTree(file=path)
            root = tree.getroot()

            return root
        except IOError:
            sys.exit('Error (schematicBlock/openXML): impossible find file or incorrect of path to file.')

    def getParameterMainBlock(self, root):
        for child0 in root:
            if(child0.tag == 'graph'):
                for child1 in child0:
                    if(child1.tag == 'rect'):
                        parameter_main_block = child1.items()

                        for param in parameter_main_block:
                            if(param[0] == 'width'):
                                self.widthMainBlock = param[1]
                            elif(param[0] == 'height'):
                                self.heightMainBlock = param[1]
                            elif(param[0] == 'x'):
                                self.paddingMainBlockX = param[1]
                            elif(param[0] == 'y'):
                                self.paddingMainBlockY = param[1]
                    elif(child1.tag == 'text'):
                        self.nameBlock = child1.text

    def getParameterPins(self, root):
        for child0 in root:
            if(child0.tag == 'pin'):
                parameter_pin = child0.items()
                polarity = False
                nameIO = ''

                for param in parameter_pin:
                    if(param[1] == 'Input'):
                        polarity = True
                    elif(param[1] == 'Output'):
                        polarity = False
                    elif(param[0] == 'name'):
                        nameIO = param[1]

                if(polarity):
                    self.listInput.append(nameIO)
                else:
                    self.listOutput.append(nameIO)

    def createBlock(self):
        self.nameBlock = 'NewBlock'
        self.paddingMainBlockX = 32
        self.paddingMainBlockY = 32
        self.paddingPins = 50
        self.widthBusRect = 64
        self.heightBusRect = 24
        self.lengthPin = 32

    def addPin(self, name, polarity, dimension):
        if(polarity == "input"):
            if(dimension > 1):
                self.listInput.append(name + "({0}:0)".format(dimension - 1))
            else:
                self.listInput.append(name)
        elif(polarity == "output"):
            if(dimension > 1):
                self.listOutput.append(name + "({0}:0)".format(dimension - 1))
            else:
                self.listOutput.append(name)

class transformBlock:
    