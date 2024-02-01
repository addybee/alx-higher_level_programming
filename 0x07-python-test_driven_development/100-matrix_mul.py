#!/usr/bin/python3
""" contains function that multiplies 2 matrices:
"""


def matrix_mul(m_a, m_b):
    """matrix multiplication

    Args:
        m_a (list of lists): matrix of first argument
        m_b (list of lists): matrix of second argument

    Raises:
        TypeError: m_a must be a list or m_b must be a list
        ValueError: m_a can't be empty or m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size
        TypeError: each row of m_b must be of the same size
        ValueError: m_a and m_b can't be multiplied


    Returns:
        list: dot product of two matrix
    """
    if type(m_a) is not list or type(m_b) is not list:
        msg = "m_a" if type(m_a) is not list else "m_b"
        raise TypeError(f"{msg} must be a list")

    if len(m_a) == 0 or len(m_b) == 0:
        msg = "m_a" if len(m_a) == 0 else "m_b"
        raise ValueError(f"{msg} can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if (len(row) != len(m_a[0])):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if (len(row) != len(m_b[0])):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    ans = [[0 for i in range(len(m_b[0]))] for a in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for m in range(len(m_b)):
                ans[i][j] += m_a[i][m] * m_b[m][j]

    return ans
