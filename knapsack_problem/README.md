Это генератор тестов для того, чтобы отловить wa для задачи "Задача о рюкзаке". 

Для того, чтобы пустить генератор тестов, необходимо сделать следующее:
g++ -std=c++11 -Wall PATH_TO_MY_SOLUTION
python test.py

Можно задать параметры, указав значения n и w:
python test.py --n 8 --w 500

Изначально рекомендуется попробовать найти тест, на котором все плохо, при небольших n и w (так как такой тест проще раздебажить).