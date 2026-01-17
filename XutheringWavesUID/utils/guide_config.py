import json
import re
from typing import Dict, List

from gsuid_core.logger import logger

from .resource.RESOURCE_PATH import GUIDE_CONFIG_PATH


def load_guide_config() -> Dict:
    """加载攻略配置

    Returns:
        配置字典，格式: {"group_id": ["提供方1", "提供方2"]}
    """
    if not GUIDE_CONFIG_PATH.exists():
        return {}

    try:
        with open(GUIDE_CONFIG_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except Exception as e:
        logger.exception(f"加载攻略配置失败: {e}")
        return {}


def save_guide_config(config: Dict) -> bool:
    """保存攻略配置

    Args:
        config: 配置字典

    Returns:
        是否保存成功
    """
    try:
        with open(GUIDE_CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logger.exception(f"保存攻略配置失败: {e}")
        return False


def parse_provider_names(names: str) -> List[str]:
    """解析攻略提供方名称

    Args:
        names: 用逗号、中文逗号或空格分隔的提供方名称

    Returns:
        提供方名称列表
    """
    # 支持逗号、中文逗号、空格分隔
    parts = re.split(r'[,，\s]+', names.strip())
    return [p.strip() for p in parts if p.strip()]


def get_excluded_providers(group_id: str) -> List[str]:
    """获取群组排除的攻略提供方

    Args:
        group_id: 群组ID

    Returns:
        排除的提供方列表
    """
    config = load_guide_config()
    return config.get(group_id, [])
