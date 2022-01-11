import random


from model.project import Project


def test_del_project(app):
    if len(app.soap.get_projects()) == 0:
        app.project.add_new_project(Project(name="Del1", description="descr"))
    old_projects = app.soap.get_projects()
    project = random.choice(old_projects)
    app.project.del_project_by_name(project.name)
    old_projects.remove(project)
    new_projects = app.soap.get_projects()
    assert sorted(old_projects, key=lambda project:project.name) == sorted(new_projects, key=lambda project:project.name)

