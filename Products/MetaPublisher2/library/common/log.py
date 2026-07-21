"""MetaPublisher - Logging Service."""


__all__ = [
    'log',
]


# ============================================================================
# Logging

try:

    from logging import getLogger
    logger = getLogger('MetaPublisher2')

    def log(message):
        """Log a message."""
        logger.info(message)

except Exception:

    from zLOG import LOG, INFO

    def log(message):
        """Log a message."""
        LOG('MetaPublisher2', INFO, message)
