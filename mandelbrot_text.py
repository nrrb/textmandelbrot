

def draw_fractal(n_columns=40, n_rows=20,
                 min_real=-1.5, min_imag=-1.0, max_real=1.0, max_imag=1.0,
                 max_iterations=200, render_chars='abcdefghijklmnopqrstuvw    '):
    '''
    This renders a Mandelbrot set fractal in text mode.
    http://en.wikipedia.org/wiki/Mandelbrot_set

    Defaults:

    def draw_fractal(n_columns=80, n_rows=40,
                     min_real=-1.0, min_imag=-1.0, max_real=1.0, max_imag=1.0,
                     max_iterations=200, render_chars = 'abcdefghijklmnopqrstuvw    ')

    n_columns = Integer. number of text columns
    n_rows = Integer. number of rows
    ((min_real,min_imag),(max_real,max_imag)) = Floats. these parameters designate the rendering window
        on the complex plane.
    max_iterations = Integer. how many iterations each point is allowed to run.
    render_chars = String. The characters used to represent the escape iterations for each point.
    '''
    m_mapping = dict(zip(range(len(render_chars)), render_chars))

    def dist(z):
        return (z*z.conjugate()).real
    fractal = []
    for y in range(n_rows):
        imag = (max_imag-min_imag)*y/float(n_rows) + min_imag
        fractal.append([])
        for x in range(n_columns):
            real = (max_real-min_real)*x/float(n_columns) + min_real
            c = complex(real, imag)
            z = 0j
            for escape in range(max_iterations):
                z = z*z + c
                if dist(z) > 1:
                    break
            fractal[y].append(escape)
    for line in fractal:
        new_line = map(lambda x: x/((max_iterations/len(m_mapping))+1), line)
        print ''.join([m_mapping[val] for val in new_line])

if __name__ == "__main__":
    from random import randint

    # All Defaults
    print '\nAll Defaults:\n'
    draw_fractal()
    # Try an alternate character set
    random_string = ''.join([chr(randint(ord(' '), ord('~'))) for i in range(randint(5, 15))])
    print '\nRandom character set "%s":\n' % random_string
    draw_fractal(render_chars=random_string, n_columns=80, n_rows=30)
    # Zoom in to something interesting
    # Try these:
    # min_real,max_real,min_imag,max_imag = 0.26, 0.27, 0.0, 0.01
    # min_real,max_real,min_imag,max_imag = -0.76, -0.74, 0.01, 0.03
    # min_real,max_real,min_imag,max_imag = -1.26, -1.24, 0.01, 0.03
    # min_real,max_real,min_imag,max_imag = -1.0, -0.5, -0.25, 0.25
    # min_real,max_real,min_imag,max_imag = -0.8, -0.7, 0.0, 0.25
    min_real, max_real, min_imag, max_imag = -0.75, -0.7, 0.1, 0.25
    # min_real,max_real,min_imag,max_imag = -0.75, -0.7, 0.2, 0.25
    # min_real,max_real,min_imag,max_imag = -0.74, -0.72, 0.23, 0.25
    # min_real,max_real,min_imag,max_imag = -0.735, -0.73, 0.237, 0.24
    print '\nZoomed into %s-%s:\n' % (complex(min_real, min_imag), complex(max_real, max_imag))
    draw_fractal(min_real=min_real, max_real=max_real, min_imag=min_imag, max_imag=max_imag, max_iterations=400)
