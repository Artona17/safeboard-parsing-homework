import task_4
import pytest


@pytest.fixture()
def document_for_testing():
    return {'as-block': 'AS30720 - AS30979', 'type': 'REGULAR', 'descr': 'RIPE NCC ASN block',
            'remarks': ['These AS Numbers are further assigned to network\n',
                        'operators in the RIPE NCC service region. AS\n',
                        'assignment policy is documented in:\n',
                        '<http://www.ripe.net/ripe/docs/asn-assignment.html>\n',
                        'RIPE NCC members can request AS Numbers using the\n',
                        'form located at:\n',
                        '<http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>\n',
                        'data has been transferred from RIPE Whois Database 20050221'],
            'org': 'ORG-AFNC1-AFRINIC',
            'admin-c': 'TEAM-AFRINIC',
            'tech-c': 'TEAM-AFRINIC',
            'mnt-by': 'AFRINIC-HM-MNT',
            'mnt-lower': 'AFRINIC-HM-MNT',
            'changed': ['***@ripe.net 20031001\n',
                        '***@ripe.net 20040421\n',
                        '***@ripe.net 20050202\n',
                        '***@afrinic.net 20050205'],
            'source': 'AFRINIC'}


def test_file_existence():
    assert task_4.file_existence('exaple.txt') == "File not found. Is path right?"


def test_abnormal_extension():
    assert task_4.parse_file('example.rar') == "Incorrect file extension!"


def test_txt_parsing_success(document_for_testing):
    assert task_4.parse_file('test_example.txt')[0] == document_for_testing


def test_zip_parsing_success(document_for_testing):
    assert task_4.parse_file('test_example.zip')[0] == document_for_testing
