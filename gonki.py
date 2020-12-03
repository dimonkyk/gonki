import pygame, time
from  pygame import display, event, image, transform
okno = display.set_mode([1500,800])
#подготовка модели
speed = 0
povorot = 0
car_r = pygame.Rect(0,0,100,30)
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
    if povorot<=-315 or povorot>-45:
        car_r.x+=1
    if -225<=povorot<=-135:
        car_r.x-=1
    if -135<=povorot<=-45:
        car_r.y+=1
    if -315<= povorot <=-225:
            car_r.y -= 1

    if case[pygame.K_RIGHT]==1:
        povorot += -1
    if case[pygame.K_LEFT]==1:
        povorot += 1
    povorot=povorot%-360

    #РИСУЕМ КАДР
    okno.fill([0, 0, 0])
    car_pov = transform.rotate(car, povorot)
    okno.blit(car_pov,[car_r.x,car_r.y])
    display.flip()