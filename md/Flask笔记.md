



# Flask笔记



### app.run

 	1. debug=True
      	1. 进入调试模式
      	2. 项目可以自动重新加载
      	3. debugger会被激活
           	1. 会提供一个pin
           	2. 当程序crash的时候，可以在网页上输入pin进行调试
	2. port
        	1. 制定一个端口
	3. host
        	1. 制定运行的ip
	4. example
        	1. app.run()
                  	2. if __name__ == ‘__name__’: app.run(debug=True/Flase, --host=localhost, port=xxxx)
                	3. ... ...more



### 插件，扩展库

1. 用来帮助开发者快速实现某些功能



#### flask_script

		1. 使用它实现了终端参数接受，运行项目
  		2. 使用流程
           1.   安装插件，安装扩展库
         
           2.   初始化插件，使用app对象进行Manager对象初始化
	
       3.   运行时，修改为Manager.run()
         
          	3. 使用方法
            
               1.  ```
                   python manage.py runserver -h 127.0.0.1 -p 9000 -r -d
                   ```
              
                   
           
                		1. 进入一个flask环境的终端
                   		2. runserver
                   		1. 运行服务器
                      		2. r - 自动重新加载
                         		3. d - debug模式
                            		4. p - port 端口
                               		5. h - host主机
                                  		6. threaded - 是否使用多线程
                                     		7. ?, - help



## views

​	1. 试图函数

​			1. 协调模型和模板的关系

​			2. 处理业务逻辑

​	2. 和试图函数直接对接的是路由  route

​			1. route可以接受请求

​			2. 还可以接受请求参数

​					1. 路径参数

​					2. 语法<var>

​					3. 原型语法  <<converter:var>>

​							1. string 默认值，string中不能包含 / ，会把认为是路径分隔

​							2. int 限制输入的参数内容为int类型，如不是Int类型则不能完成匹配

​							3. float 限制输入的参数内容为浮点型

​							4. path 接收到的类型为字符串类型，可以接受 / ，会把 / 认为是普通的字符

​							5. uuid 限制输入数据类型为uuid（格式）数据类型，接收到之后会自动转换为uuid类



## route规则

#### 请求方法

​			@app.route(‘/rule/’, methods=[‘GET’, ‘POST’])

​			def hello():

​				return ‘LOL’

#### methods中的指定请求方法

​			1. GET

​			2. POST

​			3. HEAD

​			4. PUT

​			5. DELETE

​			... ...

#### 方向解析 url_for

