# Задание 2

### Задача
```
    Напишите запрос к базе данных, который для причин "Validation error", "Balance error", "AntiFraud"
    выводит имя пользователя, его идентефикатор, дату изменения статуса и причину, для последних пользователей,
    перешедших из статуса "ok" в статус "error" по каждой из перечислинных причин, своей последней по времени записью.
    Порядок id в таблице user_status_history может не совпадать с порядком полей created.
    Статус пользователя в таблице user может не совпадать с последним изменением статуса в таблице user_status_history.
```

### Данные

<details>
  <summary> Таблицы </summary>   

    CREATE TABLE user (
        id          bigint          default nextval('user_id_seq'::regclass) not null   constraint user_pkey    primary key,
        status      text		    not null,
        name        text 	        not null,
        type        int             not null,
        created     timestamp       default now()         
    );

    CREATE TABLE user_status_history (
        id              bigint          default nextval('user_status_history_id_seq'::regclass) not null    constraint user_status_history_pkey     primary key,
        user_id         bigint          not null    constraint user_status_history_user_id_fkey     references "user",
        old_status      text            not null,
        new_status      text            not null,
        reason          text            default ''::text    not null,
        created         timestamp	    default now()
    );
</details>

<br />

<details>
    <summary> Заполнение таблиц </summary>   

    INSERT INTO public.user (id, status, name, type, created) VALUES (1, 'block', 'Дорохов Максим Николаевич', 1, '2010-01-12 04:07:06.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (2, 'reg', 'Ильина София Викторовна', 2, '2016-12-26 07:52:55.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (3, 'ok', 'Шаров Лев Антонович', 3, '2015-07-29 06:05:26.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (4, 'ok', 'Троицкая Мария Никитична', 4, '2014-09-17 04:34:19.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (5, 'error', 'Родионова Даниэла Макаровна', 1, '2013-11-05 21:51:45.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (6, 'error', 'Богомолова Мария Давидовна', 2, '2010-02-08 09:42:35.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (7, 'invalid_status', 'Лапин Георгий Фёдорович', 3, '2017-06-20 18:21:05.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (8, 'ok', 'Климова Ева Богдановна', 4, '2019-02-20 15:02:14.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (9, 'reg', 'Зимин Кирилл Святославович', 1, '2019-07-30 22:26:29.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (10, 'error', 'Зайцева Николь Вячеславовна', 2, '2011-03-08 22:57:34.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (11, 'block', 'Вдовина Полина Марковна', 3, '2011-04-26 22:08:06.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (12, 'ok', 'Скворцов Егор Ибрагимович', 4, '2013-03-27 09:01:12.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (13, 'block', 'Кондратьева Кира Никитична', 1, '2018-03-15 21:31:01.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (14, 'block', 'Петрова Ульяна Данииловна', 2, '2016-06-23 20:24:51.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (15, 'error', 'Козлова Елена Данииловна', 5, '2020-06-23 20:23:42.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (16, 'error', 'Симонов Сергей Семонович', 4, '2020-04-19 16:23:42.000000');
    INSERT INTO public.user (id, status, name, type, created) VALUES (17, 'error', 'Поморцева Ольга Владиславовна', 5, '2020-01-19 08:17:41.000000');

    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (105, 17, 'reg', 'error', 'Can''t write DB', '2020-01-19 08:19:41.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (98, 17, 'new', 'reg', 'Start registration', '2020-01-19 08:17:41.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (71, 16, 'error', 'error', 'AntiFraud', '2020-04-25 13:18:40.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (100, 16, 'ok', 'error', 'Validation error', '2020-04-20 13:16:40.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (82, 16, 'reg', 'ok', 'Success registartion', '2020-04-19 16:27:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (77, 16, 'new', 'reg', 'Start registration', '2020-04-19 16:23:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (70, 15, 'ok', 'error', 'Error registartion', '2029-06-23 20:25:44.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (66, 15, 'reg', 'ok', 'Success registartion', '2029-06-23 20:25:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (102, 15, 'new', 'reg', 'Start registration', '2029-06-23 20:23:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (75, 14, 'ok', 'error', 'AntiFraud', '2016-09-14 10:15:54.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (93, 14, 'reg', 'ok', 'Success registartion', '2016-06-23 20:34:51.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (67, 14, 'new', 'reg', 'Start registration', '2016-06-23 20:24:51.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (74, 13, 'ok', 'error', 'Validation error', '2018-08-19 14:31:00.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (62, 13, 'reg', 'ok', 'Success registartion', '2018-03-15 21:37:01.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (80, 13, 'new', 'reg', 'Start registration', '2018-03-15 21:31:01.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (63, 12, 'reg', 'ok', 'Success registartion', '2013-03-27 09:13:12.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (101, 12, 'new', 'reg', 'Start registration', '2013-03-27 09:01:12.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (97, 11, 'ok', 'block', 'User delete account', '2011-10-28 17:17:06.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (84, 11, 'reg', 'ok', 'Success registartion', '2011-04-26 23:08:06.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (83, 11, 'new', 'reg', 'Start registration', '2011-04-26 22:08:06.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (61, 10, 'ok', 'error', 'AntiFraud', '2020-04-23 13:16:40.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (68, 10, 'error', 'ok', 'Support help', '2020-04-21 13:16:40.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (79, 10, 'ok', 'error', 'Validation error', '2020-04-20 13:16:40.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (69, 10, 'reg', 'ok', 'Success registartion', '2020-04-19 16:24:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (104, 10, 'new', 'reg', 'Start registration', '2020-04-19 16:23:42.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (73, 9, 'new', 'reg', 'Start registration', '2019-07-30 22:26:29.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (96, 8, 'reg', 'ok', 'Success registartion', '2019-07-20 15:02:14.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (92, 8, 'new', 'reg', 'Start registration', '2019-02-20 15:02:14.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (91, 7, 'ok', 'error', 'Balance error', '2017-08-23 15:15:05.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (95, 7, 'reg', 'ok', 'Success registartion', '2017-06-20 18:25:07.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (65, 7, 'new', 'reg', 'Start registration', '2017-06-20 18:21:05.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (106, 6, 'ok', 'error', 'Balance error', '2010-06-08 05:45:33.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (94, 6, 'new', 'reg', 'Start registration', '2010-02-08 09:42:35.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (103, 6, 'reg', 'ok', 'Success registartion', '2010-02-08 09:42:35.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (90, 5, 'ok', 'error', 'Validation error', '2013-12-11 17:51:45.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (89, 5, 'reg', 'ok', 'Success registartion', '2013-11-05 21:54:45.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (86, 5, 'new', 'reg', 'Start registration', '2013-11-05 21:51:45.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (88, 4, 'reg', 'ok', 'Success registartion', '2014-09-17 04:39:19.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (81, 4, 'new', 'reg', 'Start registration', '2014-09-17 04:34:19.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (85, 3, 'reg', 'ok', 'Success registartion', '2015-07-29 07:05:26.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (78, 3, 'new', 'reg', 'Start registration', '2015-07-29 06:05:26.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (87, 2, 'new', 'reg', 'Start registration', '2016-12-26 07:52:55.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (64, 1, 'ok', 'block', 'User delete account', '2010-04-12 06:10:06.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (72, 1, 'new', 'reg', 'Start registration', '2010-01-12 04:07:06.000000');
    INSERT INTO public.user_status_history (id, user_id, old_status, new_status, reason, created) VALUES (76, 1, 'reg', 'ok', 'Success registartion', '2010-01-12 04:07:06.000000');

</details>

## Запрос к базе данных:
``` SQL
    SELECT u.name, u.id, h.created, h.reason 
    FROM public.user as u 
    JOIN public.user_status_history as h 
    ON u.id = h.user_id 
    WHERE h.reason in ('Validation error', 'Balance error', 'AntiFraud') 
    GROUP BY h.reason 
    ORDER BY h.created DESC;
```
