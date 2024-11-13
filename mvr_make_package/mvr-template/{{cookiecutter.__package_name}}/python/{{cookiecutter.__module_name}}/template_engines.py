
from mvr_v2.common.utils import TemplateEngine

"""
One Template Engine can have multiple xml templates.
A single template engine is equivalent to a single commit operation.

"""


class Te1(TemplateEngine):
    def settings(self):
        # you can use multiple templates
        self.templates = ["{{ cookiecutter.__package_name }}-template"]

    def format_single_commit_comment(self, _input) -> str:
        # return _input.device_name
        return 'single commit for {{ cookiecutter.__package_name }}'

    def format_splitted_commit_comment(self, _single_payload_instance) -> str:
        # return _single_payload_instance.interface_id
        return 'splitted commit for {{ cookiecutter.__package_name }}'


class Te2(TemplateEngine):
    def settings(self):
        # you can use multiple templates
        self.templates = ["{{ cookiecutter.__package_name }}-template"]

    def format_single_commit_comment(self, _input) -> str:
        # return _input.device_name
        return 'single commit for {{ cookiecutter.__package_name }}'

    def format_splitted_commit_comment(self, _single_payload_instance) -> str:
        # return _single_payload_instance.interface_id
        return 'splitted commit for {{ cookiecutter.__package_name }}'