1. 在flask中根据函数名获取url或获取path

   			2. 如果携带参数 url_for(‘函数’, key=value
            			1. url_for(‘函数名’, 参数名=value)

​	



### 蓝图（蓝本）

1. 本意是对美好事物的向往，规划
2. flask中蓝图代表的是对程序的一个美好规划，视图函数
3. 使用流程
   1. 下载安装
      
      1. ```
         pip install flask-blueprint
         ```
      
   2. 初始化
      1. 创建blueprint初始化对象
      
         - ```
           blue = Blueprint('my_first_blueName', __name__)
           ```
      
           
      
      2. 在manage.py内注蓝图，app.register_blueprint
      
         - ```
           app.register_blueprint(blueprint=blue)
           ```
      
   3. 开始使用
      1. 使用和app一致
      2. @blue.route(‘/路由地址’)



### Response

1. content, code
   1. code 根据实际需要指定
   2. 要符合状态码规则
   3. 也有可能用在反爬虫上（不论请求时成功与否都返回状态码404）

2. render_template

   1. 使用完全同上

   2. Template()配合Render(key=value, key1=value1, ...)

   3. make_response()

      1. 制作一个响应
      2. 返回的结果为Response的一个对象

   4. 直接实例化Response对象

      1. 最底层的方式

   5. 可使用重定向

      1. redirect(地址)
      2. url_for 反向解析获得

   6. 可返回json

      1. jsonfiy
         1. 支持直接的字典传输
         2. 构造使用key=value, key=value

   7. 可终止响应

      1. abort
      2. 只需传递中止的状态码

      

### 爬虫

1. 数据抓取
2. 数据提取
   1. 提取正常响应
   2. 状态码异常的通常不会继续提取
3. 数据存储







### 状态码

1. 每次Http请求都会收到HttpResponse

2. 每次HttpResponse都会携带一个对应的状态码

3. #### 1xx - 消息

   1. 100 Continue

      1. 服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。

   2. 101 Switching Protocols

      1. 服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。  

   3. 103 Checkpoint

      1. 用于 PUT 或者 POST 请求恢复失败时的恢复请求建议。

   4. #### 2xx - 成功

      1. 200 OK
         1. 请求成功（这是对HTTP请求成功的标准应答。）
      2. 201 Created
         1. 请求被创建完成，同时新的资源被创建。
      3. 202 Accepted
         1. 供处理的请求已被接受，但是处理未完成。
      4. 203 Non-Authoritative Information
         1. 请求已经被成功处理，但是一些应答头可能不正确，因为使用的是其他文档的拷贝。
      5. 204 No Content
         1. 请求已经被成功处理，但是没有返回新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。
      6. 205 Reset Content
         1. 请求已经被成功处理，但是没有返回新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。
      7. 206 Partial Content
         1. 客户发送了一个带有Range头的GET请求，服务器完成了它。

   5. #### 3xx - 重定向

      1. 300 Multiple Choices
         1. 多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。
      2. 301 Moved Permanently
         1. 所请求的页面已经转移至新的 URL 。
      3. 302 Found
         1. 所请求的页面已经临时转移至新的 URL 。
      4. 303 See Other
         1. 所请求的页面可在别的 URL 下被找到。
      5. 304 Not Modified
         1. 未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。服务器告诉客户，原来缓冲的文档还可以继续使用。
      6. 305 Use Proxy
         1. 客户请求的文档应该通过Location头所指明的代理服务器提取。
      7. 306 Switch Proxy
         1. 目前已不再使用，但是代码依然被保留。
      8. 307 Temporary Redirect
         1. 被请求的页面已经临时移至新的 URL 。
      9. 308 Resume Incomplete
         1. 用于 PUT 或者 POST 请求恢复失败时的恢复请求建议。

   6. #### 4xx - 客户端错误

      1. 400 Bad Request
         1. 因为语法错误，服务器未能理解请求。
      2. 401 Unauthorized
         1. 合法请求，但对被请求页面的访问被禁止。因为被请求的页面需要身份验证，客户端没有提供或者身份验证失败。
      3. 402 Payment Required
         1. 此代码尚无法使用。
      4. 403 Forbidden
         1. 合法请求，但对被请求页面的访问被禁止。
      5. 404 Not Found
         1. 服务器无法找到被请求的页面。
      6. 405 Method Not Allowed
         1. 请求中指定的方法不被允许。
      7. 406 Not Acceptable
         1. 服务器生成的响应无法被客户端所接受。
      8. 407 Proxy Authentication Required
         1. 用户必须首先使用代理服务器进行验证，这样请求才会被处理。
      9. 408 Request Timeout
         1. 请求超出了服务器的等待时间。
      10. 409 Conflict
          1. 由于冲突，请求无法被完成。
      11. 410 Gone
          1. 被请求的页面不可用。
      12. 411 Length Required
          1. "Content-Length" 未被定义。如果无此内容，服务器不会接受请求。
      13. 412 Precondition Failed
          1. 请求中的前提条件被服务器评估为失败。
      14. 413 Request Entity Too Large
          1. 由于所请求的实体太大，服务器不会接受请求。
      15. 414 Request-URI Too Long
          1. 由于 URL 太长，服务器不会接受请求。当 POST 请求被转换为带有很长的查询信息的 GET 请求时，就会发生这种情况。
      16. 415 Unsupported Media Type
          1. 由于媒介类型不被支持，服务器不会接受请求。
      17. 416 Requested Range Not Satisfiable
          1. 客户端请求部分文档，但是服务器不能提供被请求的部分。
      18. 417 Expectation Failed
          1. 服务器不能满足客户在请求中指定的请求头。

#### 5xx - 服务器错误

1. 500 Internal Server Error

   1. 请求未完成。服务器遇到不可预知的情况。

2. 501 Not Implemented

   1. 请求未完成。服务器不支持所请求的功能，或者服务器无法完成请求。

3. 502 Bad Gateway

   1. 请求未完成。服务器充当网关或者代理的角色时，从上游服务器收到一个无效的响应。

4. 503 Service Unavailable

   1. 服务器当前不可用（过载或者当机）。

5. 504 Gateway Timeout

   1. 网关超时。服务器充当网关或者代理的角色时，未能从上游服务器收到一个及时的响应。

6. 505 HTTP Version Not Supported

   1. 服务器不支持请求中指明的HTTP协议版本。

7. 511 Network Authentication Required

   1. 用户需要提供身份验证来获取网络访问入口。

   



## 会话技术

1. 出现场景
   - 不同请求，可能后续的请求需要前面请求返回的数据
2. 解决问题
   - web开发中http短链接
   - 从request到response请求的生命周期结束
3. 解决方案
   - cookie
     - 客户端会话技术
     - 所有信息存储在客户端，服务端不做人和存储
     - cookie 默认不支持中文
     - flask 默认支持中文
       - 当传入中文cookie值时，会被自动编码并在获取时自动解码
     - cookie 默认会携带本网站所有cookie
       - 网站值得ip和域名 
     - cookie不能跨域名，浏览器
       - 想跨域名，frame
   - session
     - 服务端会话技术
     - 数据都存储在服务器中
       - 内存中
     - 依赖于cookie存在
     - flask中session默认过期31天



### 模板

1. 模板适用于开发者快速实现生成html页面

2. 模板构成

   - 静态html
   - 模板语法

3. 模板语法

   - {{var }}
   - {% tag %}

4. 模板和视图函数对应关系

   - 多对多
   - 一个视图函数上，可以添加多个路由

5. 模板标签

   - 结构标签
     - block
     - extends
       - 如果多次继承，填充，会覆盖之前的内容
       - 如不想block中的内容被覆盖，需要使用 {{ super() }}
     
   - include 包含，能用extends和block快捷实现的，就尽量少用include

   - macro宏定义

     - jinja2模板引擎的亮点

     - 可自定义函数，并支持传参

     - 语法

       - { % macro xxx(yy,zz,...) % }

       - { % endmacro % }

         - ```
           filename：learn_macro.html
           
           {% macro say_hello(who) %}
           <h2>坚持{{ who }}</h2>
           {% endmacro %}
           ```

     - 可以实现复用

     - 可以被导入

     - ```
       {% from 'learn_macro.html' import say_hello %}
           {{ say_hello('Jeffrey') }}
       ```

       

6. 反向解析

   - url_for()
   - app
     - url_for(‘函数名’)
   - blueprint
     - url_for(‘蓝图名’.函数名)
   - static
     - url_for(‘static’, filename=‘文件名’)

7. 

8. 

9. 

10. 






### Flask-bootstrap

- 原生继承了一个Bootstrap
- 可以直接使用
- 内部划分了各个模块
  - bootstrap/
    - __init__.py
    - forms.py
    - nav.py
      - base.html
      - fixes.html
      - google.html
      - pagination.html
      - utils.html
      - wtf.html



#### Flask

- 闪过一个消息
- 通常用来在前段做提示
- 在views中使用flask函数，将消息传递出去
- 在模板中 get_flask_messages()





### 登录功能

1. 个人中心
   - cookie信息获取
2. 等于
   - form表单提交
   - cookie数据存储
3. 退出
   - cookie数据清除

