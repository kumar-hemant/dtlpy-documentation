import behave
from docs_build.tutorials_templates.data_management.upload_and_manage_annotations import scripts


@behave.when(u'I prepared test upload and manage annotations')
def step_impl(context):
    sections_list = {
        "section1": section1_prepare
    }
    section_name = context.table.rows[0].cells[0]

    context.scripts = scripts
    sections_list[section_name](context)


def section1_prepare(context):
    context.project = context.dl.projects.create('upload_and_management_annotations_project')