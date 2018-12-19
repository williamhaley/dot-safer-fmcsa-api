#!/usr/bin/env python3

from urllib import request, parse
from bs4 import BeautifulSoup, element
import re
import sys
import argparse

url = 'https://safer.fmcsa.dot.gov/query.asp'

fields = {
    'LegalName': 'Legal Name:',
    'DBAName': 'DBA Name:',
    'PhysicalAddress': 'Physical Address:',
    'Phone': 'Phone:',
    'MailingAddress': 'Mailing Address:',
    'DOTNumber': 'USDOT Number:',
    'StateId': 'State Carrier ID Number:',
    'MCMXFF': 'MC/MX/FF Number(s):',
    'DUNS': 'DUNS Number:',
}

def get(id):
    params = {
        'searchType': 'ANY',
        'query_type': 'queryCarrierSnapshot',
        'query_param': 'USDOT',
        'query_string': id
    }

    data = parse.urlencode(params).encode()
    req = request.Request(url, data=data)
    resp = request.urlopen(req, timeout=2)
    return resp.read()

def parse_html(html_bytes):
    soup = BeautifulSoup(html_bytes, 'html.parser')
    hint = soup.find(string=re.compile('Entity'))

    if hint == None:
        return

    table = hint.find_parent('table')

    if table == None:
        return

    for key, field in fields.items():
        print(key, find_field(table, field))

def find_field(table, label):
    th = table.find(string=label)
    tr = th.find_parent('tr')
    td = tr.find('td')

    # Could be briefer with list comprehension, but I find this more readable
    pieces = []
    for child in td.descendants:
        if type(child) != element.NavigableString:
            continue
        if child.string == None:
            continue
        normalized = child.string.replace('\\r\\n', '').strip()
        if normalized == '':
            continue
        pieces.append(normalized)

    return ' '.join(pieces)

def parse_local_file(file_path):
    with open(file_path, 'rb') as f:
        html_bytes = f.read()
        parse_html(html_bytes)

def query_by_id(id):
    try:
        html_bytes = get(id)
        parse_html(html_bytes)
    except:
        print('an error occurred')

def save_by_id(id):
    try:
        html_bytes = get(id)
        with open('./saved/' + id + '.html', 'wb') as f:
            f.write(html_bytes)
    except:
        print('an error occurred')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse information from US DOT API')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--parse', dest='file', type=str, help='Parse data from a local file')
    group.add_argument('--query', dest='id', type=str, help='USDOT id to query live from the API and print the parsed data')

    args = parser.parse_args()

    if args.file:
        parse_local_file(args.file)
    elif args.id:
        query_by_id(args.id)
    else:
        parser.print_help(sys.stdout)
