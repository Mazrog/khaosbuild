import os
from subprocess import run
from dotenv import dotenv_values

class cmake:
    min_version = "3.5.0"
    config = "Debug"
    opts = { "CMAKE_BUILD_TYPE": config }
    command = "/usr/bin/cmake"

    @staticmethod
    def configure(dependency_list):
        root_cmake = os.path.join(os.getenv("KHAOS_SRC"), "CMakeLists.txt")
        with open(root_cmake, "w") as cmake_file:
            cmake_file.write("cmake_minimum_required ( VERSION %s FATAL_ERROR )\n" % cmake.min_version)
            cmake_file.write("project ( KhaOS )\n\n")

            for dep in dependency_list:
                cmake_file.write("add_subdirectory ( %s )\n" % dep)
            pass

        
        # opt_str = ""
        # for (option, value) in cmake.opts.items():
        #     opt_str += ("-D%s=%s" % (option, str(value)))

        # command = [cmake.command, opt_str, src_path]

        # print("\nRunning %s\n\n" % " ".join(command))

        # run(command, cwd=wd)
    
    @staticmethod
    def make(build_dir=None):
        command = [cmake.command, "--build", build_dir, "--target", "all", "--", "-j", "2"]

        print("\nRunning %s\n\n" % " ".join(command))

        run(command)
