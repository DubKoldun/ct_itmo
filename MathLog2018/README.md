# Mathematical Logic


## [Задача 1. Разбор утверждения](ParseExpression)

```
Имя входного файла: стандартный ввод
Имя выходного файла: стандартный вывод
Ограничение по времени: 2 секунды
Ограничение по памяти: 256 мегабайт
```

На вход вашей программе дается утверждение в следующей грамматике:


```haskell
⟨Файл⟩ ::= ⟨Выражение⟩
⟨Выражение⟩ ::= ⟨Дизъюнкция⟩|⟨Дизъюнкция⟩->⟨Выражение⟩
⟨Дизъюнкция⟩ ::= ⟨Конъюнкция⟩|⟨Дизъюнкция⟩|⟨Конъюнкция⟩
⟨Конъюнкция⟩ ::= ⟨Отрицание⟩|⟨Конъюнкция⟩&⟨Отрицание⟩
⟨Отрицание⟩ ::= !⟨Отрицание⟩|⟨Переменная⟩| (⟨Выражение⟩)
⟨Переменная⟩ ::= (A-Z) {A-Z, 0-9, '}
```

Имена переменных не содержат пробелов. Между символами оператора `->` нет пробелов. В
остальных местах пробелы могут присутствовать. Символы табуляции и возврата каретки должны
трактоваться как пробелы.
Вам требуется написать программу, разбирающую утверждение и строящую его дерево разбора,
и выводящую полученное дерево в единственной строке без пробелов в следующей грамматике:


```haskell
⟨Файл⟩ ::= ⟨Вершина⟩
⟨Вершина⟩ ::= (⟨Знак⟩,⟨Вершина⟩,⟨Вершина⟩)
            | (!⟨Вершина⟩)
            | ⟨Переменная⟩
⟨Знак⟩ ::= ->, |, &
⟨Переменная⟩ ::= (A-Z) {A-Z, 0-9, '}
```

### Формат входных данных

В единственной строке входного файла дано утверждение в грамматике из условия. Размер
входного файла не превышает 100 КБ.

### Формат выходных данных

В единственной строке выходного файла выведите дерево разбора утверждения без пробелов.

### Примеры

стандартный ввод

```haskell
!A&!B->!(A|B)
```

стандартный вывод

```haskell
(->,(&,(!A),(!B)),(!(|,A,B)))
```

---

стандартный ввод

```haskell
P1'->!QQ->!R10&S|!T&U&V
```

стандартный вывод

```haskell
(->,P1',(->,(!QQ),(|,(&,(!R10),S),(&,(&,(!T),U),V))))
```

---

## [Задача 2. Минимизация доказательства](MinimizingProof)

```
Имя входного файла: стандартный ввод
Имя выходного файла: стандартный вывод
Ограничение по времени: 15 секунд
Ограничение по памяти: 512 мегабайт
```

На вход вашей программе дается доказательство утверждения в следующей грамматике:

```haskell
⟨Файл⟩ ::= ⟨Контекст⟩ |- ⟨Выражение⟩ \n ⟨Строка⟩*
⟨Контекст⟩ ::= ⟨Выражение⟩ [,⟨Выражение⟩]*
⟨Строка⟩ ::= ⟨Выражение⟩\n
⟨Выражение⟩ ::= ⟨Выражение⟩&⟨Выражение⟩
              | ⟨Выражение⟩|⟨Выражение⟩
              | ⟨Выражение⟩->⟨Выражение⟩
              | !⟨Выражение⟩
              | (⟨Выражение⟩)
              | ⟨Переменная⟩
⟨Переменная⟩ ::= (A-Z) {A-Z, 0-9, '}
```

Операторы `&` и `|` левоассоциативны. Оператор `->` правоассоциативен.
Операторы в порядке уменьшения приоритета: `!`, `&`, `|`, `->`.
Имена переменных не содержат пробелов. Между символами одного оператора нет пробелов (`->` и `|-`).
 В остальных местах пробелы могут присутствовать. Символы табуляции и возврата
каретки должны трактоваться как пробелы.
Требуется проверить доказательство на корректность. Если оно неверно, выведите `«Proof is
incorrect»`. Иначе минимизируйте и проаннотируйте доказательство.
Под минимизацией доказательства подразумевается создание нового доказательства такого, что:

+ Новое доказательство доказывает то же самое утверждение в том же самом контексте

+ Строки нового доказательства являются подпоследовательностью строк исходного доказатель-
ства

+ В новом доказательстве ни одно выражение не встречается в нескольких строках

+ В новом доказательстве нет неиспользуемых выражений, т.е. все выражения, кроме последне-
го, должны использоваться одним или более применением правила Modus Ponens.

Под аннотированием доказательства подразумевается:

+ Все строки должны быть пронумерованы

