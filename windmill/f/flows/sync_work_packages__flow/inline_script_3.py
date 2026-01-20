# import wmill


def main(x: object):
    result = []
    for i in x:
        for j in i:
            result.append(j)
    return result