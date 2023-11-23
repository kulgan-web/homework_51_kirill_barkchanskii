from random import randint


class CatDB:
    name = ""
    age = 1
    satiety = 40
    happy = 40
    cat_list = [{"name": name,"age": age, "satiety": satiety, "happy": happy}]
    is_sleeping = False

    @classmethod
    def get_name(cls, name_cat):
        cls.cat_list[0]['name'] = name_cat.capitalize()

    @classmethod
    def __get_chance_of_happiness(cls):
        chance = randint(1,3)
        if chance == 3:
            cls.cat_list[0]['happy'] = 0

    @classmethod
    def __check_cat_happy(cls):
        if cls.cat_list[0]['happy'] > 100:
            cls.cat_list[0]['happy'] = 100
        elif cls.cat_list[0]['happy'] < 0:
            cls.cat_list[0]['happy'] = 0


    @classmethod
    def __check_cat_satiety(cls):
        if cls.cat_list[0]['satiety'] > 100:
            cls.cat_list[0]['satiety'] = 100
        elif cls.cat_list[0]['satiety'] < 0:
            cls.cat_list[0]['satiety'] = 0

    @classmethod
    def play_cat(cls):
        if cls.is_sleeping == False:
            cls.cat_list[0]['happy'] += 15
            cls.cat_list[0]['satiety'] -= 10
            CatDB.__get_chance_of_happiness()
            CatDB.__check_cat_happy()
            CatDB.__check_cat_satiety()
        elif cls.is_sleeping == True:
            cls.is_sleeping = False
            cls.cat_list[0]['happy'] -= 5
            CatDB.__check_cat_happy()
            CatDB.__check_cat_satiety()

    @classmethod
    def sleep_cat(cls):
        cls.is_sleeping = True

    @classmethod
    def feed_cat(cls):
        if cls.is_sleeping == False:
            cls.cat_list[0]['happy'] += 5
            cls.cat_list[0]['satiety'] += 15
            CatDB.__check_cat_happy()
            if cls.cat_list[0]['satiety'] > 100 and cls.cat_list[0]['happy'] < 100:
                cls.cat_list[0]['happy'] -= 35
                CatDB.__check_cat_satiety()
            elif cls.cat_list[0]['satiety'] > 100 and cls.cat_list[0]['happy'] == 100:
                cls.cat_list[0]['happy'] -= 30
                CatDB.__check_cat_satiety()
        elif cls.is_sleeping == True:
            pass
