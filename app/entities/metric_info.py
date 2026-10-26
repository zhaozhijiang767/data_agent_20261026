# 用于定义指标信息的业务实体类
from dataclasses import dataclass

@dataclass
class MetricInfo:
  id: str                      # 指标编码
  name: str                    # 指标名称
  description: str             # 指标描述
  relevant_columns: list[str]  # 关联的列
  alias: list[str]             # 指标别名
