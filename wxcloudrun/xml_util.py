import datetime
import xml.etree.ElementTree as ET


# Define the class for generating XML
class XMLGenerator:
    def __init__(self, root_tag):
        self.root = ET.Element(root_tag)

    def add_element(self, tag, text):
        element = ET.SubElement(self.root, tag)
        element.text = text

    def generate_xml(self, to_user, from_uer, content):
        self.add_element('ToUserName', to_user)
        self.add_element('FromUserName', from_uer)
        self.add_element('CreateTime', str(datetime.datetime.now().timestamp()))
        self.add_element('MsgType', 'text')
        self.add_element('text', content)
        return ET.tostring(self.root)


if __name__ == '__main__':
    # Create an instance of the XMLGenerator class
    xml_generator = XMLGenerator('xml')

    # Add four fields to the XML
    xml_generator.add_element('ToUserName', 'value1')
    xml_generator.add_element('FromUserName', 'value2')
    xml_generator.add_element('CreateTime', datetime.datetime.now())
    xml_generator.add_element('MsgType', 'text')
    xml_generator.add_element('ContentContent', 'value4')

    # Generate the XML
    xml = xml_generator.generate_xml()

    # Print the generated XML
    print(xml)
