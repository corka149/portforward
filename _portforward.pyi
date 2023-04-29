"""
Rust native module / Python C Extension
"""

async def forward(
    namespace: str,
    pod_or_service: str,
    from_port: int,
    to_port: int,
    config_path: str,
    log_level: int,
    kube_context: str,
) -> None:
    pass

async def stop(namespace: str, pod_or_service: str, log_level: int) -> None:
    pass
