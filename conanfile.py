from conans import ConanFile, tools
import os


class ApprovalTestsCppConan(ConanFile):
    name = "approvaltests.cpp"
    version = "7.0.0"
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

    _header_url = "https://github.com/approvals/ApprovalTests.cpp/releases/download/v.7.0.0/ApprovalTests.v.7.0.0.hpp"
    _header_sha256 = "9dd54bcf46171b29cdabbd1d2ee8be0ecf7cd3356379f2a309cfb16696ecc75c"

    def source(self):
        tools.download(self._header_url, "approvals/ApprovalTests.v%s.hpp" % self.version)
        tools.check_sha256("approvals/ApprovalTests.v%s.hpp" % self.version, self._header_sha256)

        tools.replace_in_file(
            "approvals/ApprovalTests.v%s.hpp" % self.version,
            "#include <doctest.h>\n",
            "#include <doctest/doctest.h>\n",
            strict=True)

        os.rename("ApprovalTests.hpp.in", "approvals/ApprovalTests.hpp")
        tools.replace_in_file("approvals/ApprovalTests.hpp", "VERSION", self.version)

    def package(self):
        self.copy(pattern="*", dst="include/approvals", src="approvals")

    def package_info(self):
        self.cpp_info.includedirs = ["include", "include/approvals"]

    def package_id(self):
        self.info.header_only()
