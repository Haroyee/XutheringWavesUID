from gsuid_core.logger import logger

def calc_percent_expression(*args, **kwargs):
    try:
        from ..waves_build.damage import calc_percent_expression as _func
        return _func(*args, **kwargs)
    except ImportError:
        logger.error("请等待下载完成")
        return 0

def __getattr__(name):
    if name == "DamageAttribute":
        try:
            from ..waves_build.damage import DamageAttribute
            globals()["DamageAttribute"] = DamageAttribute
            return DamageAttribute
        except ImportError:
            logger.error("请等待下载完成")
            return None
    
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    
def check_char_id(*args, **kwargs):
    try:
        from ..waves_build.damage import check_char_id as _func
        return _func(*args, **kwargs)
    except ImportError:
        logger.error("请等待下载完成")
        return False