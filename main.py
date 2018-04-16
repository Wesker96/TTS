from lxml import etree, objectify
import tts
import os

path = os.getcwd() + "\\xml_files\\XADC_IPC.sym"

sch_block = tts.schematicBlock(path)

print(sch_block.nameBlock)
