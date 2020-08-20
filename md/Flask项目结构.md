### Flask 项目结构规划
- 创建一个app包，主要用于放应用
- 在App包中的入口文件 __init__.py 中创建flask程序并进行初始化
    - 初始化自己
    - 使用配置文件，在flask上进行设置
    - 初始化蓝图（views）
    - 初始化第三方（ext）
    
### 项目结构
- manage.py 用来全局控制程序项目
- App 项目
    - App/__init__ 初始化，使用进行项目的初始化
    - App/views 视图函数，用来处理请求
        - views中使用蓝图进行的实现
    - App/models 模型，用于定义和数据库映射对象
        - 使用orm进行实现
    - App/settings 设置，配置，App应用的配置文件
        - 全局设置
        - 设置多套环境的配置
    - App/ext 扩展库，第三方扩展库统一管理     
        - 轻量级框架
        - 第三方插件多，可以统一处理
### flask-migrate
- 数据库迁
- 使用流程
    - 安装 pip install flask-migrate
    - 进行初始化
        - 在ext中进行初始化
        - 迁移库需要同时绑定app和db
        
    - 使用方法(原生方法，针对默认结构有效，修改的结构需要额外配置)
        - flask db init
        - flask db migrate
        - flask db upgrade
        - flask db downgrade
        - flask db -- help
    - 集成 flask-script 使用
        - 安装使用流程进行配置
        - 添加和flask-script对接的代码
        - 在manage添加命令
            -manager.add_command('db', MigrateCommand)
        使用
            - Python manage.py db init
                - 初始化，每个项目只调用一次，生成迁移结构
            - Python manage.py db migrate
                - 生成迁移文件，会在根目录生成迁移文件
                - 调用时机，每次修改model之后
            - Python manage.py db upgrade|
                - 执行迁移文件
                - 将修改映射到数据库中，增量的
            - Python.manage.py db downgrade
                - 执行迁移文件
                - 降级操作
                - 可用于操作失误后
            - Python.manage.py db -- help
                - 查看帮助
### 配置
- 企业中开发，可能同时拥有多套运行环境
- 可以直接写一个文件，实现多套环境的配置
- 环境中有很多通用部分，可以进行一个代码提取

### 模型定义
-类型定义
-约束定义
    - index 索引不能乱用
    - 它会额外维护索引表
    - 比较常用的场景,pk,fk
    - 不常修改还非常具有代表性的字段

### 数据查询
- query.all 返回的是list列表
- query.filter(条件) 返回的是BaseQuery
- query.filter_by(条件) 级联查询常用
- offset 偏移，跳过多少条
- limit 限制结果集
- order_by 排序
- get 获取单个资源
- first 第一条（没有最后一条，last）
- paginate 分页