+ Каждая строка должна содержать пояснение, как она была выведена:

```
    Аксиома: номер аксиомы
    Предположение: номер предположения
    Modus Ponens: номера строк, в которых записаны выражения, используемые для вывода
    выражения в текущей строке
```

### Формат входных данных

Во входном файле задано доказательство в приведенной выше грамматике. Размер входного
файла не превышает 10 МБ.

### Формат выходных данных

Если данное доказательство является некорректным, в единственной строке выходного файла
должна быть запись `«Proof is incorrect»`.
Иначе в файле должно быть минимизированное проаннотированое корректное доказательство.
Каждая строка, кроме последней, должна быть использована хотя бы в одной аннотации Modus
Ponens. Подробный формат аннотаций смотрите в примерах.


### Примеры

стандартный ввод
```haskell
|- A -> A
A & A -> A
A -> A -> A
A -> (A -> A) -> A
A & A -> A
(A -> A -> A) -> (A -> (A -> A) -> A) -> A -> A
(A -> (A -> A) -> A) -> A -> A
A & A -> A
A -> A
```

стандартный вывод
```haskell
|- (A -> A)
[1. Ax. sch. 1] (A -> (A -> A))
[2. Ax. sch. 1] (A -> ((A -> A) -> A))
[3. Ax. sch. 2] ((A -> (A -> A)) -> ((A -> ((A -> A) -> A)) -> (A -> A)))
[4. M.P. 3, 1] ((A -> ((A -> A) -> A)) -> (A -> A))
[5. M.P. 4, 2] (A -> A)
```

---

стандартный ввод
```haskell
A->B, !B |- !A
A->B
!B
!B -> A -> !B
A -> !B
(A -> B) -> (A -> !B) -> !A
(A -> !B) -> !A
!A
```

стандартный вывод
```haskell
(A -> B), !B |- !A
[1. Hypothesis 1] (A -> B)
[2. Hypothesis 2] !B
[3. Ax. sch. 1] (!B -> (A -> !B))
[4. M.P. 3, 2] (A -> !B)
[5. Ax. sch. 9] ((A -> B) -> ((A -> !B) -> !A))
[6. M.P. 5, 1] ((A -> !B) -> !A)
[7. M.P. 6, 4] !A
```

---

стандартный ввод
```haskell
A, C |- B'
B'
```
стандартный вывод

`Proof is incorrect`

---

## Задача 3. Формальная арифметика

```
Имя входного файла: стандартный ввод
Имя выходного файла: стандартный вывод
Ограничение по времени: 15 секунд
Ограничение по памяти: 1024 мегабайт
```

Напишите программу, проверяющую доказательство в формальной арифметике на корректность.

```haskell
⟨Файл⟩ ::= ⟨Заголовок⟩\n⟨Доказательство⟩
⟨Заголовок⟩ ::= |-⟨Выражение⟩
⟨Доказательство⟩ ::= {⟨Выражение⟩'\n'}+
⟨Выражение⟩ ::= ⟨Дизъюнкция⟩|⟨Дизъюнкция⟩->⟨Выражение⟩
⟨Дизъюнкция⟩ ::= ⟨Конъюнкция⟩|⟨Дизъюнкция⟩|⟨Конъюнкция⟩
⟨Конъюнкция⟩ ::= ⟨Унарное⟩|⟨Конъюнкция⟩&⟨Унарное⟩
⟨Унарное⟩ ::= ⟨Предикат⟩|!⟨Унарное⟩|⟨Переменная⟩|(⟨Выражение⟩)|(@|?)⟨Переменная⟩.⟨Выражение⟩
⟨Переменная⟩ ::= (a-z)
⟨Предикат⟩ ::= (A-Z)|⟨Терм⟩=⟨Терм⟩
⟨Терм⟩ ::= ⟨Слагаемое⟩|⟨Терм⟩+⟨Слагаемое⟩
⟨Слагаемое⟩ ::= ⟨Умножаемое⟩|⟨Слагаемое⟩*⟨Умножаемое⟩
⟨Умножаемое⟩ ::= ⟨Переменная⟩|(⟨Терм⟩)|0|⟨Умножаемое⟩'

```
Коды символов: символ апострофа (’) — 0x27, вертикальная черта (|) — 0x7c.

### Формат входных данных

Если доказательство корректно, проаннотируйте его. Первая строка должна повторять строку
из входного файла, остальные строки доказательства должны быть предварены аннотацией:

`• [n. Ax. sch. k], где n — номер выражения, а k — номер схемы аксиом: либо число от 1 до 12, либо A9.`
`• [n. Ax. k], где k — значение от A1 до A8.`
`• [n. M.P. k, l], [n. ?@-intro k] — для правил вывода.`

