def formatearPropiedadesItemInt(item):
    itemFormateado = []
    for propiedad in item:
        try:
            itemFormateado.append(int(propiedad.lstrip()))
            assert isinstance(itemFormateado[-1], int)
        except AssertionError:
            print("la propiedad %s ha de ser integer" % propiedad)
        except ValueError:
            itemFormateado.append(propiedad)
    return itemFormateado


def fromPlaintoList(filePath):
    try:
        if not isinstance(filePath, str):
            raise ValueError
        file = open(filePath, "r")
    except (FileNotFoundError, ValueError):
        return []
    else:
        allTests = []
        for line in file:
            if line.find("day") != -1:
                testDay = []
            elif line == "\n":
                allTests.append(testDay)
            elif line.find("name") != -1:
                numProperties = len(line.split(","))
            else:
                item = line.rstrip().rsplit(",", maxsplit=numProperties - 1)
                item = formatearPropiedadesItemInt(item)
                testDay.append(item)
        file.close()
        return allTests


def writeOnFile(filePath, tests):
    try:
        if not isinstance(filePath, str):
            raise ValueError
        file = open(filePath, "w")
    except ValueError:
        pass
    else:
        for j in range(len(tests[0])):
            file.write("String[][] " + str(tests[0][j][0]).replace(" ", "") + " = { \n")
            for i in range(len(tests)):
                file.write("\t")
                file.write('{"' + str(tests[i][j][0]) + '", ')
                file.write('"' + str(tests[i][j][1]) + '", ')
                file.write('"' + str(tests[i][j][2]) + '"},')
                file.write("\n")
            file.write("};")
            file.write("\n")
            file.write("\n")
    file.close()


if __name__ == "__main__":
    tests = fromPlaintoList("./stderr.gr")
    writeOnFile("listaTests.txt", tests)
