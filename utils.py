def convert(basesize: float, newsize: float, originalsize: float = 297) -> float:  # noqa: E501
    return (newsize*basesize)/originalsize


def percent(basesize: float, newpercent: float) -> float:
    return (basesize * newpercent)/100


if __name__ == "__main__":
    from reportlab.lib.pagesizes import A4
    print()
    print(convert(A4[1], 6.11))
    print(percent(A4[1], 50))


# 297 - 810
# 6,11 - X

# X * 210 = 1 * 105
# X = 105 / 210