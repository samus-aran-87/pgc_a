import logging
import math

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "loggerTest.Log", level = logging.DEBUG, 
    format = LOG_FORMAT, 
    filemode = 'w')

logger = logging.getLogger()

# Test messages
# logger.debug("123")


def quadratic_formular(a,b,c):
    """ Return the solution to the equation ax^2 + bx + c = 0."""
    logger.info('quadratic_formular({0}, {1}, {2})'.format(a,b,c))

    # Complete the discriminant
    logger.debug('# Complete the discriminant')
    disc = b**2 - 4*a*c

    # Complete the two roots
    logger.debug('# Complete the two roots')
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug('# Return the roots')
    return (root1, root2)

roots = quadratic_formular(1, 0, -4)
print(roots)