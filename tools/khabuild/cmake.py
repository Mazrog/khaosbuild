import os
from subprocess import run

import repos_utils

class cmake:
    min_version = "3.5.0"
    command = "/usr/bin/cmake"

    @staticmethod
    def configure(project_name):
        root_cmake = os.path.join(os.getenv("KHAOS_SRC"), "CMakeLists.txt")
        common_cmake = os.path.join(os.getenv("KHAOS_ROOT"), "common.cmake")

        dependencies = repos_utils.get_dependencies_dict()
        dependency_list = dependencies[project_name] + [ project_name ]

        with open(root_cmake, "w") as cmake_file:
            cmake_file.write("cmake_minimum_required ( VERSION %s FATAL_ERROR )\n" % cmake.min_version)
            cmake_file.write("project ( %s )\n\n" % project_name)

            cmake_file.write("include ( %s )\n\n" % common_cmake)

            for dep in dependency_list:
                cmake_file.write("\nmessage ( \"\\nEntering repository %s...\" )\n" % dep)
                cmake_file.write("add_subdirectory ( %s )\n" % dep)

                cmake_file.write("publish_files ( %s )\n" % dep)
                
                sub_dep = dependencies[dep]
                if sub_dep:
                    cmake_file.write("add_dependencies ( %s %s )\n" % (dep, " ".join(sub_dep)))
            

    @staticmethod
    def reload(config, env):
        wd = os.path.join(os.getenv("KHAOS_BUILD"), "cache", config.title())

        if not os.path.exists(wd):
            os.makedirs(wd)

        # We are now computing the variables from the environment
        args_str = ""
        for (option, value) in env.items():
            args_str += ("-D%s=%s" % (option, str(value))) 

        command = [ cmake.command, args_str, os.getenv("KHAOS_SRC") ]
        
        print("\nRunning %s\n\n" % " ".join(command))
        run(command, cwd=wd)

    @staticmethod
    def make(build_dir, target):
        command = [cmake.command, "--build", build_dir, "--target", target, "--", "-j", "2"]

        print("\nRunning %s\n\n" % " ".join(command))

        run(command, cwd=build_dir)
