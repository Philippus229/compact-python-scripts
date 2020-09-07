import numpy as np
import imageio

blocks = np.array([[[np.random.randint(-1,15)*(np.random.uniform(0,1) < np.sqrt(np.sqrt(((x-32.5)**2+(y-32.5)**2)*0.16))-0.8) for z in range(64)] for y in range(64)] for x in range(64)])
texmap = []
for b in range(15):
    c = np.random.randint(0,255,size=3)
    texmap.append(np.array([[np.random.uniform(0.5,1)*c for v in range(16)] for u in range(16)]))

def get_color(sx, sy, cp, col=np.zeros(3), closest=32):
    rd = np.array([sx,sy,1])
    for d in range(3):
        lel = 1/max(abs(rd[d]),0.0000001)
        rd0 = rd*lel
        initial = 1-cp[d]%1 if rd[d] > 0 else cp[d]%1
        rp = cp+rd0*initial-np.array([d<1,d==1,d>1])*(rd[d]<0)
        dist = initial*lel
        while dist < closest:
            bID = blocks[int(rp[0])%64,int(rp[1])%64,int(rp[2])%64]
            if bID:
                col = texmap[bID][(int(16*rp[0])%16,int(16*rp[2])%16) if d == 1 else (int(16*(rp[0]+rp[2]))%16,int(16*rp[1])%16)]*(1-0.2*(d!=1))
                closest = dist
            rp += rd0
            dist += lel
    return col*(1-closest/32)

size = (256,256)
gif = []
frames = 10
for i in range(frames):
    gif.append(np.array([[get_color((2*x-size[0])/size[1], 2*y/size[1]-1, np.array([32.5,32.5,32.5+i/10])) for x in range(size[0])] for y in range(size[1])], dtype=np.uint8))
    print(f"{i+1} of {frames} done...")
imageio.mimsave("test.gif", gif)
