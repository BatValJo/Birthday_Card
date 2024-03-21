def draw_background(back_images, wind, back_width, scroll_):
    for x in range(10):
        speed = 0.1
        for ind in back_images:
            wind.blit(ind, (x*back_width - scroll_ * speed, 0))
            speed += 0.2


def draw_city(wind, city_surf_, width, scroll_):
    for i in range(20):
        wind.blit(city_surf_, (i*width - scroll_, 300))

