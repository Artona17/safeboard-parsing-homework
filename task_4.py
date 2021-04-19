import re
from zipfile import ZipFile


class Parser:
    def __init__(self, file, encoding='utf-8'):
        self.__encoding = encoding
        self.__file = file
        self.__documents = []
        self.__document = {}

    def parsing_the_line(self, line):
        if line[0] == '#':
            pass
        elif str.isspace(line):
            for key_document in self.__document:
                if isinstance(self.__document[key_document], list):
                    self.__document[key_document][-1] = self.__document[key_document][-1].rstrip()
            self.__document = {}
            self.__documents.append(self.__document)
        else:
            if '\r' in line:
                line = re.sub(r"\r", "", line)
            if ': ' in line:
                key, value = re.split(r':\s+', line)
            else:
                key = list(self.__document)[-1]
                value = line.lstrip()
            if key in self.__document:
                if isinstance(self.__document[key], list):
                    self.__document[key].append(value)
                else:
                    temp = self.__document[key] + '\n'
                    self.__document[key] = list()
                    self.__document[key].extend([temp, value])
            else:
                self.__document.update({key: value.strip()})

    def parsing_file_or_zipfile(self, type='txt'):
        for line in self.__file:
            if type == 'zip':
                line = line.decode(self.__encoding)
            self.parsing_the_line(line)
        if {} in self.__documents:
            self.__documents.remove({})
        return self.__documents


def file_existence(path):
    try:
        error = str()
        open(path, 'r').close()
    except FileNotFoundError:
        error = "File not found. Is path right?"
    return error


def parse_file(path):
    if path.split('.')[-1] == 'zip':
        error = file_existence(path)
        if error:
            return error
        zipfile = ZipFile(path)
        with zipfile.open(name=zipfile.namelist()[0], mode='r') as file:
            parser = Parser(file)
            documents = parser.parsing_file_or_zipfile(type='zip')
        return documents
    elif path.split('.')[-1] == 'txt':
        error = file_existence(path)
        if error:
            return error
        with open(path, 'r') as file:
            parser = Parser(file)
            documents = parser.parsing_file_or_zipfile()
        return documents
    else:
        error = 'Incorrect file extension!'
        return error


print(parse_file('example.txt'))
