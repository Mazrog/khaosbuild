import os
from subprocess import run

class cmake:
    min_version = "3.5.0"
    command = "/usr/bin/cmake"

    @staticmethod
    def configure(project_name, env, dependency_list):
        root_cmake = os.path.join(os.getenv("KHAOS_SRC"), "CMakeLists.txt")
        common_cmake = os.path.join(os.getenv("KHAOS_ROOT"), "common.cmake")

        with open(root_cmake, "w") as cmake_file:
            cmake_file.write("cmake_minimum_required ( VERSION %s FATAL_ERROR )\n" % cmake.min_version)
            cmake_file.write("project ( %s )\n\n" % project_name)

            cmake_file.write("include ( %s )\n\n" % common_cmake)

            for dep in dependency_list:
                cmake_file.write("add_subdirectory ( %s )\n" % dep)
            
            opt_str = ""
            for (option, value) in env.items():
                opt_str += ("-D%s=%s" % (option, str(value))) 

            print("\nConfigured CMake with the following : %s %s\n\n" % (cmake.command, opt_str)


    @staticmethod
    def make(build_dir=None):
        command = [cmake.command, "--build", build_dir, "--target", "all", "--", "-j", "2"]

        print("\nRunning %s\n\n" % " ".join(command))

        run(command)
