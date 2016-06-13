#!coding:utf8

import os

from Araneae.core.engine import Engine
from Araneae.utils.log import get_logger
from Araneae.utils.settings import Settings
from Araneee.utils.loader import load_object
from Araneae.singleton import SchedulerFactory
from Araneae.utils.livetracker import LiveObject
from Araneae.downloaders.http import HttpDownloader
from Araneae.core.middleware import MiddlewareManager


"""spider中是一些爬虫独有的属性,不需要包含动作"""

logger = get_logger(__name__)

class Spider(LiveObject):
    """
    爬虫基类
    """

    def __init__(self, setting_path, distributed=False):
        self._pid = os.getpid()
        settings = Settings(setting_path)
        self.settings = settings
        self.engine = Engine(settings)
        self._initialize(distributed)

    def _initialize(self,distributed):
        """初始化spider组件"""

        self.set_spider_name()
        self.set_logger()

    def reset(self,distributed):
        """重新加载配置文件,构建spider"""

        self.reset_settings()
        self._initialize(distributed)

    def reset_settings(self):
        """重新加载配置文件"""

        self.settings.reset()

    def set_spider_name(self):
        """设置爬虫名"""

        self.name = self.setttings.get('SPIDER_NAME', dont_empty=True)

    def set_running_type(self,distributed):
        """设置运行类型
        singleton和distributed有不同的处理逻辑"""

        scheduler_cls = load_object(self.settings.get('SCHEDULER'))
        self._scheduler = scheulder_cls.from_spider(self)

        if distributed:
            pass
        else:
            dupefiler = load_object(self.settings.get('DUPEFILTER'))
            self._dupefilter = dupefilter.from_spider(self)
            self._scheduler = SchedulerFactory(self._scheduler, self._dupefilter)            
            self._rpc = self._scheudler

    def set_logger(self):
        """设置日志格式及路径"""

        log_path = self.settings.get('LOG_PATH')
        log_level = self.settings.get('LOG_LEVEL')
        terminal_log_level = self.settings.get('TERMINAL_LOG_LEVEL')
        self.logger = get_logger(log_path)
        self.logger.setLevel(log_level)


