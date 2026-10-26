# 用于定义表格信息的业务实体类
from dataclasses import dataclass

@dataclass
class TableInfo:
    id: str           # 表编号
    name: str         # 表名称
    role: str         # 表类型：fact（事实表）/ dim（维表）
    description: str  # 表描述
