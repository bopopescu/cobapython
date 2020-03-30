import pycurl
import time
from io import BytesIO
import xml.etree.ElementTree as ET
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

def modem_connect(dial):
    url = "http://192.168.8.1/api/dialup/mobile-dataswitch"
    prereq = modem_token()
    session = prereq.find('SesInfo').text
    token = prereq.find('TokInfo').text

    payload = "<request>\n\t<dataswitch>%s</dataswitch>\n</request>"  % dial
    headers = {
      'Content-Type': 'text/xml; charset=UTF-8',
      'Cookie': session,
      '__RequestVerificationToken': token
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    time.sleep(3)

def modem_profile(apn):
    url = "http://192.168.8.1/api/dialup/profiles"
    prereq = modem_token()
    session = prereq.find('SesInfo').text
    token = prereq.find('TokInfo').text

    payload = "<request>\r\n" \
              "<Delete>0</Delete>\r\n" \
              "<SetDefault>0</SetDefault>\r\n" \
              "<Modify>2</Modify>\r\n" \
              "<Profile>\r\n" \
              "<Index>1</Index>\r\n" \
              "<IsValid>1</IsValid>\r\n" \
              "<Name>General</Name>\r\n" \
              "<ApnIsStatic>1</ApnIsStatic>\r\n" \
              "<ApnName>%s</ApnName>\r\n" \
              "<DialupNum>*99#</DialupNum>\r\n" \
              "<Username></Username>\r\n" \
              "<Password></Password>\r\n" \
              "<AuthMode>0</AuthMode>\r\n" \
              "<IpIsStatic>0</IpIsStatic>\r\n" \
              "<IpAddress>0.0.0.0</IpAddress>\r\n" \
              "<Ipv6Address></Ipv6Address>\r\n" \
              "<DnsIsStatic></DnsIsStatic>\r\n" \
              "<PrimaryDns></PrimaryDns>\r\n" \
              "<SecondaryDns></SecondaryDns>\r\n" \
              "<PrimaryIpv6Dns></PrimaryIpv6Dns>\r\n" \
              "<SecondaryIpv6Dns></SecondaryIpv6Dns>\r\n" \
              "<ReadOnly>0</ReadOnly>\r\n" \
              "<iptype></iptype>\r\n" \
              "</Profile>\r\n" \
              "</request>"  % apn
    headers = {
        'Content-Type': 'text/xml; charset=UTF-8',
        'Cookie': session,
        '__RequestVerificationToken': token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
    time.sleep(3)

def modem_main(apn):
    print(apn)
    modem_connect(0)
    modem_profile(apn)
    modem_connect(1)

modem_main(apn="supersabarbrn6")