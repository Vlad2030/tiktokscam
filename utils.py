import modules.logs


def on_startup(dispatcher) -> None:
    return modules.logs.logger.warning(msg="Bot started!")


def on_shutdown(dispatcher) -> None:
    return modules.logs.logger.warning(msg="Bot shutdown!")