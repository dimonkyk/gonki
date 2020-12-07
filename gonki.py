import pygame, time
from  pygame import display, event, image, transform, draw
okno = display.set_mode([1500,800])
#подготовка модели
speed = 0
povorot = 0
trass = pygame.Rect(170,150,1200,500)
car_r = pygame.Rect(0,0,100,50)
#подгатовка к рисование

car = image.load("kartinki/car1.png")
car = transform.scale(car,[100,50])
car = transform.flip(car,True,True)
while True:
    print(povorot)
    case=pygame.key.get_pressed()
    time.sleep(1/60)
    sobitiya = event.get()
    for forr in sobitiya:
        if forr.type == pygame.KEYDOWN:
            if forr.key == 27:
                exit()

    #движение модели
    if case[pygame.K_SPACE]==1:
        speed = 2
    else:
        speed = 1


    if case[pygame.K_RIGHT]==1:
        povorot += -1
    if case[pygame.K_LEFT]==1:
        povorot += 1
    if povorot<=-315 or povorot>-45:
        car_r.x+=speed
    if -225<=povorot<=-135:
        car_r.x-=speed
    if -135<=povorot<=-45:
        car_r.y+=speed
    if -315<= povorot <=-225:
            car_r.y -= speed


    povorot=povorot%-360
    car_pov = transform.rotate(car, povorot)
    car_r.w = car_pov.get_width()
    car_r.h = car_pov.get_height()
    if car_r.colliderect(trass):
        car_r.y = 10
        car_r.x =10


    #РИСУЕМ КАДР
    okno.fill([0, 0, 0])
    draw.rect(okno,[255,255,255],trass)

    okno.blit(car_pov,[car_r.x,car_r.y])
    draw.rect(okno,[184,45,205],car_r,5)
    display.flip()