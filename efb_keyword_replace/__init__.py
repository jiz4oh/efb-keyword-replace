import yaml
from typing import Optional, Dict, Any

from ehforwarderbot import Middleware, Message, coordinator, utils
from ehforwarderbot.types import ModuleID, InstanceID

class KeywordReplaceMiddleware(Middleware):
    middleware_id: ModuleID = ModuleID("jiz4oh.keyword_replace")
    middleware_name: str = "Keyword Replace Middleware"
    __version__: str = "0.1.0"

    def __init__(self, instance_id: Optional[InstanceID] = None):
        super().__init__(instance_id)
        config_path = utils.get_config_path(self.middleware_id)
        self.config = self.load_config(config_path)
        self.keywords = (
            self.config["keywords"] if "keywords" in self.config.keys() else {}
        )

    @staticmethod
    def load_config(path: str) -> Dict[str, Any]:
        if not path.exists():
            return
        with path.open() as f:
            d = yaml.full_load(f)
            if not d:
                return
            config: Dict[str, Any] = d
        return config

    @staticmethod
    def replace_keywords(text: str, replacements: Dict[str, str]) -> str:
        """
        根据字典替换字符串中的关键字。

        该函数会遍历替换字典，并将文本中出现的每个键（关键字）
        替换为其对应的值。为了正确处理重叠的关键字（例如 "apple" 和
        "apple pie"），它会优先替换较长的关键字。

        Args:
            text: 需要进行关键字替换的原始字符串。
            replacements: 一个字典，其中键是要查找的关键字，值是用于替换的字符串。

        Returns:
            一个新的字符串，其中关键字已被替换。
            'Blue is red.' # 注意：默认是大小写敏感的
        """
        # 如果替换字典为空，直接返回原文本
        if not replacements:
            return text

        # 按键的长度降序排序，确保优先替换更长的关键字
        # 例如，先替换 "apple pie" 再替换 "apple"
        sorted_keywords = sorted(replacements.keys(), key=len, reverse=True)

        new_text = text

        # 遍历排序后的关键字列表
        for keyword in sorted_keywords:
            replacement_value = replacements[keyword]
            # 使用 str.replace() 进行替换
            # 注意：str.replace() 是大小写敏感的，并且会替换所有出现的子字符串
            new_text = new_text.replace(keyword, replacement_value)

        return new_text

    def process_message(self, message: Message) -> Optional[Message]:
        message.text = self.replace_keywords(message.text, self.keywords)
        return message
