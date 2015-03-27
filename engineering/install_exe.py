import sys
import logging
from utils import print_log, get_hybrid_cloud_badam_path
sys.path.append(get_hybrid_cloud_badam_path())

from common import config
from common.econstants import OperationType
from engineering_factory import EnginneringFactory, HostnameConfigurator, AllInOneConfigurator
from installation import CascadingDeploy
from utils import ELog

module_logger = logging.getLogger(__name__)
logger = ELog(module_logger)

def main():
    """
    How to use:
    Step1. Copy hybrid_cloud_badam and tricircle-master to <Your-Dir>
    Step2. Config <Your-Dir>/hybrid_cloud_badam/engineering/config/configuration.conf
    Step3. Install by execute following commands.
        # cd <Your-Dir>/hybrid_cloud_badam/engineering
        #python install_exe.py --config-file config/configuration.conf
    :return:
    """
    logger.info('Start to doing deploy...')

    operation = config.CONF.sysconfig.operation
    logger.info('Your operation is - <%s>' % operation)
    if operation == OperationType.CFG_HOST_NAME:
        EnginneringFactory(operation, configurator=HostnameConfigurator()).execute()
    elif operation == OperationType.CFG_ALL_IN_ONE:
        EnginneringFactory(operation, configurator=AllInOneConfigurator()).execute()
    elif operation == OperationType.DEPLOY_HYBRID_CLOUD:
        CascadingDeploy().deploy_cascading_modules()
    else:
        err_info = 'Invalid operation-<%s>, please check your config file.' % operation
        print (err_info)
        logger.error(err_info)


    logger.info('End to do deploy..')

if __name__ == '__main__':
    main()
