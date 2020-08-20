# Jinja2模板

#### Flask如何渲染Jinja2模板和传参

1. ##### 如何渲染模板

   - 模板存放在项目文件的 templates 文件夹下
   - 从 flask 中导入 render_template 函数
   - 在视图函数中，使用 render_template 
   - 函数，渲染模板。注意：只需填写模板的名字，不需要填写 templates 这个文件夹的路径

2. ##### 模板传参

   - 如果只有一个或者少量参数，直接在 render_template 函数中添加关键字参数就可以了
   - 如果有多个参数的时候，那么可以把所有的参数存放在字典中，然后再render_template中，使用两个星号（**），把字典转换成关键参数传递进去，这样的代码更方便管理和使用

3. ##### 模板语法

   - 在模板中，如果要使用一个变量，语法是：{{params}}

   - 访问模型中的属性或者是字典，可通过{{params.property}}的形式，或使用{{params[‘property’]}}

   - ###### if判断

     - 语法：
       - {% if xxx %}
         - {% else %}
       - {% endif %}  与python不同的是，需要在if判断结束后在尾部加上{%endif%}
     - if的使用，可以和python中基本相似，可使用 >, <, <=, >=, ==, != 来进行判断，也可通过 and, or, not,() 来进行逻辑合并操作

   - ###### for循环遍历列表和字典

     - 字典的遍历，语法和 python 一致，可使用 items(), keys(), values(), iteritems(), iterkeys(), itervalues

       - {% for k, v in user.items() %}

         - <p>{{ k }}: {{ v }}</p>

       - { % endfor % }

     - 列表的遍历，语法和python一致

       - { % for k, v in user.items() % }

         - <p>{{ k }}: {{ v }}</p>

       - { % endfor% }

   - ###### 过滤器

     -  过滤器可以处理变量，把原始的变量经过处理后再展示出来,作用对象是变量

     - default过滤器

       - {{ avatar|default(‘ xxx ’) }}
       - default过滤器：如果当前变量不存在，这时可指定默认值

     - length过滤器

       - {{ comments|length }}

       - 求列表或者字符串或字典或元祖的长度，类似于python中的len()

       - 常用过滤器：

         - abs(value)：返回一个数值的绝对值。示例：-1|abs`

           ```
           default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。示例：name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。
               ``escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。示例：content|escape或content|e。
               ``first(value)：返回一个序列的第一个元素。示例：names|first
               ``format(value,*arags,**kwargs)：格式化字符串。比如：
           ```

           ```
                 ``{{ "%s" - "%s"|format('Hello?',"Foo!") }}
                 ``将输出：Helloo? - Foo!
               ``last(value)：返回一个序列的最后一个元素。示例：names|last。
           ```

           ```
               ``length(value)：返回一个序列或者字典的长度。示例：names|length。
               ``join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。
               ``safe(value)：如果开启了全局转义，那么safe过滤器会将变量关掉转义。示例：content_html|safe。
               ``int(value)：将值转换为int类型。
               ``float(value)：将值转换为float类型。
               ``lower(value)：将字符串转换为小写。
               ``upper(value)：将字符串转换为小写。
               ``replace(value,old,new)： 替换将old替换为new的字符串。
               ``truncate(value,length=255,killwords=False)：截取length长度的字符串。
               ``striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。
               ``trim：截取字符串前面和后面的空白字符。
               ``string(value)：将变量转换成字符串。
               ``wordcount(s)：计算一个长字符串中单词的个数。
           ```

   ###### 继承和block

   - 继承作用

     - 可把一些公共的代码放在父模板中，避免每个模板写相同的代码
     - 继承语法： { % extends ‘base.html’ % }

   - block

     - 可以让子模版实现自己的需求，复模版需提前定义接口
     - 子模版中的代码，必须要放在block中

   - url链接

     - 使用 url_for(‘视图函数名称’)，可以反转成url

   - 加载静态文件

     - url_for(‘static’, filename=‘路径’)

     - 静态文件，flask会从static文件夹中开始寻找，所以不需要再写 static这个路径

     - ```
       加载CSS文件
       <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
       加载JS文件
       <script src='{{ url_for('static', filename='js/index.js') }}'></script>
       加载图片文件
       <img src="{{ url_for('static', filename='img/timg.jpg') }}" alt="无法加载">
       ```

