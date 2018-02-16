from conans import ConanFile, CMake


class CeleroConan(ConanFile):
    name = "Celero"
    version = "2.1.1"
    license = "Apache License Version 2.0"
    url = "https://github.com/DigitalInBlue/Celero-Conan"
    description = "C++ Benchmark Authoring Library/Framework"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        gitRepo = "https://github.com/DigitalInBlue/Celero.git"
        commitID = "v2.1.1"
        self.run("git init")
        self.run("git fetch %s %s" % (gitRepo,commitID))
        self.run("git reset --hard FETCH_HEAD")

    def build(self):
        cmake = CMake(self)
        if self.options.shared:
            cmake.definitions["CELERO_COMPILE_DYNAMIC_LIBRARIES"] = "ON"
        else:
            cmake.definitions["CELERO_COMPILE_DYNAMIC_LIBRARIES"] = "OFF"
        cmake.definitions["CELERO_ENABLE_EXPERIMENTS"] = "OFF"
        cmake.definitions["CELERO_ENABLE_FOLDERS"] = "OFF"
        cmake.configure()
        cmake.build(target="celero")
        cmake.install()

    def package(self):
        self.copy("*", src="package")

    def package_info(self):
        self.cpp_info.libs = ["celero"]
        self.cpp_info.libdirs = ["lib","lib/static","bin"]
