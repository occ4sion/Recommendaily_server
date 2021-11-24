# recomMEndation: Yet another approach to solving the user cold start problem.
#### recomMEndation a rcommendation system for M&E (media and entertainment) contend which offers another approach to solving the problem of cold user start, by using mechanics to accelerate the collection and markup of data.
This is a server part of application - models, data and description.
___
Этапы разработки:
- [x] 1. Стратегия.
  - [x] 1. Обозначение цели и задач.
  - [x] 2. Обзор конкурентов.
  - [x] 3. Приблизительная оценка данных, моделей, метрик и взаимодействия с пользователем.
- [x] 2. EDA.
  - [x] 1. Определение выбросов, пустых строк и столбцов.
  - [x] 2. Определение стратегии работы с пропущенными и категориальными значениями.
- [x] 3. Baseline.
  - [x] 1. Апробация алгоритмов на сырых данных.
  - [x] 2. Тьюнинг параметров и оценка точности.
  > Точность 72% на 50 экземплярах.
- [ ] 4. Feature engineering.
  - [x] 1. Создание стратегии для обработки категориальных признаков.
  - [x] 2. Feature extraction.
  - [x] 3. Тестирование нового подхода на различных пользователях.
  > Точность ~90% на тренировочных данных и 80-90% на тестовых данных при 100 экземпляров.
  - [ ] 4. Добавление признаковых описаний из дополнительных источников.
- [ ] 5. Pipeline.
  - [x] 1. Обертка и оптимизация методов обработки данных.
  - [ ] 2. Пайплайн для данных.
  - [ ] 3. Пайплайн для пользователя.
- [ ] 6. Models.
  - [ ] 1. Ансамблирование.
  - [ ] 2. Тьюнинг параметров.
  - [ ] 3. Выбор лучших/лучшей модели.
- [ ] 7. Production.
  - [ ] 1. Выгрузка на сервер.
  - [ ] 2. Написание API.
  - [ ] 3. Настройка резервного копирования.
- [ ] 8. Client.
  - [ ] 1. Создание карты взаимодействия с пользователем.
  - [ ] 2. Определение потоков данных.
  - [ ] 3. Определение и попытка устранение bottleneck'ов.
  - [ ] 4. Тестирование.
  - [ ] 5. Релиз.
- [ ] 9. Улучшение.
  - [ ] 1. Добавление датасетов.
  - [ ] 2. Добавление признаковых описаний.
