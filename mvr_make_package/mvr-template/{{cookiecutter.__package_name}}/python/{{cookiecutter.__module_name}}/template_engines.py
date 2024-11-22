
from mvr_v2.common.utils import TemplateEngine

"""
One Template Engine can have multiple xml templates.
A single template engine is equivalent to a single commit operation.

"""


class Te1(TemplateEngine):
    """
    This class holds NSO `xml` templates to be applied.
    Multiple templates can be specified, with each instance corresponding to a single commit operation.
    `mvr` will iteratively apply the specified template(s) for each normalized correlated payload.
    """

    def settings(self):
        """
        This callback method is invoked by MVR to retrieve the names of the templates.
        The template names should be assigned to the `self.templates` attribute as a list of strings.
        """
        # you can use multiple templates
        self.templates = ["{{ cookiecutter.__package_name }}-template"]

    def format_single_commit_comment(self, _input) -> str:
        # return _input.device_name
        return 'single commit for {{ cookiecutter.__package_name }}'


class Te2(TemplateEngine):
    """
    This class holds NSO `xml` templates to be applied.
    Multiple templates can be specified, with each instance corresponding to a single commit operation.
    `mvr` will iteratively apply the specified template(s) for each normalized correlated payload.
    """

    def settings(self):
        """
        This callback method is invoked by MVR to retrieve the names of the templates.
        The template names should be assigned to the `self.templates` attribute as a list of strings.
        """
        # you can use multiple templates
        self.templates = ["{{ cookiecutter.__package_name }}-template"]

    def format_single_commit_comment(self, _input) -> str:
        # return _input.device_name
        return 'single commit for {{ cookiecutter.__package_name }}'
