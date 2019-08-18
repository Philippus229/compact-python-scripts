import pygame, numpy
def get_pixel(c, z, i=0): return [255*numpy.sqrt(i/127)]*3 if z[0]**2+z[1]**2 > 16 else [0]*3 if i == 127 else get_pixel(c, (z[0]**2-z[1]**2+c[0], 2*z[0]*z[1]+c[1]), i+1)
init, surface = (pygame.init(), pygame.display.set_mode((512, 512)))
while True: frame, flip = (pygame.surfarray.blit_array(surface, numpy.array([[get_pixel((x/128-2.5, y/128-2), (x/128-2.5, y/128-2)) for y in range(512)] for x in range(512)])), pygame.display.flip())
