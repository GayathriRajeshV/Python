def words(a,b):
    new_a=b[:2]+ a[2:]
    new_b=a[:2]+ b[2:]

    return new_a + ' ' +new_b
print(words('abcd','hijk'))
