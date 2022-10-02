
from typing import Dict, Type 

class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories:float,
                ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки:{self.training_type:.3f};'
                   f'Длительность: {self.duration:.3f}ч.;'
                   f'Дистанция: {self.distance:.3f}км.;'
                   f'Ср.скрость: {self.speed:.3f}км/ч;'
                   f'Потрачено ккал{self.calories:.3f}.')
        return message
    

class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65
    def get_name(self):
        return 'Тренеровка'
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
         self.action = action
         self.duration = duration
         self.weight = weight        
        
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance_km: float = self.action * self.LEN_STEP / self.M_IN_KM    
        return distance_km

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance_km = self.get_distance()
        speed: int = distance_km/self.duration
        return speed 
        
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.get_name(), self.duration,
                           self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())
        return info              


class Running(Training):
    """Тренировка: бег."""
    def get_name(self):
        return 'Бег'
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action,duration,weight)

    def get_spent_calories(self) -> float:
        coeff_1 = 18
        coeff_2 = 20
        minutes = 60
        speed = self.get_mean_speed()
        spent_calories: float = (coeff_1 * speed - coeff_2) * self.weight/ self.M_IN_KM * self.duration * minutes
        return spent_calories



class SportsWalking(Training):
    def get_name(self):
        return 'Спортивная ходьба'
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action,duration,weight)
        self.height = height
        speed = self.get_mean_speed()

    def get_spent_calories(self) -> float:
        coeff_3 = 0.035
        coeff_4 = 0.029
        speed = self.get_mean_speed()
        minutes = 60
        spent_calories = (coeff_3 * self.weight + (speed**2 //self.height) * coeff_4 * self.weight) * self.duration * minutes
        return spent_calories


class Swimming(Training):
    def get_name(self):
        return 'Плавание'
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: float,
                 ) -> None:
        super().__init__(action,duration,weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.lenght_pool * self.count_pool/self.M_IN_KM/self.duration
        return speed

    def get_spent_calories(self) -> float:
        speed = self.get_mean_speed()
        coeff_5 = 1.1
        coeff_6 = 2
        spent_calories = (speed + coeff_5) * coeff_6 * self.weight
        return spent_calories
       

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train: Dict[str, Type[Training]] = {'SWM': Swimming,
     'RUN': Running,
     'WLK': SportsWalking}
    return train[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

