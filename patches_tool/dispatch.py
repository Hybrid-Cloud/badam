__author__ = 'nash.xiejun'
import os

import log
import utils
import sshutils
from constants import SysUserInfo, SysPath, ScriptFilePath
from services import CPSServiceBusiness



class DispatchPatchTool(object):

    def __init__(self):
        # self.filter_for_dispatch = ['.py', '.sh', '.ini', '.pem', '.txt', '.vmx', '.json']
        self.filter_for_dispatch = []
        self.cps_service_business = CPSServiceBusiness()
        self.aws_cascaded_node_hosts = self.cps_service_business.get_aws_node_hosts()
        self.vcloud_cascaded_node_hosts = self.cps_service_business.get_vcloud_node_hosts()
        self.openstack_cascaded_node_hosts = self.cps_service_business.get_openstack_hosts()

    def dispatch_patch_tool_to_host(self, host):
        path_of_patch_tool = utils.get_patches_tool_path()
        files_need_to_dispatch = utils.get_files(path_of_patch_tool, self.filter_for_dispatch)

        ssh = sshutils.SSH(host=host, user=SysUserInfo.FSP, password=SysUserInfo.FSP_PWD)
        for absolute_file, relative_path_of_file in files_need_to_dispatch:
            log.info('start to copy file <<%s>> to host <<%s>>' % (relative_path_of_file, host))
            file_copy_to = os.path.join(SysPath.HOME_FSP, SysPath.PATCHES_TOOL, relative_path_of_file)
            file_dir_copy_to = os.path.dirname(file_copy_to)
            ssh.run('mkdir -p %s' % file_dir_copy_to)
            ssh.put_file(absolute_file, file_copy_to)
            log.info('End to copy file <<%s>> to host <<%s>>' % (relative_path_of_file, host))

        ssh.close()

    def dispatch_patches_tool_to_host_with_tar(self, host):
        local_full_path_of_tar_file = self.tar_patches_tool()
        ssh = sshutils.SSH(host=host, user=SysUserInfo.FSP, password=SysUserInfo.FSP_PWD)
        full_path_of_file_copy_to = os.path.join(SysPath.HOME_FSP, SysPath.PATCHES_TOOL_TAR_GZ)
        dir_of_patches_tool = os.path.join(SysPath.HOME_FSP, SysPath.PATCHES_TOOL)
        # remove dir: /home/fsp/patches_tool/
        ssh.run('rm -rf %s' % dir_of_patches_tool)
        # remove /home/fsp/patches_tool.tar.gz
        ssh.run('rm %s' % full_path_of_file_copy_to)
        ssh.put_file(local_full_path_of_tar_file, full_path_of_file_copy_to)
        ssh.run('tar -xzvf %s %s' % (full_path_of_file_copy_to, SysPath.HOME_FSP))
        ssh.close()


    def remove_tar_patches_tool(self, full_patch_of_patches_tool):
        if os.path.isfile(full_patch_of_patches_tool):
            os.remove(full_patch_of_patches_tool)

    def tar_patches_tool(self):
        patches_tool_path = utils.get_patches_tool_path()
        full_patch_of_patches_tool = os.path.join(patches_tool_path, SysPath.PATCHES_TOOL_TAR_GZ)

        self.remove_tar_patches_tool(full_patch_of_patches_tool)
        utils.make_tarfile(SysPath.PATCHES_TOOL_TAR_GZ, patches_tool_path)
        return full_patch_of_patches_tool


    def dispatch_patches_tool_to_remote_cascaded_nodes(self):
        self.dispatch_patches_tool_to_aws_cascaded_nodes()
        self.dispatch_patches_tool_to_vcloud_cascaded_nodes()
        self.dispatch_patches_tool_to_openstack_cascaded_nodes()

    def dispatch_patches_tool_to_aws_cascaded_nodes(self):
        for host in self.aws_cascaded_node_hosts:
            # self.dispatch_patch_tool_to_host(host)
            self.dispatch_patches_tool_to_host_with_tar(host)

    def dispatch_patches_tool_to_vcloud_cascaded_nodes(self):
        for host in self.vcloud_cascaded_node_hosts:
            # self.dispatch_patch_tool_to_host(host)
            self.dispatch_patches_tool_to_host_with_tar(host)

    def dispatch_patches_tool_to_openstack_cascaded_nodes(self):
        for host in self.openstack_cascaded_node_hosts:
            print('Host of openstack: %s' % host)
            # self.dispatch_patch_tool_to_host(host)
            self.dispatch_patches_tool_to_host_with_tar(host)

    def remote_patch_for_cascaded_nodes(self):
        self.remote_patch_vcloud_nodes()
        self.remote_patch_aws_nodes()

    def remote_patch_aws_nodes(self):
        for host in self.aws_cascaded_node_hosts:
            self.remote_patch_aws_node(host)

    def remote_patch_vcloud_nodes(self):
        for host in self.vcloud_cascaded_node_hosts:
            self.remote_patch_vcloud_node(host)

    def remote_patch_aws_node(self, host):
        ssh = sshutils.SSH(host=host, user=SysUserInfo.ROOT, password=SysUserInfo.ROOT_PWD)
        ssh.execute('python %s' % ScriptFilePath.PATH_REMOTE_AWS_PATCH_FILE)
        ssh.close()

    def remote_patch_vcloud_node(self, host):
        ssh = sshutils.SSH(host=host, user=SysUserInfo.ROOT, password=SysUserInfo.ROOT_PWD)
        ssh.execute('python %s' % ScriptFilePath.PATH_REMOTE_VCLOUD_PATCH_FILE)
        ssh.close()

    def remote_config_cascaded_for_all_type_node(self):
        for host in self.aws_cascaded_node_hosts:
            self.remote_config_openstack_cascaded_node(host)

        for host in self.vcloud_cascaded_node_hosts:
            self.remote_config_openstack_cascaded_node(host)

        for host in self.openstack_cascaded_node_hosts:
            self.remote_config_openstack_cascaded_node(host)

    def remote_config_openstack_cascaded_node(self, host):
        ssh = sshutils.SSH(host=host, user=SysUserInfo.ROOT, password=SysUserInfo.ROOT_PWD)
        ssh.execute('python %s cascaded' % ScriptFilePath.PATCH_REMOTE_HYBRID_CONFIG_PY)

if __name__ == '__main__':
    log.init('dispatch')
    print('Start to remote patch for AWS nodes and VCLOUD nodes.')
    dispatch_patch_tool = DispatchPatchTool()
    dispatch_patch_tool.remote_patch_for_cascaded_nodes()
    print('Finish to remote patch for AWS nodes and VCLOUD nodes.')