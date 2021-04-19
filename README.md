# safeboard-parsing-homework
Написать функцию парсинга текстового файла (`parse_file`), которая в качестве единственного аргумента принимает путь к файлу и возвращает набор словарей, содержащих данные. Работать с функцией предполагается только следующим образом:

```python
def parse_file(path):
    ...


def load_data(path):
    parsed_data = parse_file(path)

    for document in parsed_data:
        ...
        # load document to database (or do something else)
```

Файл представляет собой набор данных типа ключ-значение, ключ от значения отделен двоеточием.
Из значений должны быть удалены лишние пробелы, многострочные значения должны быть объеденены в одну строку с сохранением переносов (но не отступов).
Данные с повторяющимися ключами считаются многострочными, т.е. в исходном файле две следующие записи идентичны:

```
foo: bar
     baz

foo: bar
foo: baz
```

Каждый документ в файле разделен как минимум одной пустой строкой, строки, начинающиеся с символа `#` означают комментарии и должны игнорироваться.

Пример исходных данных находится в файле `example.txt`.

Пример одного из результирующих словарей после обработки:

```python
{'as-block': 'AS30720 - AS30979',
 'type': 'REGULAR',
 'descr': 'RIPE NCC ASN block',
 'remarks': 'These AS Numbers are further assigned to network\n' \
            'operators in the RIPE NCC service region. AS\n' \
            'assignment policy is documented in:\n' \
            '<http://www.ripe.net/ripe/docs/asn-assignment.html>\n' \
            'RIPE NCC members can request AS Numbers using the\n' \
            'form located at:\n' \
            '<http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>\n' \
            'data has been transferred from RIPE Whois Database 20050221',
 'org': 'ORG-AFNC1-AFRINIC',
 'admin-c': 'TEAM-AFRINIC',
 'tech-c': 'TEAM-AFRINIC',
 'mnt-by': 'AFRINIC-HM-MNT',
 'mnt-lower': 'AFRINIC-HM-MNT',
 'changed': '***@ripe.net 20031001\n' \
            '***@ripe.net 20040421\n' \
            '***@ripe.net 20050202\n' \
            '***@afrinic.net 20050205',
 'source': 'AFRINIC'}
```

Ограничения:

* Python 3.7+;
* только стандартная библиотека.

За что будут бонусы:

* если файл будет корректно открываться и закрываться даже в случае ексепшена;
* если код будет структурирован (короткие и понятные функции, хорошее именование, комментарии где нужно);
* если можно будет парсить большие файлы (больше размера ОЗУ);
* если будут указаны аннотации типов;
* если код будет оформлен по pep8;
* если можно будет парсить данные из gzip-архива без распаковки.
