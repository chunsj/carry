from invoke import task, run
import contextlib
import os
import shutil


@task
def site():
    """ Compiles examples and builds project site. """
    run("mkdocs build --clean", echo=True)

    site_path = os.path.join(os.getcwd(), "site")
    with chdir(os.path.join("examples", "todomvc")):
        lein("cljsbuild once")
        shutil.copytree("resources",
                        os.path.join(site_path, "examples", "todomvc"))


################################################### HELPERS
@contextlib.contextmanager
def chdir(dirname=None):
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


def lein(args):
    run("lein {0}".format(args), echo=True)
