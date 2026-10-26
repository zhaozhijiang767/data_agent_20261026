# 用于定义字段信息的业务实体类
from dataclasses import dataclass
from typing import Any

@dataclass
class ColumnInfo:
  id: str              # 列编号
  name: str            # 列名称
  type: str            # 数据类型
  role: str            # 列类型：primary_key / foreign_key / measure（度量）/ dimension（维度）
  examples: list[Any]  # 数据示例
  description: str     # 列描述
  alias: list[str]     # 列别名
  table_id: str        # 所属表编号
