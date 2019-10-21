from conans import ConanFile, tools
import os


class ApprovalTestsCppConan(ConanFile):
    name = "approvaltests.cpp"
    version = "6.0.0"
    description = "Native ApprovalTests for C++ on Linux, Mac and Windows"
    topics = ("testing", "approval tests")
    url = "https://github.com/p-podsiadly/approvaltests.cpp"
    homepage = "https://github.com/approvals/ApprovalTests.cpp"
    author = "Piotr Podsiadły <ppodsiadly@mykolab.com>"
    license = "Apache-2.0"
    no_copy_source = True
    exports_sources = ["ApprovalTests.hpp.in"]

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    def source(self):
        tools.download(self.conan_data["sources"][self.version]["url"], "approvals/ApprovalTests.v%s.hpp" % self.version)
        tools.check_sha256("approvals/ApprovalTests.v%s.hpp" % self.version, self.conan_data["sources"][self.version]["sha256"])

        os.rename("ApprovalTests.hpp.in", "approvals/ApprovalTests.hpp")
        tools.replace_in_file("approvals/ApprovalTests.hpp", "VERSION", self.version)

    def package(self):
        self.copy(pattern="*", dst="include/approvals", src="approvals")

    def package_info(self):
        self.cpp_info.includedirs = ["include", "include/approvals"]

    def package_id(self):
        self.info.header_only()
