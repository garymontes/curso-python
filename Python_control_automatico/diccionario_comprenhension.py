


def run():
    dicc={i:i**2 for i in range(-10,0) if i%2==0}
    '''for i in range(-10,0):
        if i % 2 ==0:
            dicc[i]=i**2'''
    print(dicc.items())


if __name__=='__main__':
    run()