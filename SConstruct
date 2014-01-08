
import os
import distutils.sysconfig

env = Environment(SWIGFLAGS=['-python'],
    CPPPATH=[distutils.sysconfig.get_python_inc()],
    SHLIBPREFIX="",
    CFLAGS = '-pipe -std=gnu99 -Wall -Wextra -g',
    ENV = {'PATH' : os.environ['PATH'],
           'TERM' : os.environ['TERM'],
           'HOME' : os.environ['HOME']})

src = ['pyssd1306.c', 'pyssd1306.i', 'i2c/i2c.c', 'ssd1306.c']
env.SharedLibrary('_pyssd1306.so', src)

