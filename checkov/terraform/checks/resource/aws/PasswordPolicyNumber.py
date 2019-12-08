from checkov.terraform.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_check import BaseResourceCheck


class PasswordPolicyNumber(BaseResourceCheck):
    def __init__(self):
        name = "Ensure IAM password policy requires at least one number"
        id = "BC_AWS_IAM_6"
        supported_resources = ['aws_iam_account_password_policy']
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            validates iam password policy
            https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy.html
        :param conf: aws_iam_account_password_policy configuration
        :return: <CheckResult>
        """
        key = 'require_numbers'
        if key in conf.keys():
            if conf[key]:
                return CheckResult.SUCCESS
        return CheckResult.FAILURE


check = PasswordPolicyNumber()