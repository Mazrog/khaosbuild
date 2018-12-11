import os
from subprocess import run

class git:
    command = "git"

    @staticmethod
    def pull(url, repo):
        """
        pull a git repository
        url: [string]  repo url to pull from
        repo: [string] repository name in the src/ folder
        """
        src_path = os.getenv("KHAOS_SRC")
        path = os.path.join(src_path, repo)

        _, filename = os.path.split(path)
        if os.path.exists(path):
            print("Pulling repo %s..." % filename)
            run([git.command, "pull"], cwd=path)
        else:
            print("Cloning repo %s into %s..." % (filename, path))
            run([git.command, "clone", url, path])

    @staticmethod
    def commit(repo):
        pass

    @staticmethod
    def status(repo):
        wd = os.path.join(os.getenv("KHAOS_SRC"), repo)
        command = [ git.command, "status" ]

        print("-" * 50)
        print("\n%s: Running %s\n\n" % (wd, " ".join(command)))
        
        run(command, cwd=wd)