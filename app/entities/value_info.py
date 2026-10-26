# 用于定义字段取值的业务实体类
from dataclasses import dataclass

@dataclass
class ValueInfo:
  id: str         # 取值编号
  value: str      # 字段取值
  column_id: str  # 所属列编号
