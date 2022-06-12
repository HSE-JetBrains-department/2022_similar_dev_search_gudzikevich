# Поиск похожих разработчиков - Гудзикевич Максим

## Шаги разработки

 - Научиться работать с VCS

 - Научиться работать с GiHub API
     - Извлечение истории коммитов и информации о каждом из них 
 
 - Изучить доступные репозитории и склонировать необходимые
     - Промаркировать репозитории для каждого разработчика, классифицировать по языкам и тд
 
 - Научиться извлекать информацию из исходного кода
     - Использование [enry](https://github.com/go-enry/go-enry) для классификации языков программирования
     - Использование [tree-sitter](https://github.com/tree-sitter/tree-sitter) для извлечения сущностей из кода
     - Нам нужно AST-дерево исходного кода
   
 - Составить структуру будущего проекта
     - Получение репозиториев 
     - Работа с 1 репозиторием 
     - Классификация языков программирования в файле 
     - Извлечение импортов, имен переменных из файла с кодом 
     - Группировка информации для каждого из разработчиков из нескольких репозиториев 
     - Поиск ближайших соседей для векторов 
     - Тесты, CI, docker, etc - для доп баллов

 - Определить похожесть - для этого смотрим на то, какие identifiers использовали разработчики, какие языки
     - Также сравнить и выбрать метрики схожести между разработчиками
 
## Оценка за курс

 - Оценка складывается следующим образом: (github_api * 0.15 + git * 0.25 + enry * 0.2 + tree_sitter * 0.25 + similar_dev_search * 0.15) * 8 + (tests + style_check + docker) * 2/3
 - Каждый пункт - одно из домашних заданий


##  Первая итерация - учимся извлекать сущности на scikit-learn:
```shell
!git clone https://github.com/scikit-learn/scikit-learn 

PYTHONPATH=./ python3 devsearch/cli/run.py extract-commit-info /mnt/c/Users/maxma/Documents/GitHub/scikit-learn devsearch/preprocessing/output.jsonl
```

## Для получения распределения stargazers:
```shell
PYTHONPATH=./ python3 devsearch/cli/run.py extract-stargazers scikit-learn/scikit-learn ./ -t $token
```