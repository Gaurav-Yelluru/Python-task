def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def make_rational_num(n,d):
    g=gcd(n,d)
    return (n/g,d/g)

def numer(rational_num):
    return rational_num[0]
    
def denum(rational_num):
    return rational_num[1]
    
def add_rational_num(x, y):
    sum=make_rational_num(numer(x)*denum(y)+numer(y)*denum(x),denum(x)*denum(y))
    return sum

def mul_rational_num(x, y):
    product = make_rational_num(numer(x)*numer(y),denum(x)*denum(y))
    return product

def sub_rational_num(x, y):
    difference = make_rational_num(numer(x)*denum(y)-numer(y)*denum(x),denum(x)*denum(y))
    return difference

def div_rational_num(x, y):
    quotient = make_rational_num(numer(x)*denum(y),numer(y)*denum(x))
    return quotient

def test_make_rational_num():
    x = make_rational_num(5, 6)
    w = make_rational_num(6, 9)
    assert numer(x) == 5 and denum(x) == 6
    assert numer(w) == 2 and denum(w) == 3
    print("test_make_rational_num ...  PASSED")


def test_add_rational_num():
    x = make_rational_num(5, 6)
    y = make_rational_num(2, 3)
    sum_of_x_y = add_rational_num(x, y)
    assert numer(sum_of_x_y) == 3 and denum(sum_of_x_y) == 2
    print("test_add_rational_num ...   PASSED")


def test_mul_rational_num():
    x = make_rational_num(5, 6)
    y = make_rational_num(6, 5)
    product_of_x_y = mul_rational_num(x, y)
    assert numer(product_of_x_y) == 1 and denum(product_of_x_y) == 1
    print("test_mul_rational_num ...   PASSED")


def test_sub_rational_num():
    x = make_rational_num(5, 6)
    diff_of_x_x = sub_rational_num(x, x)
    assert numer(diff_of_x_x) == 0
    print("test_sub_rational_num ...   PASSED")


def test_div_rational_num():
    x = make_rational_num(5, 6)
    y = make_rational_num(0, 1)
    try:
        _z = div_rational_num(x, y)
    except ZeroDivisionError:
        pass
    print("test_div_rational_num ...   PASSED")


def test_all():
    print("Running tests...")
    test_make_rational_num()
    test_add_rational_num()
    test_sub_rational_num()
    test_mul_rational_num()
    test_div_rational_num()


test_all()