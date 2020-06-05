import unittest

from checkov.terraform.checks.resource.gcp.GKEUseCosImage import check
from checkov.common.models.enums import CheckResult


class TestGKEUseCosImage(unittest.TestCase):

    def test_failure(self):
        resource_conf = {'name': ['google_cluster_bad'], 'monitoring_service': ['none'], 'enable_legacy_abac': [True], 'master_authorized_networks_config': [{'cidr_blocks': [{'cidr_block': ['0.0.0.0/0'], 'display_name': ['The world']}]}], 'master_auth': [{'username': ['test'], 'password': ['password']}], 'resource_labels': [{}]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        resource_conf = {'name': ['google_cluster'], 'enable_legacy_abac': [False], 'resource_labels': [{'Owner': ['SomeoneNotWorkingHere']}], 'node_config': [{'image_type': ['cos']}]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)

    def test_success_case_insensitive(self):
        resource_conf = {'name': ['google_cluster'], 'enable_legacy_abac': [False], 'resource_labels': [{'Owner': ['SomeoneNotWorkingHere']}], 'node_config': [{'image_type': ['COS_CONTAINERD']}]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == '__main__':
    unittest.main()
