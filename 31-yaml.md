# 简介
# YAML 语言（发音 /ˈjæməl/ ）的设计目标，就是方便人类读写。它实质上是一种通用的数据串行化格式。
# 它的基本语法规则如下
1. 大小写敏感
2. 使用缩进表示层级关系
3. 缩进时不允许Tab键，只允许使用空格
4. 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
#表示注释，从这个字符一直到行尾，都会被解析器忽略

# YAML支持的数据结构有三种
1. 对象:键值对的集合，又称为映射(mapping)/哈希(hashes)/字典(dictionary)
2. 数组:一组按次序排列的值，又称为序列(sequence) / 列表(list)
3. 纯量(scalars) : 单个的、不可再分的值

# 对象
# 对象的一组键值对， 使用冒号结构表示
①animal: pets  转成js-->　{ animal: 'pets' }

②YAML也允许另一种写法, 将所有键值对写成一个行内对象
hash: { name: Steve, foo: bar }   转成js--> { hash: { name: 'Steve', foo: 'bar' } }

# 数组
①一组连词先开头的行，构成一个数组
- cat
- Dog
- Golfish
转成js-->[ 'Cat', 'Dog', 'Golfish' ]

②数据结构的子成员是一个数组，则可以则该项下面缩进一个空格
- 
 - Cat
 - Dog
 - Goldfish
转成js-->[ [ 'Cat', 'Dog', 'Goldfish' ] ]

③数组也可以采用行内表示法
animal: [Cat, Dog]  转成js--> { animal: ['Cat', 'Dog'] }

# 复合结构
# 对象和数组可以结合使用，形成复合结构
languages:
 - Ruby
 - Perl
 - Python 
websites: 
 YAML: yaml.org 
 Ruby: ruby-lang.org 
 Python: python.org 
 Perl: use.perl.org 

# 转为js
{ languages: [ 'Ruby', 'Perl', 'Python' ],
  websites: 
   { YAML: 'yaml.org',
     Ruby: 'ruby-lang.org',
     Python: 'python.org',
     Perl: 'use.perl.org' } }

# 纯量
# 字符串
字符换是最常见的，也是最复杂的一种数据类型。
1. 字符串默认不使用引号表示
str: 这是一行字符串      转成js-->{ str: '这是一行字符串' }

2. 如果字符串之中包含空格或特殊字符，需要放在引号之中。
str: '内容: 字符串'      转成js-->{ str: '内容: 字符串'}

3. 单引号和双引号都可以使用，双引号不会对特殊字符转义
s1: '内容\n字符串'
s2: '内容\n字符串'
转成js--> { s1: '内容\\n字符串', s2: '内容\\n字符串'}

4. 单引号之中如果还有单引号，必须连续使用两个单引号转义
str: 'labors''s day'      转成js-->{ str: 'labal\'s day'}

5. 字符串可以写成多行，从第二行开始，必须有一个单空格缩进。换行符会被转为空格
str: 这是一段
 多行
 字符串
转为js-->{ str: '这是一个 多行 字符串'}

6. 多行字符串可以使用|保留换行符，也可以使用>折叠换行
this: |
 Foo
 Bar
that: >
 FOO 
 Bar
转成js-->{ this: 'Foo\nBar\n', that: 'Foo Bar\n' }

7. +表示保留文字末尾的换行，-表示删除字符串末尾的换行

s1: |
 Foo

s2: |+
 Foo



S3: |-
 Foo
转成js-->{ s1: 'Foo\n', s2: 'Foo\n\n\n', s3: 'Foo' }


8. 字符串之中可以插入HTML标记。
message: |
<p style="color: red">\n 段落\n</p>

# 引用
锚点&和别名*，可以用来引用。
defaults: &defaults
  adapter: postgres
  host:    localhost

development:
  database: myapp_development
  <<: *defaults

test:
  database: myapp_development
  <<: *defaults

等同于下面的代码
defaults:
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  adapter:  postgres
  host:     localhost

test:
  database: myapp_test
  adapter:  postgres
  host:     localhost

&用来建立锚点（defaults），<<表示合并到当前数据，*用来引用锚点。

下面是另一个例子:
- &showell Steve 
- Clark 
- Brian 
- Oren 
- *showell
转成js-->[ 'Steve', 'Clark', 'Brian', 'Oren', 'Steve']