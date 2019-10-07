# credit: aaron maxwell powerful python
def lines_from_file(f):
    with open(f) as fh:
        yield from fh


def house_records(lines_of_house_data):
    record = {}
    for line in lines_of_house_data:
        if line == '\n':
            yield record
            record = {}
            continue
        k, v = line.split(': ', 1)
        record[k] = v
    yield record

def main():
    lines = lines_from_file('housedata.txt')
#    print(list(lines))

    for house in house_records(lines):
        print(house)



if __name__ == '__main__':
    main()


