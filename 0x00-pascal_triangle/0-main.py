#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_isosceles_triangle(triangle):
    """
    Print an isosceles triangle from the Pascal's Triangle
    """
    max_width = len(" ".join(map(str, triangle[-1])))  # Calc max width

    for row in triangle:
        row_str = " ".join(map(str, row))
        padding = (max_width - len(row_str)) // 2
        formatted_row = " " * padding + row_str + " " * padding
        print(formatted_row)


if __name__ == "__main__":
    print_isosceles_triangle(pascal_triangle(10))
