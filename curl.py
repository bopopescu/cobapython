import pycurl
from io import BytesIO
import xml.etree.ElementTree as ET
# import xml.etree.cElementTree as ETC
import xml.dom.minidom as xml
import requests

def modem_token():
    b_obj = BytesIO()
    crl = pycurl.Curl()

    crl.setopt(crl.URL, 'http://192.168.8.1/api/webserver/SesTokInfo')
    crl.setopt(crl.CUSTOMREQUEST, "GET")
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    crl.close()
    result = b_obj.getvalue()
    xml = ET.fromstring(result)
    return xml

def modem_dialup():
    result_obj = BytesIO()
    prereq = modem_token()
    session = prereq.find('SesInfo').text
    token = prereq.find('TokInfo').text
    # file = ET.parse("Nyalain.xml")
    file = open("Nyalain.xml","r")

    dial = pycurl.Curl()
    dial.setopt(dial.URL, 'http://192.168.8.1/api/dialup/mobile-dataswitch')
    dial.setopt(dial.POST, 1)
    dial.setopt(dial.POSTFIELD, file)
    dial.setopt(dial.RETURNTRANSFER, 1)
    dial.setopt(dial.HTTPHEADER, ['Content-Type: text/xml; charset=UTF-8',
                                  'Cookie: %s' % session,
                                  '__RequestVerificationToken: %s' % token])
    dial.setopt(dial.WRITEDATA, result_obj)
    dial.perform()
    dial.close()
    result = result_obj.getvalue()
    xml = ET.fromstring(result)
    print(xml)


    # req = ET.Element("request")
    # ET.SubElement(req, "dataswitch").text = "0"
    # tree = ET.ElementTree(req)
    # tree.write("Matiin.xml")

    # headers = {'Content-Type': 'text/xml; charset=UTF-8', 'Cookie': session, '__RequestVerificationToken': token}
    #
    # dial = pycurl.Curl()
    # dial.setopt(dial.URL, 'http://192.168.8.1/api/dialup/mobile-dataswitch')


    # dial.setopt(dial.HTTPHEADER, headers)

    # dial.setopt(dial.WRITEDATA, a_obj)

    # dial.perform()
    # dial.close()
    # result = a_obj.getvalue()
    # xml = ET.fromstring(result)
    # print(xml)
    # print(ET.tostring(tree,'utf-8'))


    # headers = {'Content-Type': 'text/xml; charset=UTF-8','Cookie': session, '__RequestVerificationToken': token}
    #
    # r = requests.post("http://192.168.8.1/api/dialup/mobile-dataswitch", headers=headers)
    # print(r)


modem_dialup()