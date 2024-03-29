# 自定义打开文件操作
class MyOpen(object):

    def __init__(self, file_name):
        """初始化方法"""
        self.file_name = file_name
        self.file_handler = None
        return

    def __enter__(self):
        """enter方法，返回file_handler"""
        print("enter:", self.file_name)
        self.file_handler = open(self.file_name, "r")
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        """exit方法，关闭文件并返回True"""
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True


# 使用实例
with MyOpen("python_base.py") as file_in:
    for line in file_in:
        print(line)
        raise ZeroDivisionError
# 代码块中主动引发一个除零异常，但整个程序不会引发异常