Аннотации перечислены в порядке предпочтения: если выражение может быть обосновано, до-
пустим, как аксиома `A8` или как `M.P.`, в ответе должно быть указано `Ax. A8`.
В случае пересечения аксиом/схем (упражнение: бывает ли такое?) указывайте аксиому/схему минимальным номером; арифметические аксиомы/схемы идут после логических.

Если выражение может быть получено при
помощи одного правила вывода несколькими способами, предпочтение должно отдаваться наиболее поздним ссылкам в лексикографическом порядке: `M.P. 10,1` предпочтительнее `M.P. 1,10`.

В выражениях должны быть расставлены все скобки в точности по одному разу (т.е. скобки
вокруг всех унарных и бинарных выражений, кроме апострофа).

Если доказательство некорректно, выведите одну из следующих строк, в зависимости от типа
ошибки. Ваша программа должна находить первое некорректное выражение в доказательстве, и
для него указывать тип ошибки с минимальным номером (в соответствии со списком ниже):

`1. Expression n: variable v occurs free in ?@-rule.`
`2. Expression n: variable v is not free for term t in ?@-axiom.`
`3. Expression n is not proved.`
`4. The proof proves different expression.`

Все строки доказательства, предшествующие некорректной, должны быть проаннотированы.
Столь подробные правила введены для того, чтобы упростить проверяющую программу: ответ
сравнивается с эталонным на равенство; будьте внимательны.


### Примеры

стандартный ввод

```haskell
|-a+0=a
(((a)+0))=a
(@y.y+0*0’=y)->(?x.@y.x=y)
```

стандартный вывод

```haskell
|-((a+0)=a)
[1. Ax. A5] ((a+0)=a)
Expression 2: variable x is not free for term (y+(0*0’)) in ?@-axiom.
```

------

стандартный ввод

```haskell
|-A->W->A
A->B->A&B
A->A|B
(A->P)->(B->P)->(A|B->P)
(@a.a+0=a)->b+0=b
0=0->(?x.x=0)
a=b->a=c->b=c
a=b->a’=b’
a’=b’->a=b
0=0&(@x.x=x->x’=x’)->x=x
A->W->A
```

стандартный вывод

```haskell
|-(A->(W->A))
[1. Ax. sch. 5] (A->(B->(A&B)))
[2. Ax. sch. 6] (A->(A|B))
[3. Ax. sch. 8] ((A->P)->((B->P)->((A|B)->P)))
[4. Ax. sch. 11] ((@a.((a+0)=a))->((b+0)=b))
[5. Ax. sch. 12] ((0=0)->(?x.(x=0)))
[6. Ax. A1] ((a=b)->((a=c)->(b=c)))
[7. Ax. A2] ((a=b)->(a’=b’))
[8. Ax. A3] ((a’=b’)->(a=b))
[9. Ax. sch. A9] (((0=0)&(@x.((x=x)->(x’=x’))))->(x=x))
[10. Ax. sch. 1] (A->(W->A))
```

------

## [Задача 4.Полнота исчисления высказываний](Completness)
```
Имя входного файла: стандартный ввод
Имя выходного файла: стандартный вывод
Ограничение по времени: 15 секунд
Ограничение по памяти: 512 мегабайт
```

На вход вашей программе дается утверждениев грамматике из предыдущих заданий. От вас требуется найти:

+ Набор гипотез Γ1 со следующими свойствами:
    - Γ1 состоит только из переменных
    - Γ1 ⊢ α

В этом случае вам нужно вывести доказательство Γ1 ⊢ α.

+ Если такого набора гипотез не нашлось, то нужно найти наименьший набор гипотез Γ2:
    - Γ2 состоит только из отрицаний переменных
    - Γ2 ⊢ ¬α

В этом случае вам нужно вывести доказательство Γ2 ⊢ ¬α.

+ Если и такого набора гипотез не нашлось, то выведите `«:(»`.
Если среди предыдущих случаев существует несколько подходящих наборов гипотез (а если такие наборы есть, то их всегда бесконечно много), то требуется вывести любой подходящий набор наименьшего размера.

### Формат входных данных

Во входном файле задано утверждение. Размер входного файла не превышает 50 байт. Количество различных переменных, входящих в α, не превосходит 3.

### Формат выходных данных

Если требуемого набора гипотез не существует, в единственной строке выведите `«:(»`. Иначе выведите требуемое в условии доказательство, используя грамматику из предыдущих заданий.

### Примеры

#### стандартный ввод
```haskell
!A
```

#### стандартный вывод
```haskell
:(
```

---

#### стандартный ввод
```haskell
A -> A & B
```

#### стандартный вывод
```haskell
B |- A -> A & B
B
B -> A -> B
A -> B
A -> B -> A & B
(A -> B) -> (A -> B -> A & B) -> A -> A & B
(A -> B -> A & B) -> A -> A & B
A -> A & B
```
