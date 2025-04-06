import pygame, math
pygame.init()
s=pygame.display.set_mode((600,600))
sun=(300,300);t=pygame.time.Clock()
# Distance (pixels, ~150 pixels/AU), initial angle, speed (radians/frame), color
planets=[
    (58, 0, 0.0043*5, (139,69,19)),   # Mercury: 0.39 AU, 88 days
    (108, 0, 0.0017*5, (255,215,0)),  # Venus: 0.72 AU, 225 days
    (150, 0, 0.001*5, (0,191,255)),   # Earth: 1 AU, 365.25 days
    (228, 0, 0.00055*5, (255,69,0))   # Mars: 1.52 AU, 687 days
]
running=True
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:running=False
    s.fill((0,0,0))
    pygame.draw.circle(s,(255,255,0),sun,20)
    for i,(r,angle,speed,color) in enumerate(planets):
        x=sun[0]+r*math.cos(angle);y=sun[1]+r*math.sin(angle)
        pygame.draw.circle(s,color,(int(x),int(y)),5)
        planets[i]=(r,angle+speed,speed,color)
    pygame.display.flip()
    t.tick(60)
pygame.quit()
# Learned: Pygame can animate orbiting planets