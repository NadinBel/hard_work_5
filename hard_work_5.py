import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.videos_title = []
        self.user_data_dict = {}
    def log_in(self, nickname, password):
        find_nickname = next((x for x in self.users if getattr(x, 'nickname', None) == nickname), None)
        if hash(find_nickname.password) == hash(password):
            self.current_user = self.nickname
            return self.current_user
        else:
            print('Вход не выполнен')
            self.log_out()
    def register(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = str(password)
        self.age = age
        self.user_data = User(self.nickname, self.password, self.age)
        find_user = next((x for x in self.users if getattr(x, 'nickname', None) == self.nickname), None)
        if find_user == None:
            self.users.append(self.user_data)
            self.user_data_dict[nickname] = (password, age)
            print(f'Пользователь {nickname} успешно зарегистрирован')
            self.log_in(self.nickname, self.password)
        else:
            print(f'Пользователь {nickname} уже существует')
    def log_out(self):
        self.current_user = None
        return self.current_user
    def add(self, *videos):
        self.videos_new = [*videos]
        for x in self.videos_new:
            if getattr(x, 'title', None) not in self.videos_title:
                self.videos.append(x)
                self.videos_title.append(x.title)
    def get_videos(self, find_title):
        self.find_title = find_title
        list_find_title = [x for x in self.videos_title if self.find_title.lower() in x.lower()]
        return list_find_title

    def watch_video(self, title_video):
        current_video = next((x for x in self.videos if getattr(x, 'title', None) == title_video), None)
        def watch_video_time():
            list = [(lambda x: x+1)(x) for x in range(current_video.duration)]
            list.append('Конец видео')
            for x in list:
                print(x, end=" ")
                time.sleep(1)
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif current_video != None and self.current_user != None:
            if current_video.adult_mode and self.user_data_dict.get(self.current_user)[1] >= 18:
                watch_video_time()
            elif current_video.adult_mode and self.user_data_dict.get(self.current_user)[1] < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            elif current_video.adult_mode is False:
                watch_video_time()



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('Де'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_in('vasya_pupkin', 'akdf;akg;g;a')
print(ur.current_user)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)


