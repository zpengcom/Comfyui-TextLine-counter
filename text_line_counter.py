class TextLineCounter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_input": ("STRING", {
                    "multiline": True,  # 启用多行文本输入
                    "default": ""  # 默认值为空
                })
            }
        }

    RETURN_TYPES = ("STRING", "INT")  # 输出类型：字符串和整数
    RETURN_NAMES = ("output_text", "line_count")  # 输出端口名称
    FUNCTION = "count_lines"  # 执行函数名
    CATEGORY = "Text Processing"  # 节点分类

    def count_lines(self, text_input):
        # 计算行数（按换行符分割并过滤空行）
        lines = text_input.splitlines()
        line_count = len([line for line in lines if line.strip()])  # 仅统计非空行
        return (text_input, line_count)  # 返回原始文本和行数

# 节点映射
NODE_CLASS_MAPPINGS = {
    "TextLineCounter": TextLineCounter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextLineCounter": "Text Line Counter"
}